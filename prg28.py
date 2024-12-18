import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('download.png')
plt.imsave("download.png",img,cmap='gray',origin='lower')
imgplot=plt.imshow(img)
plt.show()
