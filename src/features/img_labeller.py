import cv2
import os

input_folder = '../../data/raw/raw_images/'
output_class1 = '../../data/processed/train/class1/' # At the top position of the pushup
output_class2 = '../../data/processed/train/class2/' # At the bottom position of the pushup
output_class3 = '../../data/processed/train/class3/' # Transition between top and bottom

for img in os.listdir(input_folder):
    image = cv2.imread(input_folder + img)
    cv2.imshow('', image)
    k = cv2.waitKey(0)
    # grab only the image number and leave out .png from file name
    index = int(''.join(filter(str.isdigit, img)))

    # assign image to each class depending on key input.
    if k == 49:
        cv2.imwrite(output_class1 + str(index) + "_labelled.png", image)
    elif k == 50:
        cv2.imwrite(output_class2 + str(img) + "_labelled.png", image)
    elif k == 51:
        cv2.imwrite(output_class3 + str(img) + "_labelled.png", image)
    elif k == 32:
        break

    # Remove the image to prevent duplicates
    os.remove(input_folder + img)
    cv2.destroyAllWindows()