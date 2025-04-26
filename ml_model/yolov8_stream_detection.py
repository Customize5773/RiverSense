# yolov8_stream_detection.py
# Object Detection from ESP32-CAM stream using YOLOv8
# Author: [Rasya Pratama]
# Date: [27 Apr 2025]

from ultralytics import YOLO
import cv2
import math

class YOLOv8_Stream:
    def __init__(self, model_path="../ml_model/model/river_trash_yolov8.pt", stream_url="http://192.168.1.50/"):
        self.model = YOLO(model_path)
        self.stream_url = stream_url
        
        self.classNames = [
            "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
            "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
            "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
            "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
            "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
            "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
            "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
            "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
            "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
            "teddy bear", "hair drier", "toothbrush"
        ]

    def start_detection(self):
        cap = cv2.VideoCapture(self.stream_url)

        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))

        while True:
            success, img = cap.read()
            if not success:
                print("[ERROR] Failed to fetch image from stream!")
                break

            results = self.model(img, stream=True)

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    conf = math.ceil((box.conf[0]*100))/100
                    cls = int(box.cls[0])

                    class_name = self.classNames[cls] if cls < len(self.classNames) else "Unknown"
                    label = f'{class_name} {conf}'

                    # Draw rectangle and label
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                    c2 = x1 + t_size[0], y1 - t_size[1] - 3
                    cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
                    cv2.putText(img, label, (x1, y1-2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

            out.write(img)
            cv2.imshow("RiverSense Stream", img)

            if cv2.waitKey(1) & 0xFF == ord('1'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = YOLOv8_Stream(
        model_path="../ml_model/model/river_trash_yolov8.pt",
        stream_url="http://192.168.1.50/"  # adjust with your ESP32-CAM IP
    )
    detector.start_detection()
