import numpy as np  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
  
fig = plt.figure()  
ax = Axes3D(fig)  

delta_period = [-1.39712903, 0.41098659, -1.61130804, -0.9263556, 0.04685894, -0.96037668, -2.29736527, 0.16654348, -2.89203067, 0.40735996]
delta_dms = [1.00066231, 1.08228967, 2.61797073, 2.88499405, 2.84737918, 1.66498518, 1.4450151, 1.53401038, 2.86850503, 1.71644053]
X =sorted(delta_period)
Y =sorted(delta_dms)

X, Y = np.meshgrid(X, Y) 
Z=np.zeros((len(X),len(Y)))
Z_temp = [-2.10456621, -2.67077683, -3.94197382, -2.80813515, -3.57714363, -2.38466996,-3.13469967, -3.61483956,-2.51853357, -3.28569297]
Z_temp = sorted(Z_temp)
print Z_temp
for i in range(len(X)):
    for j in range(len(Y)):
        Z[i,j] = Z_temp[i]
print X.shape
print Z.shape

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)  
#ax.plot_wireframe(X, Y, Z,marker = 'o')
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)  
#ax.set_zlim(-2,2)  
  
# savefig('../figures/plot3d_ex.png',dpi=48)  
plt.show()  

