import pandas as pd
import matplotlib.pyplot as plt
from config import CSV_FILE

def plot_rssi():
    df = pd.read_csv(CSV_FILE, names=['timestamp', 'sender', 'rssi', 'message'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    plt.figure(figsize=(10,5))
    plt.plot(df['timestamp'], df['rssi'], marker='o')
    plt.xlabel("Time")
    plt.ylabel("RSSI (dBm)")
    plt.title("LoRa Signal Strength Over Time")
    plt.grid(True)
    plt.savefig("data/signal_plot.png")
    plt.show()
