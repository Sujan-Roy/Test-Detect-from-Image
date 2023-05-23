import cv2
import matplotlib.pyplot as plt
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#C:\Program Files\Tesseract-OCR

input_image= cv2.imread('input.png')
# Color convert
image_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

retthres, thresh= cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY +
                                 cv2.THRESH_OTSU)

rec_image_structure= cv2.getStructuringElement(cv2.MORPH_RECT,(180,180))

dialation = cv2.dilate(thresh,rec_image_structure,iterations=3)

contours, hierarchy = cv2.findContours(dialation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)

input_image_copy = input_image.copy()

file = open("Text_From_Image.txt", "w+")
file.write("")
file.close()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
  
    rect = cv2.rectangle(input_image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
  
    cropped = input_image_copy[y:y + h, x:x + w]
     
   
    file = open("Text_From_Image.txt", "a")
     
  
    text = pytesseract.image_to_string(cropped)
    
     
    
    file.write(text)
    file.write("\n")
     
    # Close the file
    file.close


#plt.subplot(2,1,1)
#plt.figure(figsize=(5,5))
#plt.imshow(thresh)
#plt.subplot(2,1,2)
#plt.figure(figsize=(5,5))
#plt.imshow(thresh)
#plt.show()

