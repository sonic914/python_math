import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

nx=18; ny=25
for j in range(ny+1):
    plt.plot([0,nx], [j,j], color='k')
for i in range(nx+1):
    plt.plot([i,i], [0,ny], color="k")

NoH = 50
x = np.random.randint(low=0, high=nx+1, size=(NoH, 1))
y = np.random.randint(low=0, high=ny+1, size=(NoH, 1))

plt.figure(1)
plt.plot(x, y, 'ro')

fire = np.zeros((nx+1, ny+1))
for i in range (nx+1):
    for j in range (ny+1):
        distance = 0
        for k in range(NoH):
            org = abs(x[k]-i) + abs(y[k]-j)
            distance += (org*org)
            #print (distance)
            #distance += abs(x[k]-i) + abs(y[k]-j)
            fire[i,j] = distance
s = (nx+ny)*(nx+ny) * NoH
for i in range(nx+1):
    for j in range(ny+1):
        if fire[i,j] < s:
            s = fire[i,j]
            mini = i
            minj = j
print('Minimum value of fire = ', s)
print('Index of min(fire) with axis row = ', mini)
print('Index of min(fire) with axis colum = ', minj)
plt.plot(mini, minj, 'bs')
plt.axis('image')
fig = plt.figure(2)
ax = fig.add_subplot(projection="3d")
x = np.linspace(0, nx, nx+1)
y = np.linspace(0, ny, ny+1)
X,Y = np.meshgrid(x, y)
ax.plot_wireframe(X,Y,fire.T)
ax.scatter(mini, minj, color='b')
plt.axis('tight')
plt.show() 