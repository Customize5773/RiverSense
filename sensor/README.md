### File Structure
```bash
/sensor/
│
├── float_sensor_read.py
└── sensor_config.yaml
```
---
## float_sensor_read.py
**Purpose:**
- Reads the state of three float switches via Raspberry Pi GPIO.
- Determines the current water level (VERY LOW, LOW, MEDIUM, HIGH).
- Outputs the status periodically in the terminal.
- Built using a WaterLevelSensor class for easy system integration.
   
**Features:**
- Loads GPIO pins and reading interval from sensor_config.yaml.
- Uses internal pull-up resistors (active LOW logic).
- Handles errors if the configuration file is missing.
- Cleans up GPIO properly on program exit.

How to run:
```bash
  python3 float_sensor_read.py
```

---

## sensor_config.yaml
**Purpose:**
- Stores GPIO pin assignments for each sensor (Low, Medium, High).
- Sets the reading interval in seconds.
Example content:
```yaml
  pins:
  low: 17       # GPIO17
  medium: 27    # GPIO27
  high: 22      # GPIO22

read_interval: 2  # Reading interval in seconds
```
Notes:
- Ensure the GPIO pin numbers match your hardware wiring.
- Recommended reading interval is ≥ 1 second for stable readings.

---
## Dependencies
Ensure Raspberry Pi has the following libraries installed:
```bash
  pip install RPi.GPIO pyyaml
```
---
# Notes
- This module only reads sensor states. To send data to a local server or for logging purposes, additional integration is required.
- Float switches operate with active LOW logic: when touched by water, the switch closes and pulls the GPIO pin to GND.
