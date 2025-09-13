import matplotlib.pyplot as plt
import numpy as np

# Coefficients for quadratic model
a, b, c = 0.4, -2.5, 26

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c
print("=== INCREMENTAL MODEL ===")
increment_hours = 6  # increment every 6 hours
total_hours = 24
incremental_times = []
incremental_temps = []

for t in range(0, total_hours + 1, increment_hours):
    temp = quadratic_weather_model(t)
    incremental_times.append(t)
    incremental_temps.append(temp)
    print(f"Time: {t} hrs -> Temp: {temp:.2f}°C (increment added)")

plt.figure(figsize=(8, 5))
plt.plot(incremental_times, incremental_temps, 'ro-', label=f"T = {a}t² + {b}t + {c}")
plt.title("Weather Modeling - Incremental Model (Quadratic)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
