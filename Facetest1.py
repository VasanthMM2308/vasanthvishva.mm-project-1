from tkinter import*
from tkinter import ttk
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os



class Face:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title("face Recognition system")

       title_lb1 = Label(self.root, text="FACE RECOGNITION",
                         font=("time new roman", 25, "bold"), bg="WHITE", fg="green")
       title_lb1.place(x=0, y=0, width=1280, height=45)
       # image
       img_Top = Image.open(r"image\\face_detection.png")
       img_Top = img_Top.resize((650, 700), Image.ANTIALIAS)
       self.photoimg_Top = ImageTk.PhotoImage(img_Top)
       b1 = Label(self.root, image=self.photoimg_Top, cursor="hand2")
       b1.place(x=0, y=55, width=500, height=550)
       # image 2
       img2_Top = Image.open(r"image\\face1.png")
       img2_Top = img2_Top.resize((900, 700), Image.ANTIALIAS)
       self.photoimg2_Top = ImageTk.PhotoImage(img2_Top)
       b2 = Label(self.root, image=self.photoimg2_Top, cursor="hand2")
       b2.place(x=500, y=55, width=900, height=550)

       # button
       b1 = Button(b2, text="Student Face Recognition",command=self.student_face_recog,
                   font=("time new roman", 15, "bold"), bg="darkgreen", fg="blue")
       b1.place(x=420, y=500, width=280, height=40)

         #face recognition

    def student_face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                               database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = str(n)


                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = str(r)


                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = str(r)

                




                if confidence > 77:

                   
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 3)
                   
                  

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Student_classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret , img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()

       

     
      




if __name__ == '__main__':
    root = tk.Tk()
    obj = Face(root)
    root.mainloop()
