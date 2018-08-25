#This Class has functions that utilizes the Slush functions needed to control the delta robot's motors

import Slush

class motorControl():

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.motor = Slush.Motor(self.number)
    
    def motorMove(self,angle):
        currentSteps = angle/1.8
        self.motor.goTo(int(currentSteps))
        
    def setMotorSpeed(self,speed):
        if speed == '':
            speed = '0'
        self.speed = int(speed)
        self.motor.setMaxSpeed(speed)

    def goHome(self):
        while (self.motor.isBusy()):
            continue
        self.motor.goUntilPress(0,1,1000)
        while (self.motor.isBusy()):
            continue
        self.motor.setAsHome()
