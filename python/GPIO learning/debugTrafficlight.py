import ptvsd
import RPi.GPIO as GPIO
import trafficLight
from led import Led, Color

ptvsd.enable_attach("my_secret", address = ('0.0.0.0', 3000))

#Enable the below line of code only if you want the application to wait untill the debugger has attached to it
ptvsd.wait_for_attach()

GPIO.setmode(GPIO.BCM)
redLed = Led(Color.RED, 18, False)
yellowLed = Led(Color.YELLOW, 23, False)
greenLed = Led(Color.GREEN, 24, False)
 
trafficLightLeds = list()
trafficLightLeds.append(redLed)
trafficLightLeds.append(yellowLed)
trafficLightLeds.append(greenLed)

trafficLight = TrafficLight(trafficLightLeds, 1)