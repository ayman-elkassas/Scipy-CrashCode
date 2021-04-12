import numpy as np

from scipy import linalg  
# We are trying to solve a linear algebra system which can be given as   
#         x + 3y +10z = 10  
#         2x + 12y + 7z = 18  
#         5x + 8y + 8z = 30  
# Creating input array  
a = np.array([[1, 3, 10], [2, 12, 7], [5, 8, 8]])  
# Solution Array  
b = np.array([[10], [18], [30]])  
# Solve the linear algebra  
x = linalg.solve(a, b)  
# Print results  
print(x)  
# Checking Results  
print("\n Checking results, Vectors must be zeros")  
print(a.dot(x) - b)