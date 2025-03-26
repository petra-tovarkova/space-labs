import time
import RPi.GPIO as GPIO

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)
sensor_pin = 17  # GPIO pin connected to the sensor

# Set up the sensor pin as input
GPIO.setup(sensor_pin, GPIO.IN)

def log_sensor_data():
    with open("sensor_log.txt", "a") as file:
        while True:
            sensor_value = GPIO.input(sensor_pin)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}: {sensor_value}\n")
            time.sleep(1)  # Log every second

log_sensor_data()
