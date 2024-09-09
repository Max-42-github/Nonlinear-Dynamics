import numpy as np 
import matplotlib.pyplot as plt

def new_point(old_point,destination):
    x = old_point[0]
    y = old_point[1]

    if destination == 1 :
        X = A[0]
        Y = A[1]
        x_dis = abs(X+x)
        y_dis = abs(Y+y)
       
        x_new = x_dis/2
        y_new = y_dis/2
        new_point = (x_new,y_new)

        return new_point
    
    elif destination == 2 :
        X = B[0]
        Y = B[1]
        x_dis = abs(X+x)
        y_dis = abs(Y+y)

        x_new = x_dis/2
        y_new = y_dis/2
        new_point = (x_new,y_new)

        return new_point

    elif destination == 3 :
        X = C[0]
        Y = C[1]
        x_dis = abs(X+x)
        y_dis = abs(Y+y)

        x_new = x_dis/2
        y_new = y_dis/2
        new_point = (x_new,y_new)

        return new_point
    


A = (2,0)
B = (1,2)
C = (0,0)

# Random starting point
point = (0.5,0.5)
itter = 1000

#Ploting the initial cond.
plt.scatter([A[0], B[0], C[0] ,point[0]],[A[1], B[1], C[1] ,point[1]], c = 'b', s = 0.5)


for i in range(itter):
    rand_dir = np.random.randint(1,4)
    point = new_point(point,rand_dir)

    plt.scatter(point[0],point[1],c = 'b',s = 0.5)

plt.title('Sierpinski Triangle for i = 500')

plt.savefig('sierpinski triangle_1.png')




