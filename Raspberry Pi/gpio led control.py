import RPi.GPIO as GPIO
import time

# Set up the GPIO mode and pin
GPIO.setmode(GPIO.BCM)
led_pin = 18  # GPIO pin connected to the LED

# Set up the LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

def blink_led():
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait for 1 second
        GPIO.output(led_pin, GPIO.LOW)   # Turn LED off
        time.sleep(1)

blink_led()
