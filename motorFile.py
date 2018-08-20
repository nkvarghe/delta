import Slush

class motorControl():

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.motor = Slush.Motor(self.number)

    def motorMove(self,angle):
        currentSteps = angle/1.8
        self.motor.goTo(int(currentSteps))
        print([self.name,round(currentSteps,2)])
        
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