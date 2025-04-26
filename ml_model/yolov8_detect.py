# yolov8_detect.py
# YOLOv8 Detection for RiverSense Project
# Input source: ESP32-CAM MJPEG Stream
# Author: [Your Name]
# Date: [Date]

from ultralytics import YOLO
import cv2
import math

# ========================
# CONFIGURATION
# ========================
ESP32_CAM_STREAM_URL = "http://<ESP32-CAM-IP>/"  # <-- Replace with your ESP32-CAM IP Address

# Load YOLOv8 model
model = YOLO("../ml_model/model/river_trash_yolov8.pt")  # Update model path if needed

# Class names (customize if using custom dataset)
classNames = ["plastic_bottle", "trash_bag", "styrofoam", "wood_piece", "leaf", "unknown_object"]

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
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw bounding box
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls] if cls < len(classNames) else "Unknown"
                label = f'{class_name} {conf}'

                # Draw label
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = (x1 + t_size[0], y1 - t_size[1] - 3)
                cv2.rectangle(img, (x1, y1), c2, (255, 0, 255), -1, cv2.LINE_AA)
                cv2.putText(img, label, (x1, y1-2), 0, 1, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

        cv2.imshow("RiverSense Trash Detection", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
