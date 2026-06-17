import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("heat_exchanger_large_dataset.csv")

# Handle missing values
df['Outlet_Temp (°C)'] = df['Outlet_Temp (°C)'].ffill()

# Calculate temperature drop
df['Temp_Drop'] = df['Inlet_Temp (°C)'] - df['Outlet_Temp (°C)']

# Basic statistics
avg = np.mean(df['Temp_Drop'])
stdev = np.std(df['Flow_Rate (L/min)'])
maxtempdrop = np.argmax(df['Temp_Drop'])
time = df.loc[maxtempdrop, 'Time (s)']

print("Average Temperature Drop:", avg)
print("Standard Deviation of Flow Rate:", stdev)
print("Time of Maximum Temp Drop:", time)

# Plots
plt.figure()
plt.plot(df['Time (s)'], df['Inlet_Temp (°C)'], color='blue', label='Inlet')
plt.plot(df['Time (s)'], df['Outlet_Temp (°C)'], color='green', label='Outlet')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Inlet vs Outlet Temperature')
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.hist(df['Temp_Drop'], bins=10, color='green', edgecolor='black')
plt.xlabel("Temp Drop (°C)")
plt.ylabel("Frequency")
plt.title("Histogram of Temp Drop")
plt.show()

plt.figure()
plt.scatter(df['Flow_Rate (L/min)'], df['Temp_Drop'], alpha=0.7)
plt.xlabel("Flow Rate (L/min)")
plt.ylabel("Temp Drop (°C)")
plt.title("Flow Rate vs Temp Drop")
plt.show()

# Regression analysis
slope, intercept = np.polyfit(df['Flow_Rate (L/min)'], df['Temp_Drop'], 1)
reg_line = slope * df['Flow_Rate (L/min)'] + intercept
plt.plot(df['Flow_Rate (L/min)'], reg_line, color='red', label=f"y = {slope:.2f}x + {intercept:.2f}")
plt.legend()
plt.show()

if slope > 0:
    print("Positive relationship: higher flow rates increase temperature drop.")
elif slope < 0:
    print("Negative relationship: higher flow rates decrease temperature drop.")
else:
    print("No significant linear relationship detected.")
