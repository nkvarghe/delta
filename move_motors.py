import slush

def motorMove(angles):       
    motor1 = Slush.Motor(1)
    #motor1.resetDev()
    motor1.setCurrent(10,10,10,10)
    print('angle1 =' + str(int(angles[1])))
    angle1ToSteps = (angles[1]/1.8)
    print('steps =' + str(int(angle1ToSteps)))
    motor1.move(int(angle1ToSteps))

"""
#trying to put it all in a class
class motors():

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.name = Slush.Motor(self.number)
        self.name.resetDev()

    def setMotorCurrent(self,current):
        self.current = current
        self.name.setCurrent(current,current,current,current)

    def home(self):
        while (self.name.isBusy()):
            continue
        self.name.goUntilPress(0,1,1000)

        while (self.name.isBusy()):
            continue
        self.name.setAsHome()

    def motorMove(self,angles):
        self.angles = angles
        self.anglesToSteps = 
        if self.name == 'motor1':
            self.name.goTo(angleToSteps[1])
        if self.name == 'motor2':
            self.name.goTo(anglesToSteps[2])
        if self.name == 'motor3':
            self.name.goTo(anglesToSteps[3])

"""
