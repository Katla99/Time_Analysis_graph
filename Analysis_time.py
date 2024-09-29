import matplotlib.pyplot as plt

# Data for whipping times at different temperatures
temperatures = [3, 3, 3, 20, 20, 20]  # Corresponding temperatures
times = [45, 42, 44, 56, 50, 49]      # Whipping times in seconds

avg_time_3C = sum(times[:3]) / 3
avg_time_20C = sum(times[3:]) / 3

# Create the scatter plot
plt.figure(figsize=(8, 5))

# Scatter points for 3°C
plt.scatter([3]*3, times[:3], color='blue', label='3°C', s=100)  # Blue for 3°C
# Scatter points for 20°C
plt.scatter([20]*3, times[3:], color='red', label='20°C', s=100)  # Red for 20°C

# Plot the average lines for both temperatures
plt.axhline(y=avg_time_3C, color='blue', linestyle='--', label=f'Avg 3°C: {avg_time_3C:.2f} sec')
plt.axhline(y=avg_time_20C, color='red', linestyle='--', label=f'Avg 20°C: {avg_time_20C:.2f} sec')

# Labels and title
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Whipping Time (seconds)', fontsize=12)

# Adding grid
plt.grid(True)

# Adding a legend
plt.legend()

# Show the plot
plt.show()
