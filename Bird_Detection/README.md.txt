# PiBirdDetect: AI-Powered Bird Detection System for Raspberry Pi

PiBirdDetect leverages AI and hardware integration to detect birds using a PIR motion sensor and a YOLOv5 object detection model. This system combines motion detection with real-time video analysis to identify birds and trigger alerts, making it ideal for projects like bird deterrence or wildlife observation.

---

## Features
- **AI-Powered Detection**: Uses the YOLOv5 object detection model to identify birds with high precision.
- **Motion Activation**: Reduces resource usage by only processing frames when motion is detected via a PIR sensor.
- **Alert System**: Plays a sound alert when a bird is detected.
- **Visualization**: Displays real-time bounding boxes and confidence scores for detected birds (optional).

---

## AI and Object Detection Workflow

### YOLOv5 Object Detection Model
- **Model**: This project uses the `yolov5s` model, a lightweight, pre-trained model from the YOLO (You Only Look Once) family, optimized for real-time object detection.
- **Dataset**: YOLOv5 is trained on the COCO dataset, which includes 80 classes. The "bird" class corresponds to `class ID 14`.
- **Inference**: When motion is detected, the script captures a video frame and passes it to the YOLOv5 model for inference. The model returns bounding boxes, confidence scores, and class IDs for detected objects.

### Why YOLOv5?
- **Speed and Efficiency**: The `yolov5s` variant balances speed and accuracy, making it suitable for Raspberry Pi hardware.
- **Pre-trained Models**: Eliminates the need for additional training, as the COCO dataset already includes birds.

### Key Functionality
- **Bounding Boxes**: Highlight detected birds in the frame.
- **Confidence Scores**: Display the model's certainty for each detection.

---

## Requirements

### Hardware
- **Raspberry Pi**: Any model with GPIO support (e.g., Raspberry Pi 4 or 3).
- **PIR Motion Sensor**: For motion detection, connected to GPIO pin 18.
- **Camera**: Raspberry Pi Camera Module or USB webcam.

### Software
- **Python 3.x**
- Python Libraries:
  - `torch`: For running the YOLOv5 deep learning model.
  - `opencv-python`: For capturing and displaying video.
  - `RPi.GPIO`: For interfacing with the PIR motion sensor.

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/PiBirdDetect.git
cd PiBirdDetect
