# Solving and plotting Rossler Attractor
from scipy.integrate import odeint
import numpy as np 
import matplotlib.pyplot as plt

def rossler(grid,t,a,b,c):
	x,y,z = grid
	dxdt = -y-z
	dydt = x + (a*y)
	dzdt = b + (z*(x-c))

	return([dxdt,dydt,dzdt])


t_arr = np.linspace(0,300,15000)


# Parameters
a = 0.1
b = 0.1
c = 14

# Initial Conditons
x0 = 1 
y0 = -1
z0 = 1

x1 = 2
y1 = -2
z1 = 2

initial_cond_1 = [x0,y0,z0]
initial_cond_2 = [x1,y1,z1]


solution_1 = odeint(rossler, initial_cond_1, t_arr, args = (a,b,c))
solution_2 = odeint(rossler, initial_cond_2, t_arr, args = (a,b,c))

# Setting up 3D axes and plotting the phase plot

fig = plt.figure(facecolor = 'k', figsize = (9,7))  # facecolor is bg color
ax = fig.add_subplot(111,projection = '3d')
ax.set_facecolor('k')		# color of the plotting area.

# To display the choosen parameter in legend section
label_string_1 = 'x0 = 1, y0 = -1, z0 = 1'
label_string_2 = 'x0 = 2, y0 = -2, z0 = 2'

ax.plot(solution_1[:,0],solution_1[:,1],solution_1[:,2], c = 'cyan', linewidth = 0.3, label = label_string_1)
ax.plot(solution_2[:,0],solution_2[:,1],solution_2[:,2], c = 'yellow', linewidth = 0.3, label = label_string_2)

# Typesetting the system eqautions
title_string = 'Rossler Attractor \n'+ r'$\frac{dx}{dt} = -y-z$' + '\t' + '\t' + r'$\frac{dy}{dt} = x + ay$' + '\t' + r'$\frac{dz}{dt} = b + z(x-c)$' + '\n' + '[a = 0.1, b = 0.1, c = 14]' 

ax.set_title(title_string, fontsize = 10, c = 'white')
ax.legend(fontsize = 10, labelcolor = 'white', frameon = False)

ax.set_axis_off()		# Turns off the axis

plt.show()