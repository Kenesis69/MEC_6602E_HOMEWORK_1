## Imports
import numpy as np
import matplotlib.pyplot as plt
import sys

## Discretization scheme definition
class explicit_backward: #0 Number of the discretization scheme
    def __call__(self, u, cfl):
        u[2:-2] -= cfl*(u[2:-2]-u[1:-3]) #Computing u for all position exepting border nodes

class explicit_forward: #1
    def __call__(self, u, cfl): u[2:-2] -= cfl*(u[3:-1]-u[2:-2])

class forwardT_centeredS: #2
    def __call__(self, u, cfl): u[2:-2] -= 0.5*cfl*(u[3:-1]-u[1:-3])

class leap_frog: #3
    u_previous = None
    def __call__(self, u, cfl):
        if self.u_previous is None:
            self.u_previous = u.copy() #The current state become the previous one
            scheme = explicit_backward()
            scheme(u,cfl) #Explicit Backward is used because we have no u at time n-1. We therefore take the speed at the initial time
        else:
            u_next = self.u_previous[2:-2]-cfl*(u[3:-1]-u[1:-3])
            self.u_previous = u.copy() #The current state become the previous one
            u[2:-2] = u_next

class lax_wendroff: #4
    def __call__(self, u, cfl): u[2:-2] = u[2:-2] - 0.5*cfl*(u[3:-1]-u[1:-3]) + 0.5*cfl**2*(u[3:-1]-2 *u[2:-2]+u[1:-3])

class lax: # 5
    def __call__(self, u, cfl): u[2:-2] = 0.5*(u[3:-1]+u[1:-3]) - 0.5*cfl*(u[3:-1]-u[1:-3])

class hybrid0: #6
    def __call__(self, u, cfl):  u[2:-2] -= 0.5*cfl*(u[3:-1]-u[1:-3]) #Same as Forward Time-Centered Space

class hybrid1: #7
    A = None
    B = None
    def __call__(self, u, cfl): #A*u_next = B*u
        if (self.A is None): #A matrix is always the same so we can compute it only once
            self.A = np.eye(len(u)-4)
            self.B = np.zeros(len(u)-4)
            np.fill_diagonal(self.A[1:,:-1],-0.5*cfl) #Fill the lower diagonal
            np.fill_diagonal(self.A[:-1,1:],0.5*cfl) #Fill the upper diagonal
            # coupling for periodic boundary condition
            self.A[0,-1] = -0.5*cfl
            self.A[-1,0] = 0.5*cfl

        self.B = u[2:-2].copy()

        u[2:-2] = np.linalg.solve(self.A,self.B) #Solving the equation for all position exepting the border nodes

class crank_nicolson: #8
    A = None
    B = None
    def __call__(self, u, cfl): #A*u_next = B*u
        if (self.A is None): #A matrix is always the same so we can compute it only once
            self.A = np.eye(len(u)-4)
            self.B = np.zeros(len(u)-4)
            np.fill_diagonal(self.A[1:,:-1],-0.25*cfl) #Fill the lower diagonal
            np.fill_diagonal(self.A[:-1,1:],0.25*cfl) #Fill the lower diagonal
            self.A[0,-1] = -0.25*cfl
            self.A[-1,0] = 0.25*cfl

        self.B = u[2:-2] - 0.25*cfl*(u[3:-1]-u[1:-3])

        u[2:-2] = np.linalg.solve(self.A,self.B)

class own_algorithm: #9
    u_previous = None
    u_next = None
    i = 0 #Iteration counter
    def __call__(self, u, cfl):
        if self.u_previous is None: #Initalization
            self.u_previous = np.zeros((3,len(u))) #Store n, n-1, n-2
            self.u_next = np.zeros((2,len(u))) #Store n+1, n+2

        #Updating the arrays
        self.u_next[0] = self.u_next[1]
        self.u_previous[0] = u.copy()

        if (self.i == 0): #With neither n-1 nor n+1
            scheme = explicit_backward()
            scheme(u,cfl)
        elif (self.i == 1): #With n-1 but no n+1
            scheme = leap_frog()
            scheme.u_previous = self.u_previous[1]
            scheme(u,cfl)
        else:
            if (self.i == 2): #Creating the n+1
                self.u_next[0] = u.copy()
                scheme = leap_frog()
                scheme.u_previous = self.u_previous[1]
                scheme(self.u_next[0], cfl)
                self.u_next[1] = self.u_next[0].copy()

            #Creating the n+2
            scheme = leap_frog()
            scheme.u_previous = self.u_previous[0]
            scheme(self.u_next[1],cfl)

            #Computing u_n
            u[2:-2] = (1/8)*(self.u_next[1][2:-2]-self.u_previous[2][2:-2]) + self.u_next[0][2:-2] - (3/4)*cfl*(u[3:-1]-u[1:-3])

        #Updating the arrays
        self.u_previous[1] = self.u_previous[0]
        self.u_previous[2] = self.u_previous[1]
        self.i += 1
