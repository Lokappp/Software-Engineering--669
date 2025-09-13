import matplotlib.pyplot as plt
import numpy as np

# Coefficients for quadratic model
a, b, c = 0.4, -2.5, 26

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c
print("=== ITERATIVE MODEL ===")
for iteration in range(1, 4):  
    print(f"Iteration {iteration}:")
    for hour in range(0, 25, 12):  
        temp = quadratic_weather_model(hour)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("---")
    
hours = np.arange(0, 25, 12)  
plt.figure(figsize=(8, 5))

for iteration in range(1, 4):
    temps = [quadratic_weather_model(t) for t in hours]
    plt.plot(hours, temps, marker='o', label=f"Iteration {iteration}")

plt.title("Weather Modeling - Iterative Model (Quadratic)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
