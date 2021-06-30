__author__ = 'Shadab Shaikh, Obaid Kazi'

import cv2
import numpy as np

def nothing(x):
    pass

image_x, image_y = 64,64

from keras.models import load_model
classifier = load_model('ASLModel.h5')

def predictor():
       import numpy as np
       from keras.preprocessing import image
       test_image = image.load_img('1.png', target_size=(64, 64))
       test_image = image.img_to_array(test_image)
       test_image = np.expand_dims(test_image, axis = 0)
       result = classifier.predict(test_image)
       
       if result[0][0] == 1:
              return 'A'
       elif result[0][1] == 1:
              return 'B'
       elif result[0][2] == 1:
              return 'C'
       elif result[0][3] == 1:
              return 'D'
       elif result[0][4] == 1:
              return 'E'
       elif result[0][5] == 1:
              return 'F'
       elif result[0][6] == 1:
              return 'G'
       elif result[0][7] == 1:
              return 'H'
       elif result[0][8] == 1:
              return 'I'
       elif result[0][9] == 1:
              return 'J'
       elif result[0][10] == 1:
              return 'K'
       elif result[0][11] == 1:
              return 'L'
       elif result[0][12] == 1:
              return 'M'
       elif result[0][13] == 1:
              return 'N'
       elif result[0][14] == 1:
              return 'O'
       elif result[0][15] == 1:
              return 'P'
       elif result[0][16] == 1:
              return 'Q'
       elif result[0][17] == 1:
              return 'R'
       elif result[0][18] == 1:
              return 'S'
       elif result[0][19] == 1:
              return 'T'
       elif result[0][20] == 1:
              return 'U'
       elif result[0][21] == 1:
              return 'V'
       elif result[0][22] == 1:
              return 'W'
       elif result[0][23] == 1:
              return 'X'
       elif result[0][24] == 1:
              return 'Y'
       elif result[0][25] == 1:
              return 'Z'
       

       

cam = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

cv2.moveWindow("Trackbars",700,30)

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

cv2.namedWindow("ASL Scanning Window")

    
img_text = ''
img_text1 = ''
append_text=''
finalBuffer=[]
x=0
y=0
y1=y+10
z=0

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")


    img = cv2.rectangle(frame, (425,100),(625,300), (0,255,0), thickness=2, lineType=8, shift=0)

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    imcrop = img[102:298, 427:623]
    hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow("ASL Scanning Window", frame)
    cv2.imshow("mask", mask)
    cv2.moveWindow("mask", 1050,30)
    
    img1 = np.zeros((100,500,4), np.uint8)
    img2 = np.zeros((400,400,4), np.uint8)
    img3 = np.zeros((400,400,4), np.uint8)
    cv2.putText(img3, img_text, (160, 220), cv2.FONT_HERSHEY_TRIPLEX, 3.5, (0, 255, 0))
    cv2.imshow("Scanned Window", img3)
    cv2.moveWindow("Scanned Window", 900,300)
    img_name = "1.png"
    save_img = cv2.resize(mask, (image_x, image_y))
    cv2.imwrite(img_name, save_img)
    img_text=predictor()
    if cv2.waitKey(1) == ord('c'):
      try:
        append_text+=img_text
      except:
        append_text+=''
      cv2.putText(img1, append_text, (1, 10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0))
      try:
        y=0
        for x in range(len(finalBuffer)):
          cv2.putText(img2, finalBuffer[x], (1, 10+y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0))
          y+=20
      except:
        pass
      cv2.imshow("Freezing Window", img1)     
      cv2.imshow("Output Window", img2)
      
      if(len(append_text)>25):
        finalBuffer.append(append_text)
        print(finalBuffer[z])
        append_text=''
        z+=1
        

    if cv2.waitKey(1) == 27:
    	f=open("temp.txt","w")
    	for i in finalBuffer:
    		f.write(i)
    	f.close()
    	
    	break
	    

cam.release()
cv2.destroyAllWindows()
