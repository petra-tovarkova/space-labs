from pyLoRa import LoRa
import time

def send_message(text, receiver_address=1):
    lora = LoRa(frequency=868.0)
    lora.send(text, receiver_address)
    print(f"Sent message to {receiver_address}: {text}")

if __name__ == "__main__":
    while True:
        send_message("Test message")
        time.sleep(5)
