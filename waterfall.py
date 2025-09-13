import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# Coefficients for quadratic model
a, b, c = 0.4, -2.5, 26

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c


print("=== WATERFALL MODE ===")
for hour in range(0, 25, 6):  # every 6 hours
    temp = quadratic_weather_model(hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")


hours = np.arange(0, 25, 1)
temps = [quadratic_weather_model(t) for t in hours]

plt.figure(figsize=(8, 5))
plt.plot(hours, temps, 'bo-', label=f"T = {a}t² + {b}t + {c}")
plt.title("Weather Modeling - Waterfall Mode (Quadratic Model)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
