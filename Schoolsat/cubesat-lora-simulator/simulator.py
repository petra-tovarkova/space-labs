import numpy as np
import matplotlib.pyplot as plt
from config import SAT_HEIGHT, TX_POWER, FREQ, RX_SENSITIVITY, ANT_GAIN_TX, ANT_GAIN_RX
from utils import free_space_path_loss, received_power

def simulate_orbit():
    # jednoduchá kruhová dráha s 100 body
    angles = np.linspace(0, 2*np.pi, 100)
    distance = SAT_HEIGHT / np.cos(angles)  # aproximace vzdálenosti k pozemní stanici
    return distance

def run_simulation():
    distance = simulate_orbit()
    tx_power_dbm = 10 * np.log10(TX_POWER * 1000)  # W -> dBm
    rx_power = []

    for d in distance:
        path_loss = free_space_path_loss(d, FREQ)
        rx = received_power(tx_power_dbm, path_loss, ANT_GAIN_TX, ANT_GAIN_RX)
        rx_power.append(rx)

    rx_power = np.array(rx_power)
    plt.plot(rx_power)
    plt.axhline(RX_SENSITIVITY, color='r', linestyle='--', label='Receiver Sensitivity')
    plt.title("LoRa Received Power Over Orbit")
    plt.xlabel("Orbit Position")
    plt.ylabel("Received Power (dBm)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_simulation()
