# RiverSense Web Interface

This folder contains the web server and data sender scripts for the RiverSense project.

---

## File Structure
```
/web/
│
├── server.py         # Local Flask server to display water level + camera feed
├── data_sender.py    # Client script to send water level readings to server
```

---

## Requirements
- Python 3.8+
- Flask
- Requests

Install dependencies:
```bash
pip install flask requests
```

---

## Usage

1. **Start the Server:**
```bash
python3 server.py
```
Access the website at:
```
http://<your-raspberry-pi-ip>:5000/
```

2. **Start the Data Sender:**
```bash
python3 data_sender.py
```
This will read the water level sensors and push updates automatically to the server.

---

## Features
- Real-time water level status display.
- Live ESP32-CAM video stream embedded into the web page.
- Lightweight and easy to deploy on Raspberry Pi.

---

## Notes
- Update `ESP32CAM_STREAM_URL` inside `server.py` to match your camera IP.
- Make sure the Raspberry Pi and ESP32-CAM are on the same WiFi network.

---
