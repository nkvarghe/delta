import Slush

class motorControl():

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.motor = Slush.Motor(self.number)

    def motorMove(self,angle):
        angleToSteps = angle/1.8
        self.motor.move(int(angleToSteps))
        #print(self.name + '= ' + str(angleToSteps)) 

    def setMotorSpeed(self,speed):
        if speed == '':
            speed = '0'
        self.speed = int(speed)
        self.motor.setMaxSpeed(speed)
        #print(speed)
        
"""
    def goHome(self):
        while (self.motor.isBusy()):
            continue
        self.motor.goUntilPress(0,1,1000)
        while (self.motor.isBusy()):
            continue
        self.motor.setAsHome()
"""
