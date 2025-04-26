# data_sender.py
# Send real water level sensor data to RiverSense local server
# Author: [Rasya Pratama]
# Date: [27 Apr 2025]

import requests
import time
from sensor.float_sensor_read import WaterLevelSensor

SERVER_URL = "http://localhost:5000/update"

def send_data(water_level, trash_detected=False):
    payload = {
        "water_level": water_level,
        "trash_detected": trash_detected
    }
    try:
        response = requests.post(SERVER_URL, json=payload)
        if response.status_code == 200:
            print(f"[INFO] Data sent successfully: {payload}")
        else:
            print(f"[ERROR] Failed to send data: {response.status_code}")
    except Exception as e:
        print(f"[EXCEPTION] {e}")

def main():
    sensor = WaterLevelSensor(config_path="sensor/sensor_config.yaml")
    while True:
        level = sensor.read_level()
        print(f"[SENSOR] Current water level: {level}")
        send_data(level, trash_detected=False)  # TODO: integrate real trash detection
        time.sleep(sensor.read_interval)

if __name__ == "__main__":
    main()
