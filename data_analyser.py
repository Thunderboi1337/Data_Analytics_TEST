import json
import pandas as pd
import matplotlib.pyplot as plt

# Load JSON data from the file
file_path = "random_sensor_data.json"
with open(file_path, "r") as file:
    sensor_data = json.load(file)

# Convert JSON data to a Pandas DataFrame
df = pd.DataFrame(sensor_data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Data Analysis Example: Plotting
for sensor_id, group in df.groupby("sensor_id"):
    plt.plot(group["timestamp"], group["value"], label=sensor_id)

plt.title("Sensor Data Analysis")
plt.xlabel("Timestamp")
plt.ylabel("Sensor Value")
plt.legend()
plt.show()
