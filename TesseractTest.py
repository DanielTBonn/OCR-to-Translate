import numpy as np
import pytesseract
import cv2
import sys

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def get_image(img,resizer):
    img_cv = cv2.imread(img)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

    if img_rgb is None:
        sys.exit("Could not read image")

    img_rgb = cv2.resize(img_rgb, (0,0), fx=resizer, fy=resizer)

    return img_rgb

def sharpen_image(img):
    kernel = np.array([[0, -1, 0], 
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    return image_sharp

def identity_image(img):
    kernel = np.array([[0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]])
    image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    return image_sharp

def edge_detect_image(img):
    kernel = np.array([[0, -1, 0],
                      [-1, 4, -1],
                      [0, -1, 0]])
    image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    return image_sharp

def get_characters(img):
    data = pytesseract.image_to_string(img, lang='jpn_vert')
    return data

def display_image(img):
    cv2.imshow("Display window", img)

    k = cv2.waitKey(0)

    if k == ord("s"):
        print('Closing image')
        cv2.destroyAllWindows()

def main():
    resizer = 3
    img_rgb = get_image(img_1, resizer)
    img_sharp = sharpen_image(img_rgb)
    data = get_characters(img_sharp)
    print(data)
    display_image(img_sharp)


