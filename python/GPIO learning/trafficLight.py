import RPi.GPIO as GPIO
from led import Led, Color
import time

class TrafficLight:
    def startWork(self):
        for led in self.leds:
            led.switch(True)
            time.sleep(self.period)
            led.switch(False)
            time.sleep(self.period)
        
        GPIO.cleanup()

    def __init__(self, leds, period):
        GPIO.setmode(GPIO.BCM)
        print(leds, period)
        self.leds = leds
        self.period = period
        self.startWork()    
        
GPIO.setmode(GPIO.BCM)
redLed = Led(Color.RED, 18, False)
yellowLed = Led(Color.YELLOW, 23, False)
greenLed = Led(Color.GREEN, 24, False)
 
trafficLightLeds = list()
trafficLightLeds.append(redLed)
trafficLightLeds.append(yellowLed)
trafficLightLeds.append(greenLed)

trafficLight = TrafficLight(trafficLightLeds, 1)