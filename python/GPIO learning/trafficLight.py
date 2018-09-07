import RPi.GPIO as GPIO
im

GPIO.setmode(GPIO.BCM)
led = Led(Color.RED, 18, True)
time.sleep(0.5)
GPIO.cleanup()
