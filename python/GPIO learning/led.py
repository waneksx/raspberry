import RPi.GPIO as GPIO
import time
from enum import Enum

class Color(Enum):
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    
class Led:
    def __init__(self, color, pin, isSwitchedOn):
        self.color = color
        self.pin = pin
        self.isSwichedOn = isSwitchedOn
        GPIO.setup(18, GPIO.OUT)

    def switch(self, value):
        self.isSwichedOn = value
        GPIO.output(self.pin, value)

    def setupOutput(self):
        GPIO.setup(self.pin, GPIO.OUT)

#    def getInfo(self):
#        return 'Color: {}; Pin: {}; Is swithed {};'.format(self.color self.pin self.isSwichedOn)






# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)

# while (True):
#     GPIO.output(18, True)
#     time.sleep(0.5)
#     GPIO.output(18, False)
#     time.sleep(0.5)

# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(24, GPIO.OUT)

# GPIO.output(18, True)
# GPIO.output(23, True)
# GPIO.output(24, True)
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(24, GPIO.OUT)

# GPIO.output(18, True)
# GPIO.output(23, True)
# GPIO.output(24, True)


# GPIO.cleanup()

# GPIO.cleanup()


