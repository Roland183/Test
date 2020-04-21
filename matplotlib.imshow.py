# -*- coding: utf-8 -*-
################################
# Neuronal Network
# R.J.Nickerl
# 22.02.2020
################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Make an array with ones in the shape of an 'X'
a = np.zeros([4,4])
print(a)
print()

a[1,1]=3
a[1,0]=1
a[2,1]=7
a[0,1]=3
a[0,0]=1
a[2,0]=7
print(a)


# Bilinear interpolation - this will look blurry
plt.imshow(a, interpolation='nearest')


# Bilinear interpolation - this will look blurry
plt.imshow(a, interpolation='bilinear', cmap=cm.Greys_r)


# Bilinear interpolation - this will look blurry
plt.imshow(a, interpolation='bilinear')
plt.show()
