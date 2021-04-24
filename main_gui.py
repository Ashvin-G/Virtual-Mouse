from tkinter import *
from PIL import ImageTk
import cv2
import numpy as np
import mediapipe as mp
from math import sqrt
import urllib.request
from tkinter import messagebox



def ip_webcam():
    if ip_address.get() == "":
        messagebox.showerror("Error", "Enter IPv4 address")
    elif len(ip_address.get().split(".")) != 4:
        messagebox.showerror("Error", "Invalid IPv4 address")
    else:
        token = ip_address.get().split(".")
        token[3] = token[3].split(":")[0]
        
        if int(token[0]) > 0 and int(token[0]) <= 255 and int(token[1]) > 0 and int(token[1]) <= 255 and int(token[2]) > 0 and int(token[2]) <= 255 and int(token[3]) > 0 and int(token[3]) <= 255:
            from pynput.mouse import Button, Controller

            url = "http://"+ip_address.get()+"/shot.jpg"

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

            while True:
                imgResp = urllib.request.urlopen(url)
                imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
                img = cv2.imdecode(imgNp, -1)
                img = cv2.resize(img, (600, 360))
                frame = img
                frame = cv2.flip(frame, 1)

                frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                cv2.rectangle(frame, (10, 10), (20, 20), (0, 255, 255), -1)
                cv2.putText(frame, "Double Click", (25, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255), 1)

                cv2.rectangle(frame, (170, 10), (180, 20), (0, 255, 0), -1)
                cv2.putText(frame, "Click", (185, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 0), 1)

                cv2.rectangle(frame, (248, 10), (258, 20), (0, 0, 255), -1)
                cv2.putText(frame, "Scroll Down", (263, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1)

                cv2.rectangle(frame, (395, 10), (405, 20), (125, 0, 255), -1)
                cv2.putText(frame, "Scroll Up", (410, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (125, 0, 255), 1)

                cv2.rectangle(frame, (515, 10), (525, 20), (255, 255, 255), 1)
                cv2.putText(frame, "Cursor", (530, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255, 255, 255), 1)

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
                                if id == 12:
                                    mid_tip_cx, mid_tip_cy = int(lm.x * w), int(lm.y * h)
                                if id == 16:
                                    ring_tip_cx, ring_tip_cy = int(lm.x * w), int(lm.y * h)
                                

                                
                                cv2.circle(frame, (index_cx, index_cy), 5, (0, 255, 0), -1)
                                cv2.circle(frame, (mid_tip_cx, mid_tip_cy), 5, (0, 255, 255), -1)
                                cv2.circle(frame, (pinky_cx, pinky_cy), 5, (0, 0, 255), -1)
                                cv2.circle(frame, (ring_tip_cx, ring_tip_cy), 5, (125, 0, 255), -1)

                                center_thumb_index_x = int((thumb_cx + index_cx)/2)
                                center_thumb_index_y = int((thumb_cy + index_cy)/2)

                                cv2.circle(frame, (center_thumb_index_x, center_thumb_index_y), 4, (255, 255, 255), 1)

                                dist_thumb_index = sqrt((thumb_cx - index_cx)**2 + (thumb_cy - index_cy)**2)
                                dist_thumb_pinky = sqrt((thumb_cx - pinky_cx)**2 + (thumb_cy - pinky_cy)**2)
                                dist_thumb_mid = sqrt((thumb_cx - mid_tip_cx)**2 + (thumb_cy - mid_tip_cy)**2)
                                dist_thumb_ring = sqrt((thumb_cx - ring_tip_cx)**2 + (thumb_cy - ring_tip_cy)**2)

                                mouseLoc = mouseOldLoc + ((center_thumb_index_x, center_thumb_index_y) - mouseOldLoc)/dampingFactor

                                mouse_x = int((mouseLoc[0] * screen_width / 600))
                                mouse_y = int((mouseLoc[1] * screen_height / 360))

                                mouse.position = (mouse_x, mouse_y)
                                mouseOldLoc = mouseLoc

                                if dist_thumb_index > 0 and dist_thumb_index < 15:
                                    db_click_flag = 0
                                    scroll_down_flag = 0
                                    scroll_up_flag = 0
                                    cv2.putText(frame, "Click", (185, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 0), 2)
                                    mouse.click(Button.left, 1)

                                elif dist_thumb_mid > 0 and dist_thumb_mid < 15:
                                    if db_click_flag == 0:
                                        db_click_flag = 1
                                        cv2.putText(frame, "Double Click", (25, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255), 2)
                                        mouse.click(Button.left, 2)

                                elif dist_thumb_pinky > 0 and dist_thumb_pinky < 15:
                                    if scroll_down_flag == 0:
                                        db_click_flag = 0
                                        scroll_down_flag = 1
                                        cv2.putText(frame, "Scroll Down", (263, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 2)
                                        mouse.scroll(0, -2)

                                elif dist_thumb_ring > 0 and dist_thumb_ring < 15:
                                    if scroll_up_flag == 0:
                                        db_click_flag = 0
                                        scroll_up_flag = 1
                                        cv2.putText(frame, "Scroll Up", (410, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 2)
                                        mouse.scroll(0, 2)

                                
                            except:
                                pass


                cv2.imshow("Virtual Mouse", frame)

                if cv2.waitKey(1) == 27:
                    break
            cv2.destroyAllWindows()
        else:
            messagebox.showerror("Error", "Invalid IPv4 address")



def builtin_webcam():
    from pynput.mouse import Button, Controller

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cap.set(3, 480)
    cap.set(4, 360)

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

    while True:
        ret, frame = cap.read()

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.rectangle(frame, (10, 10), (20, 20), (0, 255, 255), -1)
        cv2.putText(frame, "Double Click", (25, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255), 1)

        cv2.rectangle(frame, (170, 10), (180, 20), (0, 255, 0), -1)
        cv2.putText(frame, "Click", (185, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 0), 1)

        cv2.rectangle(frame, (248, 10), (258, 20), (0, 0, 255), -1)
        cv2.putText(frame, "Scroll Down", (263, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1)

        cv2.rectangle(frame, (395, 10), (405, 20), (125, 0, 255), -1)
        cv2.putText(frame, "Scroll Up", (410, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (125, 0, 255), 1)

        cv2.rectangle(frame, (515, 10), (525, 20), (255, 255, 255), 1)
        cv2.putText(frame, "Cursor", (530, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255, 255, 255), 1)

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
                        if id == 12:
                            mid_tip_cx, mid_tip_cy = int(lm.x * w), int(lm.y * h)
                        if id == 16:
                            ring_tip_cx, ring_tip_cy = int(lm.x * w), int(lm.y * h)
                                

                                
                        cv2.circle(frame, (index_cx, index_cy), 5, (0, 255, 0), -1)
                        cv2.circle(frame, (mid_tip_cx, mid_tip_cy), 5, (0, 255, 255), -1)
                        cv2.circle(frame, (pinky_cx, pinky_cy), 5, (0, 0, 255), -1)
                        cv2.circle(frame, (ring_tip_cx, ring_tip_cy), 5, (125, 0, 255), -1)

                        center_thumb_index_x = int((thumb_cx + index_cx)/2)
                        center_thumb_index_y = int((thumb_cy + index_cy)/2)

                        cv2.circle(frame, (center_thumb_index_x, center_thumb_index_y), 4, (255, 255, 255), 1)

                        dist_thumb_index = sqrt((thumb_cx - index_cx)**2 + (thumb_cy - index_cy)**2)
                        dist_thumb_pinky = sqrt((thumb_cx - pinky_cx)**2 + (thumb_cy - pinky_cy)**2)
                        dist_thumb_mid = sqrt((thumb_cx - mid_tip_cx)**2 + (thumb_cy - mid_tip_cy)**2)
                        dist_thumb_ring = sqrt((thumb_cx - ring_tip_cx)**2 + (thumb_cy - ring_tip_cy)**2)

                        mouseLoc = mouseOldLoc + ((center_thumb_index_x, center_thumb_index_y) - mouseOldLoc)/dampingFactor

                        mouse_x = int((mouseLoc[0] * screen_width / 600))
                        mouse_y = int((mouseLoc[1] * screen_height / 360))

                        mouse.position = (mouse_x, mouse_y)
                        mouseOldLoc = mouseLoc

                        if dist_thumb_index > 0 and dist_thumb_index < 15:
                            db_click_flag = 0
                            scroll_down_flag = 0
                            scroll_up_flag = 0
                            cv2.putText(frame, "Click", (185, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 0), 2)
                            mouse.click(Button.left, 1)

                        elif dist_thumb_mid > 0 and dist_thumb_mid < 15:
                            if db_click_flag == 0:
                                db_click_flag = 1
                                cv2.putText(frame, "Double Click", (25, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255), 2)
                                mouse.click(Button.left, 2)

                        elif dist_thumb_pinky > 0 and dist_thumb_pinky < 15:
                            if scroll_down_flag == 0:
                                db_click_flag = 0
                                scroll_down_flag = 1
                                cv2.putText(frame, "Scroll Down", (263, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 2)
                                mouse.scroll(0, -2)

                        elif dist_thumb_ring > 0 and dist_thumb_ring < 15:
                            if scroll_up_flag == 0:
                                db_click_flag = 0
                                scroll_up_flag = 1
                                cv2.putText(frame, "Scroll Up", (410, 22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 2)
                                mouse.scroll(0, 2)

                    except:
                        pass


        cv2.imshow("Virtual Mouse", frame)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


root = Tk()
root.iconbitmap("./images/icon.ico")
root.title("Virtual Mouse")

def myfunc():
    help_img = cv2.imread("./images/help.jpg")
    help_img = cv2.resize(help_img, (600, 300))
    cv2.imshow("Help", help_img)

mymenu = Menu(root)
mymenu.add_command(label="Help", command=myfunc)
root.config(menu=mymenu)


root.geometry("600x300+500+200")
root.resizable(False, False)
bg = ImageTk.PhotoImage(file="./images/bg.jpg")
bg_image = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

title_ip = Label(root, text="Use IP Webcam", font=("Arial", 20, "bold"), fg="black", bg="white").place(x=35, y=60)
ip_desc = Label(root, text="Enter IP Address", font=("Arial", 10, "bold"), fg="#303030", bg="white").place(x=38, y=100)
ip_address = Entry(root, font=("times new roman", 11), bg="lightgray")

ip_address.place(x=40, y=125, width=200, height=35)
ip_submit = Button(root, command = ip_webcam, cursor="hand2", text="Start", fg="white", bg="#d77337",  font=("Arial", 20)).place(x=60, y=180, width=160, height=40)

title_webcam = Label(root, text="Use Webcam", font=("Arial", 20, "bold"), fg="black", bg="white").place(x=370, y=60)
web_submit = Button(root, command = builtin_webcam, cursor="hand2", text="Start", fg="white", bg="#d77337",  font=("Arial", 20)).place(x=380, y=180, width=160, height=40)

root.mainloop()