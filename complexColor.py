import prettyplotlib as ppl
# prettyplotlib imports
import matplotlib.pyplot as plt
import matplotlib as mpl
from prettyplotlib import brewer2mpl

import cmath


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import hsv_to_rgb

#limits of x y axis, step
X = np.arange(-5, 5, 0.125)
Y = np.arange(-5, 5, 0.125)
#display parameters
width=5
height=5
dpi=100
#define any complex function
def complex_function(z):
    return z**2

X, Y = np.meshgrid(X, Y)
Z = complex_function(X+1j*Y)

#every input complex number is a point, and every output complex number a color.
#color defined by rotation through hue, red is real positive
rotation=np.angle(Z) % (2. * np.pi)
rmin = np.min(rotation)
rmax = np.max(rotation)
rotation = rotation + rmin
hue= rotation / (rmax - rmin)
r = np.log2(1. + np.abs(Z))
saturation = (1. + np.abs(np.sin( 2*np.pi * r)))/2.
value = (1. + np.abs(np.cos( 2*np.pi * r)))/2.
rgb = hsv_to_rgb(np.dstack((hue,saturation,value)))
fig = plt.figure(figsize=(width, height), dpi=dpi)
plt.imshow(rgb)

plt.show()