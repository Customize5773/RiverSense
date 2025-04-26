# float_sensor_read.py
# Water Level Monitoring using 3x Float Switches with config file
# Author: [Rasya Pratama]
# Date: [27 Apr 2025]

import RPi.GPIO as GPIO
import yaml
import time
import os

class WaterLevelSensor:
    def __init__(self, config_path="sensor_config.yaml"):
        self.config = self.load_config(config_path)
        self.pins = {
            'low': self.config['pins']['low'],
            'medium': self.config['pins']['medium'],
            'high': self.config['pins']['high']
        }
        self.read_interval = self.config.get('read_interval', 2)

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Setup GPIO pins
        for pin in self.pins.values():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def load_config(self, path):
        """Load YAML configuration file."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Configuration file not found: {path}")
        
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def read_level(self):
        """Determine current water level based on sensor states."""
        states = {key: GPIO.input(pin) == GPIO.LOW for key, pin in self.pins.items()}

        if states['high']:
            return "HIGH"
        elif states['medium']:
            return "MEDIUM"
        elif states['low']:
            return "LOW"
        else:
            return "VERY LOW / EMPTY"

    def monitor(self):
        """Continuously monitor the water level."""
        print("Starting Water Level Monitoring...")
        try:
            while True:
                level = self.read_level()
                print(f"[INFO] Water Level Status: {level}")
                time.sleep(self.read_interval)
        except KeyboardInterrupt:
            print("\n[INFO] Stopping monitoring...")
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
    sensor = WaterLevelSensor()
    sensor.monitor()
