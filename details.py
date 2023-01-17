from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

class Detials:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title("DETAILS SYSTEM")

       # first image
       img = Image.open("image\\sabg.jpg")
       img = img.resize((1272, 650), Image.ANTIALIAS)
       self.photoimg = ImageTk.PhotoImage(img)

       bg_image = Label(self.root, image=self.photoimg)
       bg_image.place(x=0, y=0, width=1272, height=650)
       title_lb1 = Label(bg_image, text="DETAILS",
                         font=("time new roman", 25, "bold"), bg="green", fg="red")
       title_lb1.place(x=0, y=0, width=1280, height=45)

       main_frame = Frame(bg_image, bd=2, bg="white")
       main_frame.place(x=0, y=90, width=1272, height=600)

       # left label frame
       Left_frame = LabelFrame(main_frame, bd=2, bg="WHITE", relief=RIDGE, text="Staff Details",
                               font=("time new roman", 12, "bold"))
       Left_frame.place(x=20, y=10, width=590, height=535)

       img2_Left = Image.open("image\\SA3.png")
       img2_Left = img2_Left.resize((517, 97), Image.ANTIALIAS)
       self.photoimg2_Left = ImageTk.PhotoImage(img2_Left)
       b1 = Label(Left_frame, image=self.photoimg2_Left, cursor="hand2")
       b1.place(x=30, y=10, width=520, height=100)
       Serach_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Serach System",
                                 font=("time new roman", 12, "bold"))
       Serach_frame.place(x=5, y=100, width=590, height=100)

       Serach_Label = Label(Serach_frame, text="Search By:", font=("time new roman", 15, "bold"),
                            bg="red", fg="white",
                            width=0)
       Serach_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

       Serach_combo = ttk.Combobox(Serach_frame,  font=("time new roman", 13, "bold"),
                                   state="read only", width=16)
       Serach_combo["values"] = ("Select ", "Roll No", "Phone No",)
       Serach_combo.current(0)
       Serach_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

       Serach_entry = ttk.Entry(Serach_frame,  width=15,
                                font=("time new roman", 12, "bold"))
       Serach_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

       Serach_btn = Button(Serach_frame, text="Search", width=13,
                           font=("time new roman", 10, "bold"), bg="blue",
                           fg="white")
       Serach_btn.grid(row=1, column=0)

       ShowAll_btn = Button(Serach_frame, command=self.Staff_data,text="Show All", width=13,
                            font=("time new roman", 10, "bold"), bg="blue",
                            fg="white")
       ShowAll_btn.grid(row=1, column=1, padx=2)
       # table frame
       table_frame = Frame(Left_frame, bd=2, bg="green", relief=RIDGE)
       table_frame.place(x=5, y=205, width=590, height=300)

       scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

       self.staff_table = ttk.Treeview(table_frame, columns=("name", "Emp_Id", "dep", "Bloods_Group", "Gender", "dob",
                                                             "Email", "Phone", "Phone_no", "address", "Father",
                                                             "photo"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)

       scroll_x.config(command=self.staff_table.xview)
       scroll_y.config(command=self.staff_table.yview)

       self.staff_table.heading("name", text="Staff Name")
       self.staff_table.heading("Emp_Id", text="Emp ID No")
       self.staff_table.heading("dep", text="Department")
       self.staff_table.heading("Bloods_Group", text="Bloods Group")
       self.staff_table.heading("Gender", text="Gender")
       self.staff_table.heading("dob", text="DOB")
       self.staff_table.heading("Email", text="Email")
       self.staff_table.heading("Phone", text="Phone No")
       self.staff_table.heading("Phone_no", text="Phone No2")
       self.staff_table.heading("address", text="Address")
       self.staff_table.heading("Father", text="Father Name")
       self.staff_table.heading("photo", text="PhotoSampleStatus")
       self.staff_table["show"] = "headings"

       self.staff_table.column("name", width=100)
       self.staff_table.column("Emp_Id", width=100)
       self.staff_table.column("dep", width=100)
       self.staff_table.column("Bloods_Group", width=100)
       self.staff_table.column("Gender", width=100)
       self.staff_table.column("dob", width=100)
       self.staff_table.column("Email", width=100)
       self.staff_table.column("Phone", width=100)
       self.staff_table.column("Phone_no", width=100)
       self.staff_table.column("address", width=100)
       self.staff_table.column("Father", width=100)
       self.staff_table.column("photo", width=150)
       self.staff_table.pack(fill=BOTH, expand=1)
       self.Staff_data()











       # right label frame
       Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("time new roman", 12, "bold"))
       Right_frame.place(x=630, y=10, width=620, height=535)

       img3_Right = Image.open("image\\SA3.png")
       img3_Right = img3_Right.resize((517, 97), Image.ANTIALIAS)
       self.photoimg3_Right = ImageTk.PhotoImage(img3_Right)
       b1 = Label(Right_frame, image=self.photoimg3_Right, cursor="hand2")
       b1.place(x=14, y=0, width=590, height=100)
       # ========serach System========

       Serach_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Serach System",
                                 font=("time new roman", 12, "bold"))
       Serach_frame.place(x=5, y=100, width=590, height=100)

       Serach_Label = Label(Serach_frame, text="Serach By:", font=("time new roman", 15, "bold"),
                            bg="red", fg="white",
                            width=0)
       Serach_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)


       Serach_combo = ttk.Combobox(Serach_frame,  font=("time new roman", 13, "bold"),
                                   state="read only", width=16)
       Serach_combo["values"] = ("Select ", "Roll No", "Phone No", "Student Id")
       Serach_combo.current(0)
       Serach_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


       Serach_entry = ttk.Entry(Serach_frame,  width=15,
                                font=("time new roman", 12, "bold"))
       Serach_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

       Serach_btn = Button(Serach_frame,  text="Search", width=13,
                           font=("time new roman", 10, "bold"), bg="blue",
                           fg="white")
       Serach_btn.grid(row=1, column=0)

       ShowAll_btn = Button(Serach_frame, command=self.fetch_data ,text="Show All", width=13,
                            font=("time new roman", 10, "bold"), bg="blue",
                            fg="white")
       ShowAll_btn.grid(row=1, column=1, padx=2)
       # table frame
       table_frame = Frame(Right_frame, bd=2, bg="green", relief=RIDGE)
       table_frame.place(x=5, y=205, width=590, height=300)

       scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

       self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "semester", "ID", "name", "div",
                                                               "Roll", "Gender", "dob", "Email", "Phone",
                                                               "Teacher", "address", "photo"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)

       scroll_x.config(command=self.student_table.xview)
       scroll_y.config(command=self.student_table.yview)

       self.student_table.heading("dep", text="Department")
       self.student_table.heading("course", text="Course")
       self.student_table.heading("year", text="Year")
       self.student_table.heading("semester", text="Semester")
       self.student_table.heading("ID", text="Student ID")
       self.student_table.heading("name", text="Name")
       self.student_table.heading("div", text="Division")
       self.student_table.heading("Roll", text="Roll NO")
       self.student_table.heading("Gender", text="Gender")
       self.student_table.heading("dob", text="DOB")
       self.student_table.heading("Email", text="Email")
       self.student_table.heading("Phone", text="Phone No")
       self.student_table.heading("address", text="Address")
       self.student_table.heading("Teacher", text="Teacher Name")
       self.student_table.heading("photo", text="PhotoSampleStatus")
       self.student_table["show"] = "headings"

       self.student_table.column("dep", width=100)
       self.student_table.column("course", width=100)
       self.student_table.column("year", width=100)
       self.student_table.column("semester", width=100)
       self.student_table.column("ID", width=100)
       self.student_table.column("name", width=100)
       self.student_table.column("div", width=100)
       self.student_table.column("Roll", width=100)
       self.student_table.column("Gender", width=100)
       self.student_table.column("dob", width=100)
       self.student_table.column("Email", width=100)
       self.student_table.column("Phone", width=100)
       self.student_table.column("address", width=100)
       self.student_table.column("Teacher", width=100)
       self.student_table.column("photo", width=150)

       self.student_table.pack(fill=BOTH, expand=1)
       self.fetch_data()

    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                           database="face_recognition")
        my_cursor =conn.cursor()
        my_cursor.execute("Select *  From student")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def Staff_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                       database="staff")
        my_cursor = conn.cursor()
        my_cursor.execute("Select *  From staff")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.staff_table.delete(*self.staff_table.get_children())
            for i in data:
                self.staff_table.insert("", END, values=i)
            conn.commit()
        conn.close()






if __name__ == '__main__':
    root = tk.Tk()
    obj = Detials(root)
    root.mainloop()