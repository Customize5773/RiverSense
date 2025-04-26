# yolov8_detect_minimal.py
# YOLOv8 - Minimal detection for bottle, boat, and plastic-like objects only
# Author: [Rasya Pratama]
# Date: [27 Apr 2025]

from ultralytics import YOLO
import cv2
import math

# ========================
# CONFIGURATION
# ========================
ESP32_CAM_STREAM_URL = "http://<ESP32-CAM-IP>/"  # <-- Replace with your ESP32-CAM IP Address

# Load YOLOv8 model (pre-trained on COCO)
model = YOLO("../ml_model/model/river_trash_yolov8.pt")  # Previously uploaded yolov8n.pt

# Target Classes: Focus only on these COCO labels
TARGET_CLASSES = ["bottle", "boat", "backpack", "handbag", "umbrella", "plastic_bag_like"]

# Mapping class indices from COCO
COCO_CLASSES = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
    "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
    "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
    "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
    "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
    "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]

# ========================
# MAIN PROGRAM
# ========================
def main():
    cap = cv2.VideoCapture(ESP32_CAM_STREAM_URL)

    if not cap.isOpened():
        print("[ERROR] Cannot open ESP32-CAM stream.")
        return

    while True:
        success, img = cap.read()
        if not success:
            print("[WARNING] Failed to grab frame from ESP32-CAM")
            continue

        # YOLOv8 detections
        results = model(img, stream=True)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls = int(box.cls[0])
                class_name = COCO_CLASSES[cls]

                # Only process selected classes
                if class_name in ["bottle", "boat", "backpack", "handbag", "umbrella"]:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    label = f'{class_name} {conf}'

                    # Draw bounding box
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
                    cv2.putText(img, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

        cv2.imshow("RiverSense Minimal Detection", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
