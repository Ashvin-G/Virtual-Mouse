import cv2
import numpy as np
import mediapipe as mp
from math import sqrt
import win32api, win32con
import urllib.request
from pynput.mouse import Button, Controller

url = "http://192.168.42.129:8080/shot.jpg"

""" cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(3, 480)
cap.set(4, 360) """

screen_width = 1920
screen_height = 1080

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

dist = 0

mouse = Controller()

mouseOldLoc = np.array([0, 0])
mouseLoc = np.array([0, 0])
dampingFactor = 2

pressFlag = 0

while True:
    mouse.release(Button.left)
    """ ret, frame = cap.read() """
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    img = cv2.resize(img, (600, 360))
    frame = img
    
    
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.rectangle(frame, (10, 10), (20, 20), (0, 255, 0), -1)
    cv2.putText(frame, "Double Click", (30, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)

    cv2.rectangle(frame, (200, 10), (210, 20), (0, 0, 255), -1)
    cv2.putText(frame, "Click", (220, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)


    results = hands.process(frameRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape

                try:
                    if id == 4:
                        thumb_cx, thumb_cy = int(lm.x * w), int(lm.y * h)
                    if id == 8:
                        index_cx, index_cy = int(lm.x * w), int(lm.y * h)
                    if id == 20:
                        pinky_cx, pinky_cy = int(lm.x * w), int(lm.y * h)
                    if id == 13:
                        ring_end_cx, ring_end_cy = int(lm.x * w), int(lm.y * h)


                    cv2.circle(frame, (index_cx, index_cy), 2, (0, 0, 255), -1)
                    cv2.circle(frame, (pinky_cx, pinky_cy), 2, (0, 255, 0), -1)
                    cv2.circle(frame, (ring_end_cx, ring_end_cy), 2, (255, 0, 0), -1)


                    
                    center_thumb_index_x = int((thumb_cx + index_cx)/2)
                    center_thumb_index_y = int((thumb_cy + index_cy)/2)
                    

                    center_thumb_pinky_x = int((thumb_cx + pinky_cx)/2)
                    center_thumb_pinky_y = int((thumb_cy + pinky_cy)/2)

                    center_thumb_ring_end_x = int((thumb_cx + ring_end_cx)/2)
                    center_thumb_ring_end_y = int((thumb_cy + ring_end_cy)/2)
                    




                    dist_thumb_index = sqrt((thumb_cx - index_cx)**2 + (thumb_cy - index_cy)**2)
                    dist_thumb_mid = sqrt((thumb_cx - pinky_cx)**2 + (thumb_cy - pinky_cy)**2)
                    dist_thumb_ring_end = sqrt((thumb_cx - ring_end_cx)**2 + (thumb_cy - ring_end_cy)**2)

                    if dist_thumb_index < 30 and dist_thumb_index > 0:
                        print("Click")
                    elif dist_thumb_mid < 30 and dist_thumb_mid > 0:
                        print("Double Click")
                    elif dist_thumb_ring_end < 30 and dist_thumb_ring_end > 0:
                        print("Scroll Down")



                    mouseLoc = mouseOldLoc + ((center_x, center_y) - mouseOldLoc)/dampingFactor


                    mouse_x = int((mouseLoc[0] * screen_width / 600))
                    mouse_y = int((mouseLoc[1] * screen_height / 360))

                    mouse.position = (mouse_x, mouse_y)
                    mouseOldLoc = mouseLoc

                    


                    """ if dist < 30 and dist > 0:
                        if pressFlag == 0:
                            mouse.click(Button.left, 2)
                            cv2.putText(frame, "Double Click", (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
                            pressFlag = 1

                    elif dist > 30:
                        pressFlag = 0 """
                    
                    
                        
                    

                    
                    
                    

                except:
                    pass

    

    

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()