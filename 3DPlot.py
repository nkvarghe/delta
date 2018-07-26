from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

fig = plot.figure()
axes = fig.add_subplot(111, projection='3d')

X = 1
Y = 2
Z = -30

axes.scatter(X,Y,Z,c='r',marker='o')

axes.set_xlabel('x axis')
axes.set_ylabel('y axis')
axes.set_zlabel('z axis')

plot.show()