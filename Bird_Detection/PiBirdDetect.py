import torch
import RPi.GPIO as GPIO
import os
import time
import cv2

# Initialize GPIO
PIR_PIN = 18  # GPIO pin for PIR sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Load the pre-trained YOLOv5 model (yolov5s is a small model for faster detection)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load webcam (change 0 to a video path for video input)
cap = cv2.VideoCapture(0)
time.sleep(2)  # Allow camera to initialize

# Class ID for birds in COCO dataset (YOLOv5 is trained on COCO dataset, class 14 corresponds to "bird")
BIRD_CLASS_ID = 14

def play_sound():
    """Function to play an alert sound when a bird is detected."""
    os.system("aplay /home/lidah/Bird_Detection/sounds/BirdDeterence.wav")  # Replace with your actual sound file path

try:
    print("Waiting for motion...")

    # Check if the camera is initialized
    if not cap.isOpened():
        print("Camera failed to initialize.")
        GPIO.cleanup()
        exit()

    while True:
        # Check PIR sensor for motion
        if GPIO.input(PIR_PIN):
            print("Motion detected! Checking for birds...")
            time.sleep(1)  # Allow PIR sensor to stabilize

            ret, frame = cap.read()
            if not ret:
                print("Camera error. Reinitializing...")
                cap.release()
                cap = cv2.VideoCapture(0)
                time.sleep(2)  # Allow camera to stabilize
                continue

            # Run YOLOv5 model on the frame
            results = model(frame)

            # Convert detection results into a pandas DataFrame
            detections = results.pandas().xyxy[0]

            # Filter for "bird" class
            bird_detections = detections[detections['class'] == BIRD_CLASS_ID]

            # If any bird is detected
            if not bird_detections.empty:
                print("Bird detected! Playing sound...")
                play_sound()

                # Draw bounding boxes for detected birds
                for index, row in bird_detections.iterrows():
                    xmin, ymin, xmax, ymax, confidence = \
                        (
                            int(row['xmin']),
                            int(row['ymin']),
                            int(row['xmax']),
                            int(row['ymax']),
                            row['confidence']
                        )

                    # Draw the bounding box
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

                    # Add label
                    cv2.putText(frame, f'Bird {confidence:.2f}', (xmin, ymin - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Display the frame
                cv2.imshow('Bird Detection', frame)

            else:
                print("No bird detected.")

            # Delay to prevent rapid re-triggering
            time.sleep(10)

        # Show live feed (optional, can remove for headless setup)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Live Feed', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Cleanup resources
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()