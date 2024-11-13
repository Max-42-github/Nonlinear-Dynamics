# Solving and plotting Van Der Pol Non Linear system
from scipy.integrate import odeint
import numpy as np 
import matplotlib.pyplot as plt 

def VanDerPol(grid,t,mu):
	x,y = grid
	dxdt = y
	dydt = (mu*(1-(x**2))*y)-x

	return ([dxdt,dydt])

# Setting up initial points and parameters

t_arr = np.arange(0,2000,0.08)

x0 = 0.4
y0 = 0.1 
initial_cond_1 = [x0,y0]

x1 = -0.4
y1 = -0.1
initial_cond_2 = [x1,y1]

mu = 0.3

solution_1 = odeint(VanDerPol, initial_cond_1, t_arr, args = (mu,))
solution_2 = odeint(VanDerPol, initial_cond_2, t_arr, args = (mu,))


fig = plt.figure(facecolor = 'k', figsize = (9,7))  # facecolor is bg color
ax = fig.add_subplot(111)
ax.set_facecolor('k')

# Typesetting the system eqautions
title_string = 'Rossler Attractor \n'+ r'$\frac{dx}{dt} = y$' + '\t' + r'$\frac{dy}{dt} = \mu(1-x^2)y - x$' + '\n' + r'[$\mu = 0.3$]' 

# To display the choosen parameter in legend section
label_string_1 = 'x0 = 0.4, y0 = 0.1'
label_string_2 = 'x0 = -0.4, y0 = -0.1'

plt.plot(solution_1[:,0],solution_1[:,1], c = 'cyan', linewidth = 0.3, label = label_string_1)
plt.plot(solution_2[:,0],solution_2[:,1], c = 'red', linewidth = 0.3, label = label_string_2)

ax.set_title(title_string, fontsize = 10, c = 'white')
plt.legend(fontsize = 10, labelcolor = 'white', frameon = False)

ax.set_axis_off()

plt.show()
