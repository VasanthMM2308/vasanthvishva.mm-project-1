from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox


class HELP:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title(" HELP ")

       img_Top = Image.open(r"image\\sabg.jpg")
       img_Top = img_Top.resize((1272, 650), Image.ANTIALIAS)
       self.photoimg_Top = ImageTk.PhotoImage(img_Top)
       b1 = Label(self.root, image=self.photoimg_Top, cursor="hand2")
       b1.place(x=0, y=0, width=1272, height=650)

       title_lb1 = Label(b1, text="COLLEGE HELP",
                         font=("time new roman", 25, "bold"), bg="green", fg="red")
       title_lb1.place(x=0, y=0, width=1280, height=45)



       HELP_frame = LabelFrame(b1,  bg="white",
                                font=("time new roman", 12, "bold"))
       HELP_frame.place(x=450, y=120, width=400, height=400)

       Office_Label = Label(HELP_frame, text="Office Of The Controller", font=("time new roman", 12, "bold"), bg="white",
                          fg="Red",width=0)
       Office_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

       College_Label = Label(HELP_frame, text="S A ENGINEERING COLLEGE", font=("time new roman", 12, "bold"), bg="white",
                         fg="green", width=0)
       College_Label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

       Address_Label = Label(HELP_frame, text="Poonamallee - Avadi Main Road, Thiruverkadu,", font=("time new roman", 12, "bold"), bg="white",
                          fg="orange",width=0)
       Address_Label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

       Address_Label = Label(HELP_frame, text="Chennai - 600077",
                             font=("time new roman", 12, "bold"), bg="white",
                             fg="orange",width=0)
       Address_Label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

       Phone_Label = Label(HELP_frame, text="Phone :044-26801999", font=("time new roman", 12, "bold"), bg="white",
                          fg="Blue",width=0)
       Phone_Label.grid(row=4, column=0, padx=10, pady=5, sticky=W)


       Email_Label = Label(HELP_frame, text="Email : coe@saec.ac.in", font=("time new roman", 12, "bold"), bg="white",
                           fg="Blue",width=0)
       Email_Label.grid(row=5, column=0, padx=10, pady=5, sticky=W)

       Website_Label = Label(HELP_frame, text="Website : www.saec.ac.in", font=("time new roman", 12, "bold"), bg="white",
                           fg="Blue",width=0)
       Website_Label.grid(row=6, column=0, padx=10, pady=5, sticky=W)

       img_College = Image.open(r"image\\Email1.png")
       img_College = img_College.resize((200, 100), Image.ANTIALIAS)
       self.photoimg_College = ImageTk.PhotoImage(img_College)
       b1 = Label(HELP_frame, image=self.photoimg_College, cursor="hand2")
       b1.place(x=180, y=260, width=200, height=100)


if __name__ == '__main__':
    root = tk.Tk()
    obj = HELP(root)
    root.mainloop()