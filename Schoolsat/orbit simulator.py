import numpy as np
import matplotlib.pyplot as plt

# Parameters for the satellite (example values)
orbital_radius = 10000  # in km
orbital_speed = 7.12  # in km/s

# Time and number of steps
time = np.linspace(0, 2 * np.pi, 100)
x = orbital_radius * np.cos(time)
y = orbital_radius * np.sin(time)

# Plot the orbit
plt.figure(figsize=(6, 6))
plt.plot(x, y, label="Satellite Orbit")
plt.scatter(0, 0, color='red', label="Earth")
plt.title("Satellite Orbit Simulation")
plt.xlabel("X Position (km)")
plt.ylabel("Y Position (km)")
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
