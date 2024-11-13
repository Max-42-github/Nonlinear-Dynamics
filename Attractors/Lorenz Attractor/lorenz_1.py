# Generating data for Lorentz Attractor and plotting.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz_data_gen(initial_cond):

	def lorenz(x,y,z,dt):

		'''
			evaluates the lorenz equations
		'''
		
		# Parameters
		sigma = 10
		rho = 28
		beta = 8/3

		dx = sigma*(y-x) * dt
		dy = ((x*(rho-z)) - (y)) * dt
		dz = ((x*y) - (beta*z)) * dt

		return ([dx,dy,dz])

	# setting parameters : 

	'''
	For High res plot : 
	
	dt = 0.001
	iter_num = 5000

	'''

	dt = 0.001							# Time step 
	iter_num = 50000					# End time for calcualtion (total iterations)
	lorenz_arr = np.zeros((3,iter_num))

	lorenz_arr[0][0] = initial_cond[0]
	lorenz_arr[1][0] = initial_cond[1]
	lorenz_arr[2][0] = initial_cond[2]

	for i in range(iter_num-1):

		x = lorenz_arr[0][i]
		y = lorenz_arr[1][i]
		z = lorenz_arr[2][i]

		lorenz_step = lorenz(x,y,z,dt)

		# Iterating : lor_n+1 = lor_n + d(lor)

		lorenz_arr[0][i+1] = lorenz_arr[0][i] + lorenz_step[0]
		lorenz_arr[1][i+1] = lorenz_arr[1][i] + lorenz_step[1]
		lorenz_arr[2][i+1] = lorenz_arr[2][i] + lorenz_step[2]


	return lorenz_arr

# setting up to close initial point and evaluating them.

# Change to set initial points in the phase space
init_cond_1 = [0,0.1,0]
init_cond_2 = [0,0.11,0]
		
lorenz_data_1 = lorenz_data_gen(init_cond_1)
lorenz_data_2 = lorenz_data_gen(init_cond_2)



# Setting up 3D axes and plotting the phase plot

fig = plt.figure(facecolor = 'k', figsize = (8,7))  # facecolor is bg color
ax = fig.add_subplot(111,projection = '3d')
ax.set_facecolor('k')		# color of the plotting area.

# Typesetting the system eqautions
title_string = 'Lorentz Attractor \n'+ r'$\frac{dx}{dt} = \sigma(y-x)$' + '\t' + r'$\frac{dy}{dt} = x(\rho-z) - y$' + '\t' + r'$\frac{dz}{dt} = xy - \beta z$' + '\n' + r'$[\sigma = 10, \rho = 28, \beta = 8/3]$' 

ax.set_title(title_string, fontsize = 10, c = 'white')

# To display the choosen parameter in legend section
label_string_1 = 'x0 = 0, y0 = 0.1, z0 = 0'
label_string_2 = 'x0 = 0, y0 = 0.11, z0 = 0'

ax.plot(lorenz_data_1[0],lorenz_data_1[1],lorenz_data_1[2], c = 'cyan', linewidth = 0.5, label = label_string_1)
ax.plot(lorenz_data_2[0],lorenz_data_2[1],lorenz_data_2[2], c = 'yellow', linewidth = 0.5, label = label_string_2)
ax.legend(fontsize = 10, labelcolor = 'white', frameon = False)

ax.set_axis_off()		# Turns off the axis

plt.show()





