import RPi.GPIO as GPIO
import led
import time

class TrafficLight:
    def __init__(self, leds, period):
        GPIO.setmode(GPIO.BCM)
        print(leds, period)
        self.leds = leds
        self.period = period
        startWork()

    def startWork(self):
        for led in self.leds
            led.switch(True)
            time.sleep(self.period)
            led.switch(False)
            time.sleep(self.period)
        
redLed = Led(Color.RED, 18, False)
yellowLed = Led(Color.YELLOW, 23, False)
greenLed = Led(Color.GREEN, 24, False)
 
trafficLightLeds = list(redLed, yellowLed, greenLed)
trafficLight = TrafficLight(trafficLightLeds, 1)