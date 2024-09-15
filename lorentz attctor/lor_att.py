import numpy as np
import matplotlib.pyplot as plt


def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])


dt = 0.01
num_steps = 10000

par_lst = [1.,4.,9.] 

for i in range(len(par_lst)):
   
   par_2 = par_lst[i]

   xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
   
   #xyzs[0] = (0., 1., 1.05)  # Set initial values
   
   xyzs[0] = (0., par_2, 1.05)  # Set initial values
   
   # Step through "time", calculating the partial derivatives at the current point
   # and using them to estimate the next point
   for i in range(num_steps):
       xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

   # Plot
   width = 1366
   height = 768
   dpi = 100

   fig = plt.figure(facecolor = 'k',figsize = (width/dpi, height/dpi))
   ax = fig.gca(projection = '3d')
   ax.set_facecolor('k')

   ax.plot(*xyzs.T, lw=0.5, c = 'y')
   #ax.set_xlabel("X Axis")
   #ax.set_ylabel("Y Axis")
   #ax.set_zlabel("Z Axis")
   #ax.set_title("Lorenz Attractor")

   ax.set_axis_off()

   '''
   for i in range(len(xyzs)):
      print(xyzs[i][0],xyzs[i][1],xyzs[i][2])
      
    '''  
plt.savefig('lorenz.png',dpi=dpi)
plt.show()