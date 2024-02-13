import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return ((x-2)*(x-4)/((1- 2)*(1 -4)))*(-1) + ((x-1)*(x-4)/((2-1)*(2-4)))*(-2) + ((x-1)*(x-2)/((4-1)*(4-2)))*(2)
    
x = np.linspace(-0.5, 4.5, 1000)
y = f(x)
plt.scatter([1, 2, 4], [-1, -2, 2], color = "r")
plt.plot(x, y)
