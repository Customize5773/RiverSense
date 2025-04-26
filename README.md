# RiverSense
> River Monitoring System Based on Liquid Sensors and YOLOv8 on Raspberry Pi
## Background

The increase in human activities has caused various environmental problems, including river pollution that can lead to flooding and a decline in water quality. One of the main challenges is detecting and monitoring river conditions in real-time to ensure appropriate mitigation measures can be taken.

**RiverSense** is designed to provide an innovative solution by integrating liquid sensors, YOLOv8-based object recognition, and Raspberry Pi to monitor river water levels and detect waste on the water surface. This system aims to deliver up-to-date information to local users through a web-based server, assisting in quick and accurate decision-making.

## Project Description
**RiverSense** is a river condition monitoring system that integrates:
- Water level sensing using three Polypropylene Liquid Water Level Float Switches.
- Visual detection of waste in the river current using ESP32-CAM and the YOLOv8 Object Detection algorithm.
- All data is processed and controlled by the **Raspberry Pi Model B+** and sent to a local HTML/JS-based website server.

The main objectives of RiverSense are to provide real-time information regarding:
- River water level
- The presence of waste detected on the river surface

The system utilizes a **Mini UPS** as a backup power supply to maintain operational stability during power outages.

---

## Key Features
- 📈 Real-time water level monitoring using three vertical float switches.
- 📷 Visual waste detection using an ESP32-CAM with the YOLOv8 model.
- 🌐 Automatic transmission of sensor data and detection results to a local website.
- ⚡ Backup power using a Mini UPS to keep the system running during power failures.

---

## System Architecture

```
+-----------------+      +-----------------+       +-----------------+
| Liquid Float    |      | ESP32-CAM       |       | Raspberry Pi B+ |
| Sensors (3x)    |      | YOLO8 Detection |       | Local Webserver |
+--------+--------+      +--------+--------+       +--------+--------+
         |                       |                       |
         +-----------+-------------+-----------+-------------+
                         |
                     Mini UPS
```

---

## Component Specifications

### Liquid Water Level Float Switch (Polypropylene)
- **Max Contact Rating:** 10W
- **Max Switching Voltage:** 220V DC/AC
- **Max Switching Current:** 1.5A
- **Temperature Rating:** -10°C to +85°C
- **Materials:** Float Ball & Body - Polypropylene (PP)
- **Dimensions:** 23.3mm (Diameter) x 57.7mm (Height)
- **Cable Length:** 36cm

### ESP32-CAM Module
- **Processor:** Dual-core 32-bit, 240MHz
- **Memory:** 520KB SRAM + 4MB PSRAM
- **Camera Support:** OV2640 / OV7670
- **WiFi Modes:** STA / AP / STA+AP
- **Storage:** TF Card support
- **Framework:** FreeRTOS embedded

### Raspberry Pi Model B+
- **Processor:** ARM1176JZF-S, 700MHz
- **RAM:** 512MB SDRAM
- **Connectivity:** WiFi Dongle USB
- **Storage:** microSD

---

## Data Flow Architecture

```
Liquid Float Sensors -> GPIO Raspberry Pi
ESP32-CAM -> WiFi Stream (Captured Image) -> Raspberry Pi
Raspberry Pi -> YOLO8 Inference
Raspberry Pi -> Data Aggregation -> Local Website (HTML/JS)
```

- Data is sent in **JSON** format to the local server via HTTP POST.
- The local website polls or receives push updates to refresh data dynamically.

---

## Installation

### Hardware
1. Mount the 3x Liquid Water Level Sensors vertically in a waterproof protective box.
2. Connect the three sensors to the GPIO of the Raspberry Pi Model B+.
3. Prepare the ESP32-CAM to monitor the river, ensuring stable WiFi coverage to the Raspberry Pi.
4. Connect the Raspberry Pi and ESP32-CAM to the Mini UPS.

### Software
1. Flash the ESP32-CAM with firmware for image streaming via HTTP.
2. Deploy the YOLOv8 model to the Raspberry Pi using Python (recommendation: [Ultralytics YOLOv8](https://docs.ultralytics.com/)).
3. Run the detection and sensor monitoring scripts on the Raspberry Pi.
4. Run the local HTML/JS-based server for data visualization.

---

## Usage

- Open a browser and access the local website (example: `http://192.168.1.100/`).
- Monitor the river water level and waste detection in real-time.
- The latest data will be updated automatically without manual refresh.

---

## Roadmap
- [ ] Telegram-based notification integration when the water level exceeds safe limits.
- [ ] Historical data storage to a local database (SQLite).
- [ ] Visualization of water level graphs and the number of detected waste items.

---

## License
[MIT License](LICENSE)

---
