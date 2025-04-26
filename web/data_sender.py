# data_sender.py
# Water Level Sender to Local Server
# Author: [Rasya Pratama]
# Date: [27 Apr 2025]

import requests
import time
from sensor.float_sensor_read import WaterLevelSensor

SERVER_URL = "http://localhost:5000/update_level"

def send_water_level(level):
    payload = {"level": level}
    try:
        response = requests.post(SERVER_URL, json=payload)
        if response.status_code == 200:
            print(f"[INFO] Successfully sent: {level}")
        else:
            print(f"[ERROR] Failed to send: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Server connection error: {e}")

def main():
    sensor = WaterLevelSensor(config_path="sensor/sensor_config.yaml")
    print("Starting Water Level Data Sender...")

    try:
        while True:
            level = sensor.read_level()
            send_water_level(level)
            time.sleep(sensor.read_interval)
    except KeyboardInterrupt:
        print("\n[INFO] Stopping Data Sender...")

if __name__ == "__main__":
    main()
