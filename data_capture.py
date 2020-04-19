import cv2

output_folder = "raw_images/"

# Capture frames from webcam video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Reads and starts the new image count from said number
with open("start_from.txt", "r") as f:
    img_count = int(f.readline())

while True:
    ret, frame = cap.read()
    cv2.imwrite(output_folder + str(img_count) + ".png", frame)
    img_count += 1
    key = cv2.waitKey(1)
    cv2.imshow('', frame)

    with open("start_from.txt", "w") as f:
        f.write(str(img_count))

    if key == 32:  # 32 is space key
        break

cap.release()
cv2.destroyAllWindows()