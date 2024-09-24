import numpy as np
import matplotlib.pyplot as plt

#Question d
N = 12
S = np.linspace(0,1.1,N)

kdx = np.linspace(0,2*np.pi,100)

function_d = lambda s: 1-4*(s*np.sin(kdx/2))**2 + 4*(s*np.sin(kdx/2))**4 + (s*np.sin(kdx))**2

G = np.zeros((N,100))
for n in range(N):
    G[n][:] = function_d(S[n])
Question_d = plt.figure()
for n in range(N):
    if S[n]<2:
        plt.plot(kdx,G[n],label='S={}'.format(S[n]))
    else: break

plt.xlabel('kΔx')
plt.ylabel('|G|')
plt.title("|G| in fonction of sigma and kmx")
plt.legend()
plt.show()

#Question f for θ=1
N = 11
S = np.linspace(0,2,N)

kdx = np.linspace(np.pi,2*np.pi,100)

function_f = lambda s: np.abs( (1-1j*s*np.sin(kdx)) / (1+(s*np.sin(kdx))**2) )

G = np.zeros((N,100))
for n in range(N):
    G[n][:] = function_f(S[n])

Question_f1 = plt.figure()
for n in range(N):
    plt.plot(kdx,G[n],label='S={}'.format(S[n]))
   
plt.title("|G| in fonction of sigma and kmx for implicite scheme when theta = 0.5")
plt.xlabel('kΔx')
plt.ylabel('|G|')
plt.legend()
plt.show()

#Question f for θ=0.5
N = 10
S = np.linspace(0,1,N)

kdx = np.linspace(np.pi,2*np.pi,100)

function_f = lambda s: np.abs((1 - 1j*np.sin(kdx)*s - (np.sin(kdx)*s/2)**2) / (1 + (s*np.sin(kdx)/2)**2))

G = np.zeros((N,100))
for n in range(N):
    G[n][:] = function_f(S[n])

Question_f2 = plt.figure()
for n in range(N):
    if S[n]<2:
        plt.plot(kdx,G[n],label='S={}'.format(S[n]))
    else: break
plt.title("|G| in fonction of sigma and kmx for implicite scheme when theta = 1")
plt.xlabel('kΔx')
plt.ylabel('|G|')
plt.legend()
plt.show()