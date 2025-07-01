import scipy.stats as st
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x, y = np.mgrid[10:100:2, 10:100:2]

pos = np.empty(x.shape + (2,))
pos[:,:,0] = x
pos[:,:,1] = y

rv = multivariate_normal([50,50],[[100,0],[0,100]])
z = rv.pdf(pos)
print(z)

fig = plt.figure(dpi=100)
ax = Axes3D(fig)
ax.plot_wireframe(x, y, z)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x,y)")
ax.ticklabel_format(style='sci', axis='z', scilimits=(0,0))
