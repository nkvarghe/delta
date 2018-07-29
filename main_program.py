from tkinter import *
from kinematics import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
#import slush
#import move
import time

"""
This part will be used once the rasperrypi/slushengine is working

#initialize the board
SlushEngine = Slush.sBoard()

#Initialize motors and set the currents
#setCurrent arguments (current,current while holding, current accel,current decel)
motor1 = Slush.Motor(1)
motor1.resetDev()
motor1.setCurrent(10,10,10,10)

motor2 = Slush.Motor(2)
motor2.resetDev()
motor2.setCurrent(10,10,10,10)

motor3 = Slush.Motor(3)
motor3.resetDev()
motor3.setCurrent(10,10,10,10)
"""

#functions called to move delta 
def xPos():
    global x0
    x0 = x0 + 1
    #motorMove(inverse(x0,y0,z0))
    var1.set(x0)
    time.sleep(t)

def xNeg():
    global x0
    x0 = x0 - 1
    #motorMove(inverse(x0,y0,z0))
    var1.set(x0)
    time.sleep(t)

def yPos():
    global y0
    y0 = y0 + 1
    #motorMove(inverse(x0,y0,z0))
    var2.set(y0)
    time.sleep(t)

def yNeg():
    global y0
    y0 = y0 - 1
    #motorMove(inverse(x0,y0,z0))
    var2.set(y0)
    time.sleep(t)

def zPos():
    global z0
    z0 = z0 + 1
    #motorMove(inverse(x0,y0,z0))
    var3.set(z0)
    time.sleep(t)

def zNeg():
    global z0
    z0 = z0 - 1
    #motorMove(inverse(x0,y0,z0))
    var3.set(z0)
    time.sleep(t)

def home():
    global x0,y0,z0
    x0,y0,z0 = 0,0,-50
    #motorMove(inverse(x0,y0,z0))
    var1.set(x0)
    var2.set(y0)
    var3.set(z0)
    time.sleep(t)

def userInput():
    global x0,y0,z0
    x0 = int(x.get())
    y0 = int(y.get())
    z0 = int(z.get())
    #motorMove(inverse(x0,y0,z0))
    var1.set(x0)
    var2.set(y0)
    var3.set(z0)

def moveScale():
    global x0,y0,z0
    x0 = var1.get()
    y0 = var2.get()
    z0 = var3.get()
    #motorMove(inverse(x0,y0,z0))

def showOutput():
    global x0,y0,z0
    angles = inverse(x0,y0,z0)
    OutputX.config(text=x0)
    OutputY.config(text=y0)
    OutputZ.config(text=z0)
    OutputAngle1.config(text=angles[1])
    OutputAngle2.config(text=angles[2])
    OutputAngle3.config(text=angles[3])

def plot_3D():
	global x0,y0,z0
	fig = plot.figure()
	axes = fig.add_subplot(111, projection='3d')
	axes.scatter(x0,y0,z0,c='r',marker='o')
	axes.set_xlabel('x axis')
	axes.set_ylabel('y axis')
	axes.set_zlabel('z axis')
	plot.show()

#main window
root = Tk()
root.geometry('1000x600')
root.title('My Delta')

#Home coordinates and time constant
x0 = 0
y0 = 0
z0 = -50
t = 0
initialAngles = inverse(x0,y0,z0)

#Buttons to move by increments
x_pos = Button(root, text = "x-pos", fg = "red", command = xPos).place(x=100,y=100)
x_neg = Button(root, text = "x-neg", fg = "red", command = xNeg).place(x=150,y=100)
y_pos = Button(root, text = "y-pos", fg = "red", command = yPos).place(x=100,y=150)
y_neg = Button(root, text = "y-neg", fg = "red", command = yNeg).place(x=150,y=150)
z_pos = Button(root, text = "z-pos", fg = "red", command = zPos).place(x=100,y=200)
z_neg = Button(root, text = "z-neg", fg = "red", command = zNeg).place(x=150,y=200)
home = Button(root, text = "Home", fg = "red", command = home).place(x=125,y=50)

#Entry boxes for user specified coordinates
x = StringVar()
y = StringVar()
z = StringVar()
x_text = Entry(root, textvariable = x).place(x=300,y=100)
y_text = Entry(root, textvariable = y).place(x=300,y=150)
z_text = Entry(root, textvariable = z).place(x=300,y=200)
labelX = Label(root,text = 'X-coord').place(x=300,y=70)
labelY = Label(root,text = 'Y-coord').place(x=300,y=120)
labelZ = Label(root,text = 'Z-coord').place(x=300,y=170)
coord = Button(root, text = "MOVE!", fg = "black", bg = "red", command = userInput).place(x=350,y=50)

#Scales for greater degree of movement
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
slider1 = Scale(root,orient = HORIZONTAL,length = 300,width = 10,tickinterval = 10,label = 'X-scale',variable = var1).place(x=500,y=70)
slider2 = Scale(root,orient = HORIZONTAL,length = 300,width = 10,tickinterval = 10,label = 'Y-scale',variable = var2).place(x=500,y=120)
slider3 = Scale(root,orient = HORIZONTAL,length = 300,width = 10,tickinterval = 10,from_ = -50,to = 0,label = 'Z-scale',variable = var3).place(x=500,y=170)
scale = Button(root, text = "MOVE!", fg = "red", bg = "black", command = moveScale).place(x=550,y=50)

#Plot coordinates onto 3D grid
Plot = Button(root, text = "Plot", fg = "Black", bg = "Green", command = plot_3D). pack()

#Display coordinates and angles
OutputBox = LabelFrame(root,text = "OutputBox")
OutputBox.pack(side = BOTTOM)
displayOutput = Button(OutputBox, text = "Output", fg = "Black", bg = "Blue", command = showOutput).pack()
OutputX = Label(OutputBox,text = x0)
OutputX.pack()
OutputY = Label(OutputBox,text = y0)
OutputY.pack()
OutputZ = Label(OutputBox,text = z0)
OutputZ.pack()
OutputAngle1 = Label(OutputBox,text = initialAngles[1])
OutputAngle1.pack()
OutputAngle2 = Label(OutputBox,text = initialAngles[2])
OutputAngle2.pack()
OutputAngle3 = Label(OutputBox,text = initialAngles[3])
OutputAngle3.pack()

root.mainloop()
