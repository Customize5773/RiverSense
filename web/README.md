# RiverSense Local Website

This folder contains the source code for the local monitoring dashboard of RiverSense, running on a lightweight webserver.

---

## Overview

The website displays:
- **Water Level Status** (Very Low, Low, Medium, High)
- **Trash Detection Status** (Trash Detected / No Trash Detected)
- **Live Camera Stream** from ESP32-CAM

The data is fetched dynamically from a local server hosted by Raspberry Pi.

---

## File Structure

```
/web/
│
├── index.html    # Main dashboard page
├── app.js        # JavaScript file to fetch and update sensor data
└── styles.css    # Styling for the dashboard
```

---

## How it Works

- `app.js` fetches data from the API endpoint (`http://<raspberry-pi-ip>:5000/data`) every 5 seconds.
- The water level and trash detection statuses are updated automatically without page reload.
- The ESP32-CAM live stream is embedded as an `<img>` element that refreshes internally.

---

## Setup Instructions

1. Host these files on a simple HTTP server. For example, using Python:
```bash
cd /path/to/web/
python3 -m http.server 8000
```
2. Open your browser and navigate to:
```
http://<raspberry-pi-ip>:8000/
```

3. Ensure:
   - The local API server (Flask/Python) is running and serving data at `/data`.
   - The ESP32-CAM is streaming at `http://192.168.1.50/`.

---

## Notes

- Adjust the `API_URL` in `app.js` if your server IP or port is different.
- Adjust the `img` `src` in `index.html` if your ESP32-CAM IP address is different.

---
