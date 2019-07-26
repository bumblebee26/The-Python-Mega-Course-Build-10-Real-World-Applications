# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 02:06:45 2019

@author: viren
"""

import cv2
import os


face_cascade=cv2.CascadeClassifier("files\haarcascade_frontalface_default.xml")

base_filename=input("\nEnter the name of the .jpg file : ")

dir_name= "C:\\Viren\\Work\\Python\\Solutions\\18. Python for Image and Video Processing with OpenCV\Files\\"
filename_suffix = "jpg"
x=os.path.join(dir_name, base_filename + "." + filename_suffix)


img=cv2.imread(x)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
                                    scaleFactor=1.1,
                                    minNeighbors=5)
##using scaleFactor=1.1

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) 
    
## rectangle(img,x,y,width,height,(color of rectangle),(width of rectangle))
## color of rectangle : BGR--> 255,0,0 --> "Blue" 
## color of rectangle : BGR--> 0,255,0 --> "Green"
## color of rectangle : BGR--> 0,0,255 --> "Red"

print(faces)

resized=cv2.resize(img,(500,500))


cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()