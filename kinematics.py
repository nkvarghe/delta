# Original code from
# http://forums.trossenrobotics.com/tutorials/introduction-129/delta-robot-kinematics-3276/
# License: MIT

import math

# Specific geometry for bitbeambot:
# http://flic.kr/p/cYaQah
e  =  26.0
f  =  69.0
re = 128.0
rf =  88.0

# Trigonometric constants
s      = 165*2
sqrt3  = math.sqrt(3.0)
pi     = 3.141592653
sin120 = sqrt3 / 2.0
cos120 = -0.5
tan60  = sqrt3
sin30  = 0.5
tan30  = 1.0 / sqrt3


# Inverse kinematics (x0, y0, z0) -> (theta1, theta2, theta3)
# Helper functions, calculates angle theta1 (for YZ-pane)
def angle_yz(x0, y0, z0, theta=None):
    y1 = -0.5*0.57735*f # f/2 * tg 30
    y0 -= 0.5*0.57735*e # shift center to edge
    # z = a + b*y
    a = (x0*x0 + y0*y0 + z0*z0 + rf*rf - re*re - y1*y1) / (2.0*z0)
    b = (y1-y0) / z0

    # discriminant
    d = -(a + b*y1)*(a + b*y1) + rf*(b*b*rf + rf)
    if d<0:
        return [1,0] # non-existing povar.  return error, theta

    yj = (y1 - a*b - math.sqrt(d)) / (b*b + 1) # choosing outer povar
    zj = a + b*yj
    theta = math.atan(-zj / (y1-yj)) * 180.0 / pi + (180.0 if yj>y1 else 0.0)
    return [0,theta] # return error, theta

def inverse(x0, y0, z0):
    theta1 = 0
    theta2 = 0
    theta3 = 0
    status = angle_yz(x0,y0,z0)

    if status[0] == 0:
        theta1 = status[1]
        status = angle_yz(x0*cos120 + y0*sin120, y0*cos120 - x0*sin120, z0, theta2)
        
    if status[0] == 0:
        theta2 = status[1]
        status = angle_yz(x0*cos120 - y0*sin120, y0*cos120 + x0*sin120, z0, theta3)
        
    theta3 = status[1]

    return [status[0],theta1,theta2,theta3]



