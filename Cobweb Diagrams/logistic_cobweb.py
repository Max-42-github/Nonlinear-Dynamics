# Cobweb plot of logistics function : 
import numpy as np 
import matplotlib.pyplot as plt 


# Parameters : 
r = 4 
x0 = 0.2
iter_num = 25

x_arr = np.linspace(0,1,100)

def logistic(r,x):
	return r*x*(1-x)

def straight(x):
	return x

def cobweb(x0,iter_num):
	cobweb_x = [x0]
	cobweb_y = [0]
	for i in range(iter_num):
		if i%2 == 0:
			x = cobweb_x[i]
			y = logistic(r,x)
			cobweb_x.append(x)
			cobweb_y.append(y)
		else:
			y = cobweb_y[i]
			x = straight(y)
			cobweb_x.append(x)
			cobweb_y.append(y)

	return (cobweb_x,cobweb_y)


cobweb_array = cobweb(x0,iter_num)

y_arr = logistic(r,x_arr)
x_cob = cobweb_array[0]
y_cob = cobweb_array[1]
y_str = straight(x_arr)


fig = plt.figure(figsize = (6.5,6.5))

plt.grid()
plt.title(fr'Logistic Map $y = rx_n(1-x_n)$ for [r = {r} and $x_0$ = {x0}]',size = 14)
plt.xlabel(r'$x_n \rightarrow$',size = 14)
plt.ylabel(r'$x_{n+1} \rightarrow$',size = 14)


plt.plot(x_arr,y_arr,c = 'red')
plt.plot(x_arr,y_str,'--',c = 'black')
plt.plot(x_cob,y_cob,c = 'blue')

plt.show()




