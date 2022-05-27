import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\tersract\\tesseract.exe'
img = cv2.imread('b.png')
#tesseract only accept rgb value
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
## detecting characters
# print(pytesseract.image_to_boxes(img))
# hImg,wImg, = img.shape
cv2.imshow("Result",img)
cv2.waitKey(0)

