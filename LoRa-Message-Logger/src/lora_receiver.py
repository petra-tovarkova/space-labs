from pyLoRa import LoRa
import csv
import datetime
from config import CSV_FILE
from logger import log_event

def receive_messages():
    lora = LoRa(frequency=868.0)
    while True:
        message = lora.receive()
        if message:
            timestamp = datetime.datetime.now()
            # Zápis do CSV
            with open(CSV_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, message.sender, message.rssi, message.text])
            # Zápis do logu
            log_event(f"Received message from {message.sender}: {message.text} | RSSI: {message.rssi}")
            print(f"[{timestamp}] Received: {message.text} from {message.sender} with RSSI {message.rssi}")
