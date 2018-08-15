import Slush

#trying to put it all in a class
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
    def home(self):
        while (self.name.isBusy()):
            continue
        self.name.goUntilPress(0,1,1000)

        while (self.name.isBusy()):
            continue
        self.name.setAsHome()

"""
