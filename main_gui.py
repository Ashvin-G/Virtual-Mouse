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
            url = "http://"+ip_address.get()+"/shot.jpg"
            while True:
                imgResp = urllib.request.urlopen(url)
                imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
                img = cv2.imdecode(imgNp, -1)
                img = cv2.resize(img, (600, 360))
                frame = img

                cv2.imshow("frame", frame)

                if cv2.waitKey(1) == 27:
                    break
            cv2.destroyAllWindows()
        else:
            messagebox.showerror("Error", "Invalid IPv4 address")



def builtin_webcam():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        ret, frame = cap.read()

        cv2.imshow("frame", frame)
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