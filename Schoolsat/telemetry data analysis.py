import pandas as pd

# Example telemetry data (temperature and pressure)
data = {
    "Time": ["2023-03-26 00:00", "2023-03-26 01:00", "2023-03-26 02:00"],
    "Temperature (C)": [22, 21.5, 21],
    "Pressure (Pa)": [101325, 101300, 101280]
}

df = pd.DataFrame(data)

# Convert time to datetime
df["Time"] = pd.to_datetime(df["Time"])

# Analyze data (basic statistics)
print(df.describe())

# Plot the data
df.plot(x="Time", y=["Temperature (C)", "Pressure (Pa)"], kind="line")
plt.title("Telemetry Data: Temperature & Pressure Over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
