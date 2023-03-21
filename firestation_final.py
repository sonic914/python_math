import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

nx=18; ny=25
for j in range(ny+1):
    plt.plot([0,nx], [j,j], color='k')
for i in range(nx+1):
    plt.plot([i,i], [0,ny], color="k")

NoH = 50
plt.show()