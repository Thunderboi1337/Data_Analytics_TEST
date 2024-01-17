import json
import random
from datetime import datetime, timedelta

def generate_random_sensor_data(sensor_id):
    timestamp = datetime.utcnow().isoformat() + "Z"
    value = round(random.uniform(10.0, 30.0), 2)
    unit = "Celsius"

    data = {
        "timestamp": timestamp,
        "sensor_id": sensor_id,
        "value": value,
        "unit": unit,
        "location": {
        }
    }

    return data

def generate_random_sensor_data_batch(sensor_ids, num_samples):
    data_batch = []

    for _ in range(num_samples):
        sensor_id = random.choice(sensor_ids)
        sensor_data = generate_random_sensor_data(sensor_id)
        data_batch.append(sensor_data)

    return data_batch

if __name__ == "__main__":
    # Example: Generate random data for three sensors, each with 5 samples
    sensor_ids = ["temperature_sensor_1",
                  "humidity_sensor_1", "pressure_sensor_1"]
    num_samples = 5

    random_data_batch = generate_random_sensor_data_batch(
        sensor_ids, num_samples)

    # Append generated JSON data to the existing file
    output_file = "random_sensor_data.json"
    with open(output_file, "a") as file:
        # Add a newline character before appending to separate batches
        if file.tell() != 0:
            file.write("\n")
        json.dump(random_data_batch, file, indent=2)

    print(f"Generated data appended to {output_file}")

