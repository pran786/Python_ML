import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from time import time



#parameters for finding the distance between camera and object
focal_length = 1500
image_height = 75
object_height = 5
# distance = 100
speed = 0
prev_distance = 0
# #first need to find the focal length of camera
# #focal_length = round(((image_height*distance)/object_height),2)
# def find_focal_length():
#     focal_length = (image_height*distance)/object_height
#     print(focal_length)

# find_focal_length()


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector()
speedl = [0]
while True:
    ret,frame = cap.read()
    
    if ret:
        hands,frame = detector.findHands(frame)
        
        if hands:
            for hand in hands:
                #print(hand)
                nuckles = hand['lmList']
                bbox = hand['bbox']
                cpts = hand['center']
                ptx,pty,ptw,pth = bbox
               
                f1x,f1y,f1z = nuckles[5]
                f2x,f2y,f2z = nuckles[17]
                #print(nuckles[5])
                #handwidth = np.linalg.norm(np.array((f1x,f1y,f1z))-np.array((f2x,f2y,f2z)))
                handwidth = round(np.sqrt((f2x-f1x)**2+(f2y-f1y)**2+(f2z-f1z)**2),2)
                
                  

                t1 = time()
                #print(t1)
                distance = (object_height*focal_length)//handwidth
                distance = distance
                if prev_distance!=0:
                    speed = round(abs(distance-prev_distance)/abs(t1-t2))
                    if len(speedl)>=10:
                        speedl.pop(0)
                    speedl.append(speed)
                    #print(speedl)
                    #print(t1-t2)
                    prev_distance = distance
                    t2 = t1
                    
                else:
                    prev_distance = distance
                    t2 = t1
                




                frame = cv2.putText(frame, f'distance : {distance}CM', cpts, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3, cv2.LINE_AA)
                frame = cv2.putText(frame, f'speed : {sum(speedl)//len(speedl)}cm/s', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3, cv2.LINE_AA)
                
                #print(handwidth)
                
        cv2.imshow('image',frame)
        cv2.waitKey(10)



