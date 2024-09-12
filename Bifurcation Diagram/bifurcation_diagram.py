#Bifurcation plot

import numpy as np 
import matplotlib.pyplot as plt 


# Parameters : 
r_arr = np.linspace(0,4,1000) 
x = 0.3
iter_num = 200

x_arr = np.linspace(0,1,100)

def logistic(r,x):
	return r*x*(1-x)


r_lst = []
x_lst = []

for r in r_arr:
	x = 0.3
	for i in range(iter_num):
		x = logistic(r,x)
		if (iter_num-i) <= 17 : 
			r_lst.append(r)
			x_lst.append(x)



fig = plt.figure(figsize = (13,6.5))

#plt.grid()
plt.title(fr'Bifurcation Diagram',size = 14)
plt.ylabel(r'$x^{*} \rightarrow$',size = 14)
plt.xlabel(r'$r \rightarrow$',size = 14)


plt.scatter(r_lst,x_lst,c = 'black',s = 0.1)
plt.show()