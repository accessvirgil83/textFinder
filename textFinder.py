from PIL import Image
import pytesseract
import cv2
import os

img = 'C:/Users/rs/screenie.png'
preprocess = "thresh"
image = cv2.imread(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3) 
filename = "{}.png".format(os.getpid())
#filename = "C:/Users/rs/{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
