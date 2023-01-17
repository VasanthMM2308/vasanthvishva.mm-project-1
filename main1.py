from tkinter import*
import tkinter
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from time import strftime
from PIL import Image, ImageTk
import tkinter as tk
import os
from train import Train
from attedance import Attendance
from student import student
from help import HELP
from staff import Staff
from details import Detials
from face import Face



class face_Recognition_system:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title("S.A.ENGINEERING COLLEGE ")
       # bg image
       img = Image.open("image\\SABG.png")
       img= img.resize((1272, 650), Image.ANTIALIAS)
       self.photoimg = ImageTk.PhotoImage(img)

       bg_image = Label(self.root, image=self.photoimg)
       bg_image.place(x=0, y=0, width=1272, height=650)

       title_lb1 = Label(bg_image, text="FACE DETECTION ATTENDANCE BASED USING IN PYTHON", font=("time new roman", 25, "bold"), bg="green", fg="red")
       title_lb1.place(x=0, y=100, width=1280, height=45)

       # top front image
       img2 = Image.open("image\\SA3.png")
       img2 = img2.resize((517, 97), Image.ANTIALIAS)
       self.photoimg2 = ImageTk.PhotoImage(img2)

       b1 = Button(bg_image, image=self.photoimg2, cursor="hand2")
       b1.place(x=0, y=0, width=1272, height=100)
      #student button

       img4 = Image.open("image\\student.png")
       img4 = img4.resize((220, 220), Image.ANTIALIAS)
       self.photoimg4 = ImageTk.PhotoImage(img4)

       b1 = Button(bg_image, image=self.photoimg4,command=self.student_details, cursor="hand2")
       b1.place(x=50, y=150, width=190, height=190)
       b1 = Button(bg_image, text="student",command=self.student_details,
                font=("time new roman", 15, "bold"), bg="green", fg="red")
       b1.place(x=50, y=320, width=190, height=30)
       #face delection
       img5 = Image.open("image\\face3.png")
       img5 = img5.resize((220, 220), Image.ANTIALIAS)
       self.photoimg5 = ImageTk.PhotoImage(img5)

       b2 = Button(bg_image, image=self.photoimg5, cursor="hand2",command=self.face_data)
       b2.place(x=250, y=150, width=190, height=190)
       b2 = Button(bg_image, text="face detection",command=self.face_data,
                font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=250, y=320, width=190, height=30)
       # attendance
       img6 = Image.open("image\\attendance.png")
       img6 = img6.resize((220, 220), Image.ANTIALIAS)
       self.photoimg6 = ImageTk.PhotoImage(img6)

       b2 = Button(bg_image, image=self.photoimg6, cursor="hand2",command=self.Attendance_data)
       b2.place(x=450, y=150, width=190, height=190)
       b2 = Button(bg_image, text="Attendance", command=self.Attendance_data,
                   font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=450, y=320, width=190, height=30)
       # Help
       img7 = Image.open("image\\help.png")
       img7 = img7.resize((220, 220), Image.ANTIALIAS)
       self.photoimg7 = ImageTk.PhotoImage(img7)

       b2 = Button(bg_image, image=self.photoimg7, cursor="hand2",command=self.HELP_data)
       b2.place(x=650, y=150, width=190, height=190)
       b2 = Button(bg_image, text="Help",command=self.HELP_data,
                   font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=650, y=320, width=190, height=30)
       # Train face button
       img8 = Image.open("image\\face4.png")
       img8 = img8.resize((220, 220), Image.ANTIALIAS)
       self.photoimg8 = ImageTk.PhotoImage(img8)

       b2 = Button(bg_image, image=self.photoimg8, cursor="hand2",command=self.train_data)
       b2.place(x=850, y=150, width=190, height=190)
       b2 = Button(bg_image, text="TRAIN FACE", command=self.train_data,
                   font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=850, y=320, width=190, height=30)
       # photo image button
       img9= Image.open("image\\image.jpg")
       img9 = img9.resize((220, 220), Image.ANTIALIAS)
       self.photoimg9 = ImageTk.PhotoImage(img9)

       b2 = Button(bg_image, image=self.photoimg9, cursor="hand2", command=self.open_img)
       b2.place(x=1050, y=150, width=190, height=190)
       b2 = Button(bg_image, text="photo image", command=self.open_img,
                   font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=1050, y=320, width=190, height=30)
       # detail
       img10 = Image.open("image\\developer.jpg")
       img10 = img10.resize((220, 220), Image.ANTIALIAS)
       self.photoimg10 = ImageTk.PhotoImage(img10)

       b2 = Button(bg_image, image=self.photoimg10, cursor="hand2",command=self.Details_data)
       b2.place(x=50, y=355, width=190, height=190)
       b2 = Button(bg_image, text="Details",command=self.Details_data,
                   font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=50, y=520, width=190, height=30)
       #Teacher
       img13 = Image.open("image\\staff.png")
       img13 = img13.resize((220, 220), Image.ANTIALIAS)
       self.photoimg13 = ImageTk.PhotoImage(img13)

       b2 = Button(bg_image, image=self.photoimg13, cursor="hand2",command=self.Staff_data)
       b2.place(x=250, y=355, width=190, height=190)
       b2 = Button(bg_image, text="STAFF",command=self.Staff_data,
                   font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=250, y=520, width=190, height=30)
       # exit button
       img11 = Image.open("image\\exit.png")
       img11 = img11.resize((220, 220), Image.ANTIALIAS)
       self.photoimg11 = ImageTk.PhotoImage(img11)

       b2 = Button(bg_image, image=self.photoimg11, cursor="hand2",command=self.iExit)
       b2.place(x=450, y=355, width=190, height=190)
       b2 = Button(bg_image, text="EXIT",command=self.iExit,
                   font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=450, y=520, width=190, height=30)
     

    def open_img(self):
       os.startfile("data")

    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure Exit this project",parent=self.root)
       if self.iExit >0:
          self.root.destroy()
       else:
          return

     #function buttons
    def student_details(self):
       self.new_window = Toplevel(self.root)
       self.app=student(self.new_window)

    def train_data(self):
       self.new_window = Toplevel(self.root)
       self.app=Train(self.new_window)

    def face_data(self):
       self.new_window = Toplevel(self.root)
       self.app=Face(self.new_window)

    def Attendance_data(self):
       self.new_window = Toplevel(self.root)
       self.app=Attendance(self.new_window)

    def Staff_data(self):
       self.new_window = Toplevel(self.root)
       self.app=Staff(self.new_window)

    def HELP_data(self):
       self.new_window = Toplevel(self.root)
       self.app=HELP(self.new_window)

    def Details_data(self):
       self.new_window = Toplevel(self.root)
       self.app=Detials(self.new_window)

    







if __name__ == '__main__':
    root = tk.Tk()
    obj = face_Recognition_system(root)
    root.mainloop()



