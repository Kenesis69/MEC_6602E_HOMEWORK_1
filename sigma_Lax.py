import matplotlib.pyplot as plt
import numpy as np


for sigma in np.linspace(0,1.1,12):
    x = np.linspace(0,2*np.pi,100)
    y = (np.cos(x))**2 +  4*sigma**2*(np.sin(x))**2
    plt.plot(x,y)
    
plt.legend(["sigma = 0","sigma = 0.1","sigma = 0.2","sigma = 0.3","sigma = 0.4","sigma = 0.5","sigma = 0.6","sigma = 0.7","sigma = 0.8","sigma = 0.9","sigma = 1.0","sigma = 1.1"])
plt.xlabel("angle value in")
plt.ylabel("G value")    

plt.show()
plt.title("sigma stability in backward scheme")