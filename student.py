from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title("face Recognition system")
       #=======variables=====
       self.var_dep = StringVar()
       self.var_course = StringVar()
       self.var_Year = StringVar()
       self.var_semester = StringVar()
       self.var_ID = StringVar()
       self.var_name = StringVar()
       self.var_div = StringVar()
       self.var_Roll = StringVar()
       self.var_Gender = StringVar()
       self.var_dob = StringVar()
       self.var_Email = StringVar()
       self.var_Phone = StringVar()
       self.var_address = StringVar()
       self.var_Teacher = StringVar()
       self.var_Radiobutton1 = StringVar()
       self.var_Radiobutton2 = StringVar()



       #first image
       img = Image.open("image\\student.png")
       img = img.resize((1272, 650), Image.ANTIALIAS)
       self.photoimg = ImageTk.PhotoImage(img)

       bg_image = Label(self.root, image=self.photoimg)
       bg_image.place(x=0, y=0, width=1272, height=650)
       title_lb1 = Label(bg_image, text="STUDENT MANAGEMENT SYSTEM",
                         font=("time new roman", 25, "bold"), bg="green", fg="red")
       title_lb1.place(x=0, y=0, width=1280, height=45)

       main_frame=Frame(bg_image, bd=2, bg="yellow")
       main_frame.place(x=0, y=90, width=1272, height=600)

       #left label frame
       Left_frame = LabelFrame(main_frame, bd=2, bg="green", relief=RIDGE, text="Student Details",
                               font=("time new roman", 12, "bold"))
       Left_frame.place(x=20, y=10, width=590, height=535)

       img2_Left = Image.open("image\\SA3.png")
       img2_Left = img2_Left.resize((517, 97), Image.ANTIALIAS)
       self.photoimg2_Left = ImageTk.PhotoImage(img2_Left)
       b1 = Label(Left_frame, image=self.photoimg2_Left, cursor="hand2")
       b1.place(x=0, y=0, width=590, height=100)

       # current course
       current_course_frame = LabelFrame(Left_frame, bd=2, bg="green", relief=RIDGE, text="Current course information ",
                               font=("time new roman", 12, "bold"))
       current_course_frame.place(x=5, y=100, width=590, height=150)
       #department
       dep_Label=Label(current_course_frame, text="Department", font=("time new roman", 12, "bold"), bg="blue", width=0)
       dep_Label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

       dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("time new roman", 12, "bold"),
                                state="read only", width=16)
       dep_combo["values"] = ("Select Department", "CSE", "IT", "ECE", "EEE", "MECH", "CIVIL")
       dep_combo.current(0)
       dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

       # course
       course_Label = Label(current_course_frame, text="Course", font=("time new roman", 13, "bold"), bg="blue",
                            width=0)
       course_Label.grid(row=0, column=2, padx=2, pady=10, sticky=W)

       course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course ,
                                   font=("time new roman", 13, "bold"), state="read only", width=16)
       course_combo["values"] = ("Select Course", "BE", "ME", "PHD", "MAC")
       course_combo.current(0)
       course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

       # year
       year_Label = Label(current_course_frame, text="Year", font=("time new roman", 13, "bold"), bg="blue", width=0)
       year_Label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

       year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Year ,font=("time new roman", 13, "bold"),
                                 state="read only", width=16)
       year_combo["values"] = ("Select Year", "2011-2015", "2015-2019", "2019-2023", "2023-2027", "2027-2031")
       year_combo.current(0)
       year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

       #SEMESTER
       semester_Label = Label(current_course_frame, text="Semester", font=("time new roman", 12, "bold"), bg="blue",
                              width=0)
       semester_Label.grid(row=1, column=2, padx=2, pady=10, sticky=W)

       semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,
                                     font=("time new roman", 12, "bold"), state="read only", width=16)
       semester_combo["values"] = ("Select Semester", "SEMESTER 1", "SEMESTER 2", "SEMESTER 3", "SEMESTER 4",
                                   "SEMESTER 5", "SEMESTER 6", "SEMESTER 7", "SEMESTER 8")
       semester_combo.current(0)
       semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

       # Class student information
       Class_Student_frame = LabelFrame(Left_frame, bd=2, bg="green", relief=RIDGE, text="Class Student information ",
                                        font=("time new roman", 12, "bold"))
       Class_Student_frame.place(x=5, y=200, width=590, height=300)
       # student id
       ID_Label = Label(Class_Student_frame, text="Student ID: ", font=("time new roman", 12, "bold"), bg="blue",
                        width=0)
       ID_Label.grid(row=0, column=0, padx=10, sticky=W)
       ID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_ID, width=14, font=("time new roman", 12, "bold"))
       ID_entry.grid(row=0, column=1, padx=10, sticky=W)
       # student name
       name_Label = Label(Class_Student_frame, text="Student Name:", font=("time new roman", 12, "bold"), bg="blue",
                                width=0)
       name_Label.grid(row=0, column=2, padx=10,pady=5, sticky=W)
       name_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_name, width=14,
                              font=("time new roman", 12, "bold"))
       name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
       # Class division
       div_Label = Label(Class_Student_frame, text="Class Division:", font=("time new roman", 12, "bold"),
                         bg="blue", width=0)
       div_Label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

       div_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_div, font=("time new roman", 13, "bold"),
                                 state="read only", width=12)
       div_combo["values"] = ("Select Division","A", "B", "C", "D", "E")
       div_combo.current(0)
       div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

       # Roll no
       Roll_Label = Label(Class_Student_frame, text="Roll No:", font=("time new roman", 12, "bold"),
                          bg="blue", width=0)
       Roll_Label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
       Roll_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_Roll, width=14,
                              font=("time new roman", 12, "bold"))
       Roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
       # gender
       Gender_Label = Label(Class_Student_frame, text="Gender:", font=("time new roman", 12, "bold"),
                                  bg="blue",
                                  width=0)
       Gender_Label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

       Gender_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_Gender, font=("time new roman", 13, "bold"),
                                state="read only", width=12)
       Gender_combo["values"] = ("Male", "Female", "Other")
       Gender_combo.current(0)
       Gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

       # DOB
       dob_Label = Label(Class_Student_frame, text="DOB:", font=("time new roman", 12, "bold"),
                                  bg="blue",
                                  width=0)
       dob_Label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
       dob_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_dob,width=14,
                             font=("time new roman", 12, "bold"))
       dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
       # Email
       Email_Label = Label(Class_Student_frame, text="Email:", font=("time new roman", 12, "bold"),
                                  bg="blue",
                                  width=0)
       Email_Label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
       Email_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_Email,width=14,
                               font=("time new roman", 12, "bold"))
       Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
       # phone no
       Phone_Label = Label(Class_Student_frame, text="Phone No:", font=("time new roman", 12, "bold"),
                                  bg="blue",
                                  width=0)
       Phone_Label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
       Phone_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_Phone, width=14,
                               font=("time new roman", 12, "bold"))
       Phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
       # address
       address_Label = Label(Class_Student_frame, text="Address:", font=("time new roman", 12, "bold"),
                                  bg="blue",
                                  width=0)
       address_Label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
       address_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_address,width=14,
                                 font=("time new roman", 12, "bold"))
       address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
       # teacher name
       Teacher_Label = Label(Class_Student_frame, text="Teacher Name:", font=("time new roman", 12, "bold"),
                                  bg="blue",
                                  width=0)
       Teacher_Label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
       Teacher_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_Teacher, width=14,
                                 font=("time new roman", 12, "bold"))
       Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
       #radio buttons
       Radiobutton1= ttk.Radiobutton(Class_Student_frame,variable=self.var_Radiobutton1,
                                     text="Take Photos Sample",value="Yes")
       Radiobutton1.grid(row=6, column=0)
       Radiobutton2 = ttk.Radiobutton(Class_Student_frame,variable=self.var_Radiobutton1,
                                      text="No Photos Sample", value="No")
       Radiobutton2.grid(row=6, column=1)
       # button frame
       btn_Frame= Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
       btn_Frame.place(x=0, y=200, width=715, height=70)

       update_btn=Button(btn_Frame, text="Update",command=self.update_data,width=13,font=("time new roman", 12, "bold"), bg="blue", fg="white")
       update_btn.grid(row=0, column=0)

       delete_btn = Button(btn_Frame, text="Delete",command=self.delete_data, width=13, font=("time new roman", 12, "bold"), bg="blue",
                           fg="white")
       delete_btn.grid(row=0, column=1)

       reset_btn = Button(btn_Frame, text="Reset",command=self.reset_data, width=13, font=("time new roman", 12, "bold"), bg="blue", fg="white")
       reset_btn.grid(row=0, column=2)

       save_btn = Button(btn_Frame, text="Save",command=self.add_data,width=15, font=("time new roman", 12, "bold"),
                         bg="blue", fg="white")
       save_btn.grid(row=0, column=3)

       btn_Frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
       btn_Frame1.place(x=0, y=235, width=710, height=70)

       take_photos_btn = Button(btn_Frame1, command=self.generate_dataset,text="Take Photos Sample ",width=17, font=("time new roman", 12, "bold"),
                                bg="blue", fg="white")
       take_photos_btn.grid(row=0, column=0)
       update_photos_btn = Button(btn_Frame1, command=self.generate_dataset,text="update Photos Sample ", width=18,
                                  font=("time new roman", 12, "bold"), bg="blue", fg="white")
       update_photos_btn.grid(row=0, column=1)

       # right label frame
       Right_frame = LabelFrame(main_frame, bd=2, bg="green", relief=RIDGE, text="Student Details",
                                font=("time new roman", 12, "bold"))
       Right_frame.place(x=620, y=10, width=620, height=535)

       img3_Right = Image.open("image\\SA3.png")
       img3_Right = img3_Right.resize((517, 97), Image.ANTIALIAS)
       self.photoimg3_Right = ImageTk.PhotoImage(img3_Right)
       b1 = Label(Right_frame, image=self.photoimg3_Right, cursor="hand2")
       b1.place(x=0, y=0, width=590, height=100)


       #========serach System========

       Serach_frame = LabelFrame(Right_frame, bd=2, bg="green", relief=RIDGE, text="Serach System",
                                        font=("time new roman", 12, "bold"))
       Serach_frame.place(x=5, y=100, width=590, height=100)

       Serach_Label = Label(Serach_frame, text="Serach By:", font=("time new roman", 15, "bold"),
                              bg="red",fg="white",
                              width=0)
       Serach_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

       self.search_var=StringVar()
       Serach_combo = ttk.Combobox(Serach_frame, textvariable=self.search_var,font=("time new roman", 13, "bold"), state="read only", width=16)
       Serach_combo["values"] = ("Select ", "Roll", "Phone","Student Id")
       Serach_combo.current(0)
       Serach_combo.grid(row=0, column=1,  pady=5, sticky=W)

       self.txt_search=StringVar()
       Search_entry = ttk.Entry(Serach_frame,textvariable=self.txt_search, width=15, font=("time new roman", 12, "bold"))
       Search_entry.grid(row=0, column=2, pady=5, sticky=W)

       Serach_btn = Button(Serach_frame,command=self.f_data,text="Search", width=13, font=("time new roman", 10, "bold"), bg="blue",
                           fg="white")
       Serach_btn.grid(row=1, column=0)

       ShowAll_btn = Button(Serach_frame, command=self.fetch_data,text="Show All", width=13, font=("time new roman", 10, "bold"), bg="blue",
                            fg="white")
       ShowAll_btn.grid(row=1, column=1, padx=2)
       # table frame
       table_frame =Frame(Right_frame, bd=2, bg="green", relief=RIDGE)
       table_frame.place(x=5, y=205, width=590, height=300)

       scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

       self.student_table=ttk.Treeview(table_frame, columns=("dep", "course", "year", "semester", "ID", "name", "div",
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
       self.student_table["show"]="headings"

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
       self.student_table.bind("<ButtonRelease>", self.get_cursor)
       self.fetch_data()

                                   #======FUNCTION DECRATION=====
    def add_data(self):

       if (self.var_dep.get()=="" or self.var_name.get()=="" or self.var_ID.get()==""):
             messagebox.showerror("Error", "All Fields are required",parent=self.root)
       else:
          try:
             conn= mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                           database="face_recognition")
             my_cursor =conn.cursor()
             my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                         self.var_dep.get(),
                         self.var_course.get(),
                         self.var_Year.get(),
                         self.var_semester.get(),
                         self.var_ID.get(),
                         self.var_name.get(),
                         self.var_div.get(),
                         self.var_Roll.get(),
                         self.var_Gender.get(),
                         self.var_dob.get(),
                         self.var_Email.get(),
                         self.var_Phone.get(),
                         self.var_Teacher.get(),
                         self.var_address.get(),
                         self.var_Radiobutton1.get()
                                          ))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
          except Exception as es:
             messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

             #_____fetch data___
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
            #=======get cursor======
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_Roll.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_Teacher.set(data[12]),
        self.var_address.set(data[13]),
        self.var_Radiobutton1.set(data[14])

 #updata function
    def update_data(self):
        if (self.var_dep.get() == "" or self.var_name.get() == "" or self.var_ID.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Are You want to update this student details", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set  Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s,Division=%s,"
                                      "Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Teacher=%s,Address=%s, "
                                      "PhotoSample=%s where Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_Year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_Roll.get(),
                        self.var_Gender.get(),
                        self.var_dob.get(),
                        self.var_Email.get(),
                        self.var_Phone.get(),
                        self.var_Teacher.get(),
                        self.var_address.get(),
                        self.var_Radiobutton1.get(),
                        self.var_ID.get()
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully update completed", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)
          # delete function
    def delete_data(self):
        if self.var_ID.get=="":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete= messagebox.askyesno("Student delete page","Do You want to delete this Student",
                                            parent= self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)
           #reset functiom
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_ID.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_Roll.set("")
        self.var_Gender.set("Male")
        self.var_dob.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Teacher.set("")
        self.var_address.set("")
        self.var_Radiobutton1.set("")
# Take Photos Samples or generate data
    def generate_dataset(self):
        if (self.var_dep.get() == "" or self.var_name.get() == "" or self.var_ID.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                   database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set  Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s,Division=%s,"
                              "Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Teacher=%s,Address=%s, "
                              "PhotoSample=%s where Student_id=%s", (
                                  self.var_dep.get(),
                                  self.var_course.get(),
                                  self.var_Year.get(),
                                  self.var_semester.get(),
                                  self.var_name.get(),
                                  self.var_div.get(),
                                  self.var_Roll.get(),
                                  self.var_Gender.get(),
                                  self.var_dob.get(),
                                  self.var_Email.get(),
                                  self.var_Phone.get(),
                                  self.var_address.get(),
                                  self.var_Teacher.get(),
                                  self.var_Radiobutton1.get(),
                                  self.var_ID.get()==id+1
                                                           ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #face open================================
                faceCascade = cv2.CascadeClassifier("C:\\Users\\SENTHIL RK\\python\\Lib\\"
                                                    "site-packages\\cv2\\data\\"
                                                    "haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                   ret, my_frame = cap.read()
                   if face_cropped(my_frame) is not None:
                       img_id+=1
                       face=cv2.resize(face_cropped(my_frame),(450,450))
                       face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                       file_name_path="data/student_data/user"+str(id)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name_path, face)
                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,225,0),2)
                       cv2.imshow("Crooped Face", face)
                   if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets compeled!!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)

           #search data
    def f_data(self):
        if self.search_var.get()=="" or self.txt_search.get()=="":
            messagebox.showerror("Error", "Please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student"+str(self.var_name.get())+"LIKES '%"+str(self.txt_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)









if __name__ == '__main__':
    root = tk.Tk()
    obj = student(root)
    root.mainloop()