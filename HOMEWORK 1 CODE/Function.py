## Imports
import numpy as np
import matplotlib.pyplot as plt
import sys
import Classes

schemes = [Classes.explicit_backward, Classes.explicit_forward, Classes.forwardT_centeredS, Classes.leap_frog, Classes.lax_wendroff, Classes.lax, Classes.hybrid0, Classes.hybrid1, Classes.crank_nicolson, Classes.own_algorithm]

##Function
def compute(N_scheme,CFL_range,N,Exact_sol):
    #Global modeling parameters
    x = np.linspace(0,5,N)
    dx = 5/(N-1) #-1 because N is the number of nodes, not of cells
    c = 10
    t_end = 1.75/c #The time at which the wave is at x=2.5

    for cfl in CFL_range: #For each CFL value
        scheme = schemes[N_scheme]()

        t = 0 #Reset the time
        dt = cfl*dx/c #Determine the new dt with the new value of CFL
        u = np.zeros(N + 4) #Initalize u and put 4 nodes to manage the border

        #Inital state of the wave
        u[int(1.0/dx)+3:] = 0.0 #Before the wave
        u[int(0.5/dx)+3:int(1.0/dx)+3] = 1.0 #On the wave
        u[:int(0.5/dx)+3] = 0.0 #After the wave

        while t < t_end: #Calculating the propagation of the wave at each t
            #Computation at time t
            scheme(u, cfl)

            #Border nodes
            u[0] = u[-4]
            u[1] = u[-3]
            u[-2] = u[2]
            u[-1] = u[3]

            #Moving forward in time
            t += dt

        #Plot the final iteration
        if Exact_sol == 1:
            plt.plot(x, u[2:-2], '--y', label=f'Exact solution')
        else:
            plt.plot(x, u[2:-2], label=f'CFL = {cfl}')