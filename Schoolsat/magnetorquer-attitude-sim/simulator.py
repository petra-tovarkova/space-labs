import numpy as np
import matplotlib.pyplot as plt
from config import *

def pid_controller(error, kp, ki, kd, dt, integral, prev_error):
    integral += error * dt
    derivative = (error - prev_error) / dt
    output = kp*error + ki*integral + kd*derivative
    return output, integral

def simulate_attitude():
    angles = np.zeros(NUM_STEPS)
    angular_velocity = np.zeros(NUM_STEPS)
    integral = 0
    prev_error = 0

    for i in range(1, NUM_STEPS):
        error = TARGET_ANGLE - angles[i-1]
        torque, integral = pid_controller(error, KP, KI, KD, DT, integral, prev_error)
        angular_acc = torque / MOMENT_OF_INERTIA
        angular_velocity[i] = angular_velocity[i-1] + angular_acc*DT
        angles[i] = angles[i-1] + angular_velocity[i]*DT
        prev_error = error

    plt.plot(angles)
    plt.title("CubeSat Attitude Control Simulation")
    plt.xlabel("Time Step")
    plt.ylabel("Angle (rad)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_attitude()
