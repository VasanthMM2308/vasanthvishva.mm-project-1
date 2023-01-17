from tkinter import*
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Train:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title("face Recognition system")

       title_lb1 = Label(self.root, text="Train DATA SET",
                         font=("time new roman", 25, "bold"), bg="WHITE", fg="red")
       title_lb1.place(x=0, y=0, width=1280, height=45)
       # image
       img_Top = Image.open(r"image\\allface.png")
       img_Top = img_Top.resize((1272, 650), Image.ANTIALIAS)
       self.photoimg_Top = ImageTk.PhotoImage(img_Top)
       b1 = Label(self.root, image=self.photoimg_Top, cursor="hand2")
       b1.place(x=0, y=55, width=1272, height=650)

       # button
       b1 = Button(self.root, text="STUDENT TRAIN  DATA ",command=self.Student_train_classifier,
                   font=("time new roman", 15, "bold"), bg="darkgreen", fg="red",)
       b1.place(x=520, y=300, width=280, height=40)
       b2 = Button(self.root, text="STAFF TRAIN  DATA ", command=self.Staff_train_classifier,
                   font=("time new roman", 15, "bold"), bg="green", fg="red")
       b2.place(x=520, y=200, width=280, height=40)
    def Student_train_classifier(self):
        data_dir=("data/student_data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path :
            img=Image.open(image).convert('L')
            imageNp= np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #======Train the classifier And save======
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Student_classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training datasets completed!!")

    def Staff_train_classifier(self):
        data_dir=("data/staff_data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path :
            img=Image.open(image).convert('L')
            imageNp= np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #======Train the classifier And save======
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Staff_classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training datasets completed!!")



if __name__ == '__main__':
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()