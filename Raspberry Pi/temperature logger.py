import Adafruit_DHT
import time

# Set up the sensor
sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO pin where the sensor is connected

def log_temperature():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} - Temp: {temperature}°C  Humidity: {humidity}%")
            with open("temperature_log.txt", "a") as file:
                file.write(f"{timestamp} - Temp: {temperature}°C  Humidity: {humidity}%\n")
        time.sleep(60)  # Log every minute

log_temperature()
