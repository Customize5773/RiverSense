# RiverSense - Machine Learning Model

This folder contains the YOLOv8 detection script and model files used to detect trash on the river surface, captured from ESP32-CAM live stream.

---

## File Structure
```bash
/ml_model/
│
├── yolov8_detect.py
├── model/
│        └── river_trash_yolov8.pt
└── requirements.txt
```
---

## Installation

Install required Python packages:

```bash
pip install ultralytics opencv-python
```
Usage
1. Update the ESP32_CAM_STREAM_URL in yolov8_detect.py with your actual ESP32-CAM IP address.
2. Run the detection script:
```bash
python3 yolov8_detect.py
```
3. The live video with detection results will appear in a window.
    Press 'q' to exit.

Notes
- Ensure your Raspberry Pi has enough resources (RAM/CPU) to run real-time YOLOv8 detection.
- For better performance, using the smaller model version (yolov8n.pt or a quantized model) is recommended.
- You can customize the classNames list if using different or more specific object classes.
