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
"""
def userInput():
    global x0,y0,z0
    x0 = int(x.get())
    y0 = int(y.get())
    z0 = int(z.get())
    #motorMove(inverse(x0,y0,z0))
    var1.set(x0)
    var2.set(y0)
    var3.set(z0)
"""
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
    OutputAngle1.config(text=round(angles[1],2))
    OutputAngle2.config(text=round(angles[2],2))
    OutputAngle3.config(text=round(angles[3],2))

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
root.geometry('500x600+200+200')
root.title('My Delta')

#Home coordinates and time constant
x0 = 0
y0 = 0
z0 = -50
t = 0
initialAngles = inverse(x0,y0,z0)

#Buttons to move by increments
ButtonFrame = LabelFrame(root,text = "Buttons")
ButtonFrame.pack()
home = Button(ButtonFrame, text = "Home", fg = "red", command = home).grid(row=0,column=0)
x_pos = Button(ButtonFrame, text = "x-pos", fg = "red", command = xPos).grid(row=1,column=0)
x_neg = Button(ButtonFrame, text = "x-neg", fg = "red", command = xNeg).grid(row=1,column=1)
y_pos = Button(ButtonFrame, text = "y-pos", fg = "red", command = yPos).grid(row=2,column=0)
y_neg = Button(ButtonFrame, text = "y-neg", fg = "red", command = yNeg).grid(row=2,column=1)
z_pos = Button(ButtonFrame, text = "z-pos", fg = "red", command = zPos).grid(row=3,column=0)
z_neg = Button(ButtonFrame, text = "z-neg", fg = "red", command = zNeg).grid(row=3,column=1)
"""
#Entry boxes for user specified coordinates
x = StringVar()
y = StringVar()
z = StringVar()
EntryFrame = LabelFrame(root,text = "User Input")
EntryFrame.pack(fill=X)
coord = Button(EntryFrame, text = "MOVE!", fg = "black", bg = "red", command = userInput).pack()
labelX = Label(EntryFrame,text = 'X-coord').pack()
x_text = Entry(EntryFrame, textvariable = x).pack()
labelY = Label(EntryFrame,text = 'Y-coord').pack()
y_text = Entry(EntryFrame, textvariable = y).pack()
labelZ = Label(EntryFrame,text = 'Z-coord').pack()
z_text = Entry(EntryFrame, textvariable = z).pack()
"""
#Scales for greater degree of movement
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
ScaleFrame = LabelFrame(root,text = "Sliders")
ScaleFrame.pack()
slider1 = Scale(ScaleFrame,orient = VERTICAL,length = 150,width = 40,from_=0,to = 30,label = 'X-scale',variable = var1).grid(row=0,column=0)
slider2 = Scale(ScaleFrame,orient = VERTICAL,length = 150,width = 40,from_= 0,to = 30,label = 'Y-scale',variable = var2).grid(row=0,column=1)
slider3 = Scale(ScaleFrame,orient = VERTICAL,length = 150,width = 40,from_ = -50,to = -39,label = 'Z-scale',variable = var3).grid(row=0,column=2)
var3.set(-50)
ScaleButtonFrame = LabelFrame(root).pack(fill=X)
scale = Button(ScaleButtonFrame, text = "MOVE!", fg = "red", bg = "black", command = moveScale).pack(fill=X)

#Display coordinates and angles
OutputBox = LabelFrame(root,text = "OutputBox")
OutputBox.pack()
XLabel = Label(OutputBox,text = 'X :')
XLabel.grid(row=0,column=0)
OutputX = Label(OutputBox,text = x0)
OutputX.grid(row=0,column=1)
YLabel = Label(OutputBox,text = 'Y :')
YLabel.grid(row=1,column=0)
OutputY = Label(OutputBox,text = y0)
OutputY.grid(row=1,column=1)
ZLabel = Label(OutputBox,text = 'Z :')
ZLabel.grid(row=3,column=0)
OutputZ = Label(OutputBox,text = z0)
OutputZ.grid(row=3,column=1)
Angle1 = Label(OutputBox,text = 'Angle1 :')
Angle1.grid(row=4,column=0)
OutputAngle1 = Label(OutputBox,text = round(initialAngles[1],2))
OutputAngle1.grid(row=4,column=1)
Angle2 = Label(OutputBox,text = 'Angle2 :')
Angle2.grid(row=5,column=0)
OutputAngle2 = Label(OutputBox,text = round(initialAngles[2],2))
OutputAngle2.grid(row=5,column=1)
Angle3 = Label(OutputBox,text = 'Angle3 :')
Angle3.grid(row=6,column=0)
OutputAngle3 = Label(OutputBox,text = round(initialAngles[3],2))
OutputAngle3.grid(row=6,column=1)
OutputButtonFrame = LabelFrame(root).pack(fill=X)
displayOutput = Button(OutputButtonFrame, text = "Output", fg = "Black", bg = "Blue", command = showOutput).pack(fill=X)

#Plot coordinates onto 3D grid
Plot = Button(root, text = "Plot", fg = "Black", bg = "Green", command = plot_3D).pack(fill=X)

root.mainloop()