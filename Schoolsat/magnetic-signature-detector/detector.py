import pandas as pd
import matplotlib.pyplot as plt

# načtení simulovaných dat z magnetometru
data = pd.read_csv("magnetometer_readings.csv")
threshold = 0.05  # detekce změn větších než 0.05 gauss

# detekce náhlých změn v signálu
data['delta'] = data['field'].diff().abs()
events = data[data['delta'] > threshold]

plt.plot(data['time'], data['field'], label='Magnetometer Reading')
plt.scatter(events['time'], events['field'], color='r', label='Potential Object')
plt.xlabel("Time [s]")
plt.ylabel("Magnetic Field [Gauss]")
plt.title("Magnetic Signature Detection")
plt.legend()
plt.show()
