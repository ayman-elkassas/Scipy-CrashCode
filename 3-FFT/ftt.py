# importing the fft and inverse fft functions from fftpackage  
from scipy.fftpack import fft  
#Importing numpy  
import numpy as np  
#create an array with random n numbers  
x = np.array([4.0, 2.0, 1.0, -3.0, 1.5])  
#Applying the fft function  
y = fft(x)
print(y)