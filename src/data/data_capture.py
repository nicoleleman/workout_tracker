import cv2
import os

output_folder = "../../data/raw/raw_images/"

# Capture frames from webcam video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    raise IOError("Webcam not detected!")

# Reads and starts the new image count from said number
with open("img_counter.txt", "r") as f:
    img_count = int(f.readline())

while True:
    ret, frame = cap.read()
    cv2.imwrite(output_folder + str(img_count) + ".png", frame)
    img_count += 1
    key = cv2.waitKey(1)
    cv2.imshow('', frame)

    with open("img_counter.txt", "w") as f:
        f.write(str(img_count))

    if key == 32:  # press space bar to end the script
        break

cap.release()
cv2.destroyAllWindows()