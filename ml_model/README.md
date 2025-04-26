# RiverSense YOLOv8 Stream Detection

This module handles object detection on the ESP32-CAM video stream using a YOLOv8 model.

---

## File Structure
```
/ml_model/
│
├── yolov8_stream_detection.py  
├── model/
│   └── river_trash_yolov8.pt     # Trained YOLOv8 model (custom trash detection)
├── requirements.txt  
```

---

## Requirements
- Python 3.8+
- OpenCV
- ultralytics (YOLOv8)

Install dependencies:
```bash
pip install opencv-python ultralytics
```

---

## Usage

1. Make sure the ESP32-CAM is running and accessible via IP address (default `http://192.168.1.50/`).
2. Run the detection script:
```bash
python3 yolov8_stream_detection.py
```
3. Press `1` to stop detection.

---

## Notes
- Modify `stream_url` and `model_path` if your network IP or model location is different.
- Output video is saved as `output.avi` in the current directory.
- Adjust ESP32-CAM resolution (in firmware) if detection is slow.

---
