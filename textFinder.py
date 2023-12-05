from PIL import Image
import pytesseract
import cv2
import os

img = 'C:/Users/rs/screenie.png'
preprocess = "thresh"
image = cv2.imread(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.error: OpenCV(4.6.0) :-1: error: (-5:Bad argument) in function 'cvtColor'
> Overload resolution failed:
>  - src is not a numpy array, neither a scalar
>  - Expected Ptr<cv::UMat> for argument 'src'

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

    
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
False
cv2.imwrite(filename, gray)
False
filename = "C:/Users/rs/{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
True
os.chdir("C:/Users/rs")
text = pytesseract.image_to_string(Image.open(filename))
