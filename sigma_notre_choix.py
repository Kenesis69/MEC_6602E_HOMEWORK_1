import numpy as np 
import matplotlib.pyplot as plt

def f(x,C): 
    if x == 0:
        return np.inf
    else:
        return 1/8 * x**2 - x + x**-1 - 1/8 * x **-2 - C

def fp(x):
    if x == 0:
        return np.inf
    else: return 1/4*x - 1 + -x**-2 - 1/4 * x**-3

def newton_raphson(C,x0, tol = 1e-6, max_iter = 400):
    iteration = 0
    while iteration < max_iter:
        fx = f(x0,C)
        fpx = fp(x0)
        if fpx == 0:
            print("you are cooked bruv")
            return None
        
        x1 = x0 - fx/fpx
        if all(abs (x1 - x0)) < tol:
            return x1
    x0 = x1
    iteration += 1

    print ("ur cooked")




x = np.linspace(0,2*np.pi,30)
sigma_mat = np.linspace(0,3,30)
for sigma in sigma_mat:
    C = 2j/2*sigma*(2*np.sin(x))

    x0 = 1 + 0j
    sol = newton_raphson(C,x0, tol = 1e-6, max_iter = 100)
    print(abs(sol))
    plt.plot(x,abs(sol))

plt.xlabel('x')
plt.ylabel('|Solution|')
plt.title('Module des solutions en fonction de x pour différentes valeurs de σ')
plt.legend()
plt.show()
