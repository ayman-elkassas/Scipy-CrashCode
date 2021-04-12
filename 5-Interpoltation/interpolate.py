import numpy as np  
from scipy.interpolate import interp1d  
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 10)   
y = np.cos(x**2/3+4)

fun1 = interp1d(x, y,kind = 'linear')  
fun2 = interp1d(x, y, kind = 'cubic')

xnew = np.linspace(0, 4,30)  

plt.plot(x, y, 'o', xnew, fun1(xnew), '-', xnew, fun2(xnew), '--')  
plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')  
plt.show()