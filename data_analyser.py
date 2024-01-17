import json
import pandas as pd
import matplotlib.pyplot as plt

# Load JSON data from the file
file_path = "random_sensor_data.json"
with open(file_path, "r") as file:
    sensor_data = json.load(file)

# Convert JSON data to a Pandas DataFrame
df = pd.DataFrame(sensor_data)

# Convert timestamp to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Display the DataFrame with formatted timestamp
df['formatted_timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d')
print("DataFrame:")
print(df[['formatted_timestamp', 'sensor_id', 'value']])

# Data Analysis Example: Plotting
for sensor_id, group in df.groupby("sensor_id"):
    plt.plot(group["timestamp"], group["value"], label=sensor_id)


# Calculate the index of the middle row
middle_index = len(df) // 2

# Set x-axis ticks with the timestamp of the middle row
plt.xticks([df['timestamp'].iloc[0], df['timestamp'].iloc[middle_index], df['timestamp'].iloc[-1]])


plt.title("Sensor Data Analysis")
plt.xlabel("Timestamp")
plt.ylabel("Sensor Value")
plt.legend()
plt.show()
