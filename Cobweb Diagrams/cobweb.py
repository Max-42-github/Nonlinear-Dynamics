# Cobweb plot
import numpy as np
import matplotlib.pyplot as plt


def sin(x):

	return np.sin(x)

def str_line(x):

	return x

def error_cal(r, r_cob):

	diff = abs(r-r_cob)
	return (diff/r)*100


# Constants
x_end = 1.6
x_0 = 1.5
iter_num = 40

x_arr = np.linspace(0,x_end,100)

y_arr_1 = sin(x_arr)
y_arr_2 = str_line(x_arr)


x_cob = [x_0]
y_cob = [0]

for i in range(iter_num):

	if i%2 == 0:
		y = sin(x_cob[i])
		x = x_cob[i]

		x_cob.append(x)
		y_cob.append(y)

	else :
		x = str_line(y_cob[i])
		y = y_cob[i]

		x_cob.append(x)
		y_cob.append(y)


fig_1 = plt.figure(figsize = (7,7))

plt.grid()
plt.title(r'cobweb diagram for sine curve $f(x) = sin(x)$')
plt.xlabel(r'$x \rightarrow$')
plt.ylabel(r'$f(x) \rightarrow$')

plt.plot(x_cob,y_cob, linewidth = 1)

plt.plot(x_arr, y_arr_1, label = f'iter no. = {iter_num}')
plt.plot(x_arr, y_arr_2, linestyle = '--')

plt.legend()

plt.show()






