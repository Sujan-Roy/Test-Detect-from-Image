import cv2
import matplotlib.pyplot as plt

input_image= cv2.imread('input.png')
# Color convert
image_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

retthres, thresh= cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(5,5))
plt.imshow(image_gray)
plt.show()