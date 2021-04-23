from tkinter import *
from PIL import ImageTk

root = Tk()
root.title("Virtual Mouse")
root.geometry("600x300+500+200")
root.resizable(False, False)
bg = ImageTk.PhotoImage(file="./images/bg.jpg")
bg_image = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

title = Label(root, text="Use IP Webcam", font=("Arial", 20, "bold"), fg="black", bg="white").place(x=35, y=60)
ip_desc = Label(root, text="Enter IP Address", font=("Arial", 10, "bold"), fg="#303030", bg="white").place(x=38, y=100)
ip_address = Entry(root, font=("times new roman", 11), bg="lightgray")

ip_address.place(x=40, y=125, width=200, height=35)
ip_submit = Button(root, cursor="hand2", text="Start", fg="white", bg="#d77337",  font=("Arial", 20)).place(x=60, y=180, width=160, height=40)

title = Label(root, text="Use Webcam", font=("Arial", 20, "bold"), fg="black", bg="white").place(x=370, y=60)
web_submit = Button(root, cursor="hand2", text="Start", fg="white", bg="#d77337",  font=("Arial", 20)).place(x=380, y=180, width=160, height=40)

root.mainloop()