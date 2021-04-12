from scipy import misc  
from scipy import ndimage

face = misc.face()

blurred_image = ndimage.gaussian_filter(face, sigma=4)  
import matplotlib.pyplot as plt  
plt.imshow(blurred_image)  
plt.show()  