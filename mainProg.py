""" This program contains the bulk of the code base. 
It makes use of the tkinter library for UI and calls the kinematics,slush and motorFile modules
for the sole purpose of moving the delta robot from the UI."""

from tkinter import *
from kinematics import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import Slush
import motorFile
import time

#Initialize the Board
SlushEngine = Slush.sBoard()

#File for coordinates
COORDINATES_FILE = 'points.txt'

#Create motor objects from motorContol class to access Slush functions
motor1 = motorFile.motorControl('Motor1',1)
motor2 = motorFile.motorControl('Motor2',2)
motor3 = motorFile.motorControl('Motor3',3)

motors = [motor1,motor2,motor3]

#Opens and writes coordinates to file
def save_coordinates(x, y, z):
    coord_file = open(COORDINATES_FILE, 'a+')
    coord_file.write('{},{},{}\n'.format(x, y, z))
    coord_file.close()

#Moves delta by 1mm in funcName direction
def xPos():
    global x0,y0,z0
    x0 = x0 + 1
    for index, motor in enumerate(motors, start=1):
        motor.motorMove(inverse(x0, y0, z0)[index])
    save_coordinates(x0, y0, z0)
    var1.set(x0)
    time.sleep(t)

def xNeg():
    global x0,y0,z0
    x0 = x0 - 1
    for index, motor in enumerate(motors, start=1):
        motor.motorMove(inverse(x0, y0, z0)[index])
    save_coordinates(x0, y0, z0)
    var1.set(x0)
    time.sleep(t)

def yPos():
    global x0,y0,z0
    y0 = y0 + 1
    for index, motor in enumerate(motors, start=1):
        motor.motorMove(inverse(x0, y0, z0)[index])
    save_coordinates(x0, y0, z0)
    var2.set(y0)
    time.sleep(t)

def yNeg():
    global x0,y0,z0
    y0 = y0 - 1
    for index, motor in enumerate(motors, start=1):
        motor.motorMove(inverse(x0, y0, z0)[index])
    save_coordinates(x0, y0, z0)
    var2.set(y0)
    time.sleep(t)

def zPos():
    global x0,y0,z0
    z0 = z0 + 1
    for index, motor in enumerate(motors, start=1):
        motor.motorMove(inverse(x0, y0, z0)[index])
    save_coordinates(x0, y0, z0)
    var3.set(z0)
    time.sleep(t)

def zNeg():
    global x0,y0,z0
    z0 = z0 - 1
    for index, motor in enumerate(motors, start=1):
        motor.motorMove(inverse(x0, y0, z0)[index])
    save_coordinates(x0, y0, z0)
    var3.set(z0)
    time.sleep(t)

#delta moves according to the points on the saved file
def moveFromFile():
    X_list,Y_list,Z_list = readFile()[0], readFile()[1], readFile()[2]
    for i in range(len(readFile()[0])):
        x,y,z = X_list[i],Y_list[i],Z_list[i]
        print(x,y,z)
        for index, motor in enumerate(motors, start=1):
            #motor.motorMove(inverse(x0, y0, z0)[index])
            print([motor.name,inverse(x,y,z)[index]])

#Homes each motor of it's limit switch
def home1():
    for motor in motors:
        motor.goHome()

def home():
    global x0,y0,z0
    x0,y0,z0 = 0,0,-50
    for index, motor in enumerate(motors, start=1):
        motor.motorMove(inverse(x0, y0, z0)[index])
    save_coordinates(x0, y0, z0)
    var1.set(x0)
    var2.set(y0)
    var3.set(z0)
    time.sleep(t)

#Scales for greater degree of movement
def moveScale():
    global x0,y0,z0
    x0 = var1.get()
    y0 = var2.get()
    z0 = var3.get()
    for index, motor in enumerate(motors, start=1):
        motor.motorMove(inverse(x0, y0, z0)[index])
    save_coordinates(x0, y0, z0)

#Sets delta speed
def setSpeed():
    for motor in motors:
        motor.setMotorSpeed(speed.get())

#Displays coordinates and angles
def showOutput():
    global x0,y0,z0
    angles = inverse(x0,y0,z0)
    OutputX.config(text=x0)
    OutputY.config(text=y0)
    OutputZ.config(text=z0)
    OutputAngle1.config(text=round(angles[1],2))
    OutputAngle2.config(text=round(angles[2],2))
    OutputAngle3.config(text=round(angles[3],2))

#Reads the points file
def readFile():
    coord_file = open(COORDINATES_FILE, 'r')
    data = coord_file.read()
    coord_file.close()
    lines = data.split('\n')
    X_list = []
    Y_list = []
    Z_list = []
    for line in lines:
        if len(line) > 1:
            X, Y, Z = line.split(',')
            X_list.append(int(X))
            Y_list.append(int(Y))
            Z_list.append(int(Z))
            
    return [X_list,Y_list,Z_list]

#Plots coordinates onto a 3D grid
def plotCoordinates():
    fig = plot.figure()
    axes = fig.add_subplot(111, projection='3d')
    axes.scatter(readFile()[0],readFile()[1],readFile()[2],c='r',marker='o')
    axes.set_xlabel('x axis')
    axes.set_ylabel('y axis')
    axes.set_zlabel('z axis')
    plot.show()

#main window
root = Tk()
root.geometry('300x705+400+15')
root.title('My Delta')

#Home coordinates and time constant
x0 = 0
y0 = 0
z0 = -50
t = 0
initialAngles = inverse(x0,y0,z0)

#Home the robot
HomeButton = Button(root, text = "HOME", fg = "Black", bg = "Green", font = ('Times',14,'bold'), command = home).pack(fill=X)

#Set the speed
speed=StringVar()
SpeedFrame = LabelFrame(root)
SpeedFrame.pack()
speedLabel = Label(SpeedFrame, text = "Enter Speed").grid(row=0,column=0)
speedEntry = Entry(SpeedFrame, textvariable = speed).grid(row=0,column=1)
speedButtonFrame = LabelFrame(root).pack(fill=X)
speedButton = Button(speedButtonFrame, text = "SET SPEED", fg = 'black', bg = 'red', font = ('Times',14,'bold'), command = setSpeed).pack(fill=X)

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

#Configure Scales
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
ScaleFrame = LabelFrame(root,text = "Sliders")
ScaleFrame.pack()
slider1 = Scale(ScaleFrame,orient = VERTICAL,length = 150,width = 40,from_= -40,to = 40,label = 'X',variable = var1).grid(row=0,column=0)
slider2 = Scale(ScaleFrame,orient = VERTICAL,length = 150,width = 40,from_= -40,to = 40,label = 'Y',variable = var2).grid(row=0,column=1)
slider3 = Scale(ScaleFrame,orient = VERTICAL,length = 150,width = 40,from_ = -50,to = -40,label = 'Z',variable = var3).grid(row=0,column=2)
var3.set(-50)
ScaleButtonFrame = LabelFrame(root).pack(fill=X)
scale = Button(ScaleButtonFrame, text = "MOVE TO SCALE POSITION", fg = "red", bg = "black", font = ('Times',14,'bold'), command = moveScale).pack(fill=X)

#Move from file button
moveFile = Button(root, text = "MOVE FROM FILE", fg = "Black", bg = "magenta", font = ('Times',14,'bold'), command = moveFromFile).pack(fill=X)

#Configuration of Output box
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
displayOutput = Button(OutputButtonFrame, text = "GET OUTPUT", fg = "Black", bg = "Cyan", font = ('Times',14,'bold'), command = showOutput).pack(fill=X)

#Plot button
Plot = Button(root, text = "PLOT", fg = "Black", bg = "Yellow", font = ('Times',14,'bold'), command = plotCoordinates).pack(fill=X)

root.mainloop()