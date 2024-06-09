import cv2
from PIL import Image

from util import get_limits

yellow = [0, 255, 255]  # yellow in BGR colorspace
blue = [255, 0, 0] #blue in bgr colorspace
darkpink = [102, 0, 102] #darkpink in bgr colorspace

# Define the video capture object
cap = cv2.VideoCapture(0)  # 0 indicates the default camera

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Capture and display frames until 'q' key is pressed
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
