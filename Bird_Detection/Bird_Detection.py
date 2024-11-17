import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
cap = cv2.VideoCapture(2)

BIRD_CLASS_ID = 14

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)
    detections = results.pandas().xyxy[0]
    bird_detections = detections[detections['class'] == BIRD_CLASS_ID]
    for index, row in bird_detections.iterrows():
        xmin, ymin, xmax, ymax, confidence = \
            (
                int(row['xmin']),
                int(row['ymin']),
                int(row['xmax']),
                int(row['ymax']),
                row['confidence']
            )
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(frame, f'Bird {confidence:.2f}', (xmin, ymin - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Bird Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
