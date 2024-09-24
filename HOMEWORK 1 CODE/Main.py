## Module imports
import numpy as np
import matplotlib.pyplot as plt
import sys

## File imports
import Classes
import Function

##Scheme numbers
#0 - Explicit Backward
#1 - Explicit Forward
#2 - Forward Time-Centered Space
#3 - Leap-Frog
#4 - Lax-Wendroff
#5 - Lax
#6 - Hybrid Explicit-Implicit with θ = 0
#7 - Hybrid Explicit-Implicit with θ = 1
#8 - Crank-Nicolson (Hybrid with θ = 0.5)
#9 - Our own scheme

## Computation
#Parameters
N_scheme = 0 #Discretization scheme choice
CFL_range = [0.25, 0.5, 0.75, 1]  #CFL values
N = 400 #Number of discretization points

plt.figure()
#Computation with the discretization scheme we have chosen
Function.compute(N_scheme,CFL_range,N,0)

#Computation for the exact solution (the Explicit Backward give us the exact solution for CFL = 1)
N_scheme = 0 #Explicit Backward
CFL_range = [1]
Function.compute(N_scheme,CFL_range,N,1)

#Plotting parameters
plt.xlabel('Distance (m)')
plt.ylabel('Wave Speed (m/s)')
plt.legend()
plt.title('Results')
plt.show()