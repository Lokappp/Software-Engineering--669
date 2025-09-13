import matplotlib.pyplot as plt
import numpy as np

# Coefficients for quadratic model
a, b, c = 0.4, -2.5, 26

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c
print("=== AGILE MODEL ===")
times_to_check = [0, 6, 12, 18, 24]  # hours to check
for sprint in range(1, 3):  # 2 sprints
    print(f"Sprint {sprint}:")
    for t in times_to_check:
        temp = quadratic_weather_model(t)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")
plt.figure(figsize=(8, 5))

for sprint in range(1, 3):
    temps = [quadratic_weather_model(t) for t in times_to_check]
    plt.plot(times_to_check, temps, marker='o', label=f"Sprint {sprint}")

plt.title("Weather Modeling - Agile Model (Quadratic)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
