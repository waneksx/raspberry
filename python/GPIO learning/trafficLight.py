import RPi.GPIO as GPIO
from led import Led, Color
import time

class TrafficLight:
    def startWork(self):
        redLed = self.leds[0]
        yellowLed = self.leds[1]
        greenLed = self.leds[2]

        redLed.switch(True)
        time.sleep(3)
        redLed.blink(0.4, 3)
        redLed.switch(False)
        yellowLed.switch(True)
        time.sleep(2)
        yellowLed.switch(False)
        greenLed.switch(True)
        time.sleep(2)
        greenLed.switch(False)
        
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