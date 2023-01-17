from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2



class Staff:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title("STAFF SYSTEM")
       # =======variables=====
       self.var_name = StringVar()
       self.var_Emp_Id = StringVar()
       self.var_dep = StringVar()
       self.var_Bloods_Group = StringVar()
       self.var_Gender = StringVar()
       self.var_dob = StringVar()
       self.var_Email = StringVar()
       self.var_Phone = StringVar()
       self.var_Phone_no = StringVar()
       self.var_address = StringVar()
       self.var_Father= StringVar()
       self.var_Radiobutton1 = StringVar()
       self.var_Radiobutton2 = StringVar()

       # first image
       img = Image.open("image\\sabg.jpg")
       img = img.resize((1272, 650), Image.ANTIALIAS)
       self.photoimg = ImageTk.PhotoImage(img)

       bg_image = Label(self.root, image=self.photoimg)
       bg_image.place(x=0, y=0, width=1272, height=650)
       title_lb1 = Label(bg_image, text="STAFF DETAIL",
                         font=("time new roman", 25, "bold"), bg="green", fg="red")
       title_lb1.place(x=0, y=0, width=1280, height=45)

       main_frame = Frame(bg_image, bd=2, bg="white")
       main_frame.place(x=0, y=90, width=1272, height=600)

       # left label frame
       Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Staff Details",
                               font=("time new roman", 12, "bold"))
       Left_frame.place(x=10, y=10, width=590, height=535)

       img2_Left = Image.open("image\\SA3.png")
       img2_Left = img2_Left.resize((517, 97), Image.ANTIALIAS)
       self.photoimg2_Left = ImageTk.PhotoImage(img2_Left)
       b1 = Label(Left_frame, image=self.photoimg2_Left, cursor="hand2")
       b1.place(x=0, y=0, width=590, height=100)

       # current course
       current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information ",
                                         font=("time new roman", 12, "bold"))
       current_course_frame.place(x=5, y=100, width=590, height=410)

       # staff name
       name_Label = Label(current_course_frame, text="Staff Name:", font=("time new roman", 12, "bold"), bg="white",
                          width=0)
       name_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
       name_entry = ttk.Entry(current_course_frame, textvariable=self.var_name, width=14,
                              font=("time new roman", 12, "bold"))
       name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

       # Emp_id_no
       Emp_ID_Label = Label(current_course_frame, text="EMP_ID_No: ", font=("time new roman", 12, "bold"), bg="white",
                            width=0)
       Emp_ID_Label.grid(row=0, column=2, padx=10, sticky=W)
       Emp_ID_entry = ttk.Entry(current_course_frame, textvariable=self.var_Emp_Id, width=14,
                                font=("time new roman", 12, "bold"))
       Emp_ID_entry.grid(row=0, column=3, padx=10, sticky=W)

       # department
       dep_Label = Label(current_course_frame, text="Department", font=("time new roman", 12, "bold"), bg="white",
                         width=0)
       dep_Label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

       dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("time new roman", 12, "bold"),
                                state="read only", width=12)
       dep_combo["values"] = (" Department", "CSE", "IT", "ECE", "EEE", "MECH", "CIVIL")
       dep_combo.current(0)
       dep_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

       # Bloods group
       Bloods_group_Label = Label(current_course_frame, text="Bloods Group", font=("time new roman", 13, "bold"), bg="white",
                            width=0)
       Bloods_group_Label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

       Bloods_group_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Bloods_Group,
                                   font=("time new roman", 13, "bold"), state="read only", width=12)
       Bloods_group_combo["values"] = ("Bloods Group", "O+", "O-", "A+", "A-","B+","B-","AB+","AB-")
       Bloods_group_combo.current(0)
       Bloods_group_combo.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # gender
       Gender_Label = Label(current_course_frame, text="Gender:", font=("time new roman", 12, "bold"),
                            bg="white",
                            width=0)
       Gender_Label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

       Gender_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Gender,
                                   font=("time new roman", 13, "bold"),
                                   state="read only", width=12)
       Gender_combo["values"] = ("Male", "Female", "Other")
       Gender_combo.current(0)
       Gender_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

       # DOB
       dob_Label = Label(current_course_frame, text="DOB:", font=("time new roman", 12, "bold"),
                         bg="white",
                         width=0)
       dob_Label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
       dob_entry = ttk.Entry(current_course_frame, textvariable=self.var_dob, width=14,
                             font=("time new roman", 12, "bold"))
       dob_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
       # Email
       Email_Label = Label(current_course_frame, text="Email:", font=("time new roman", 12, "bold"),
                           bg="white",
                           width=0)
       Email_Label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
       Email_entry = ttk.Entry(current_course_frame, textvariable=self.var_Email, width=14,
                               font=("time new roman", 12, "bold"))
       Email_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
       # phone no
       Phone_Label = Label(current_course_frame, text="Phone No:", font=("time new roman", 12, "bold"),
                           bg="white",
                           width=0)
       Phone_Label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
       Phone_entry = ttk.Entry(current_course_frame, textvariable=self.var_Phone, width=14,
                               font=("time new roman", 12, "bold"))
       Phone_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

       # phone no2
       Phone_no_Label = Label(current_course_frame, text="Phone No2:", font=("time new roman", 12, "bold"),
                           bg="white",
                           width=0)
       Phone_no_Label.grid(row=5, column=2, padx=10, pady=5, sticky=W)
       Phone_no_entry = ttk.Entry(current_course_frame, textvariable=self.var_Phone_no, width=14,
                               font=("time new roman", 12, "bold"))
       Phone_no_entry.grid(row=5, column=3, padx=10, pady=5, sticky=W)
       # address
       address_Label = Label(current_course_frame, text="Address:", font=("time new roman", 12, "bold"),
                             bg="white",
                             width=0)
       address_Label.grid(row=5, column=0, padx=10, pady=5, sticky=W)
       address_entry = ttk.Entry(current_course_frame, textvariable=self.var_address, width=14,
                                 font=("time new roman", 12, "bold"))
       address_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)
       # father name
       Father_Label = Label(current_course_frame, text="Father Name:", font=("time new roman", 12, "bold"),
                             bg="white",
                             width=0)
       Father_Label.grid(row=6, column=0, padx=10, pady=5, sticky=W)
       Father_entry = ttk.Entry(current_course_frame, textvariable=self.var_Father, width=14,
                                 font=("time new roman", 12, "bold"))
       Father_entry.grid(row=6, column=1, padx=10, pady=5, sticky=W)
       # radio buttons
       Radiobutton1 = ttk.Radiobutton(current_course_frame, variable=self.var_Radiobutton1,
                                      text="Take Photos Sample", value="Yes")
       Radiobutton1.grid(row=6, column=2)
       Radiobutton2 = ttk.Radiobutton(current_course_frame, variable=self.var_Radiobutton1,
                                      text="No Photos Sample", value="No")
       Radiobutton2.grid(row=6, column=3)
       # button frame
       btn_Frame = Frame(current_course_frame, bd=2, relief=RIDGE, bg="white")
       btn_Frame.place(x=0, y=220, width=715, height=100)

       save_btn = Button(btn_Frame, text="Save",command=self.add_data,width=15, font=("time new roman", 12, "bold"),
                         bg="blue", fg="white")
       save_btn.grid(row=0, column=0)

       update_btn = Button(btn_Frame, text="Update",command=self.update_data ,width=13,
                           font=("time new roman", 12, "bold"), bg="blue", fg="white")
       update_btn.grid(row=0, column=1)

       delete_btn = Button(btn_Frame, text="Delete", command=self.delete_data, width=13,
                           font=("time new roman", 12, "bold"), bg="blue",
                           fg="white")
       delete_btn.grid(row=0, column=2)

       reset_btn = Button(btn_Frame, text="Reset", command=self.reset_data, width=13,
                          font=("time new roman", 12, "bold"), bg="blue", fg="white")
       reset_btn.grid(row=0, column=3)



       btn_Frame1 = Frame(current_course_frame, bd=2, relief=RIDGE, bg="white")
       btn_Frame1.place(x=0, y=255, width=710, height=70)

       take_photos_btn = Button(btn_Frame1, text="Take Photos Sample ",command=self.generate_dataset, width=17,
                                font=("time new roman", 12, "bold"),
                                bg="blue", fg="white")
       take_photos_btn.grid(row=0, column=0)


       # right label frame
       Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Staff Details",
                                font=("time new roman", 12, "bold"))
       Right_frame.place(x=620, y=10, width=620, height=535)

       img3_Right = Image.open("image\\SA3.png")
       img3_Right = img3_Right.resize((517, 97), Image.ANTIALIAS)
       self.photoimg3_Right = ImageTk.PhotoImage(img3_Right)
       b1 = Label(Right_frame, image=self.photoimg3_Right, cursor="hand2")
       b1.place(x=0, y=0, width=590, height=100)

       # ========serach System========

       Serach_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Serach System",
                                 font=("time new roman", 12, "bold"))
       Serach_frame.place(x=5, y=100, width=590, height=100)

       Serach_Label = Label(Serach_frame, text="Serach By:", font=("time new roman", 15, "bold"),
                            bg="red", fg="white",
                            width=0)
       Serach_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

       self.var_com_search = StringVar()
       Serach_combo = ttk.Combobox(Serach_frame, textvariable=self.var_com_search, font=("time new roman", 13, "bold"),
                                   state="read only", width=16)
       Serach_combo["values"] = ("Select ", "Roll No", "Phone No",)
       Serach_combo.current(0)
       Serach_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

       self.var_search = StringVar()
       Serach_entry = ttk.Entry(Serach_frame, textvariable=self.var_search, width=15,
                                font=("time new roman", 12, "bold"))
       Serach_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

       Serach_btn = Button(Serach_frame,  text="Search", width=13,
                           font=("time new roman", 10, "bold"), bg="blue",
                           fg="white")
       Serach_btn.grid(row=1, column=0)

       ShowAll_btn = Button(Serach_frame, text="Show All", width=13,
                            font=("time new roman", 10, "bold"), bg="blue",
                            fg="white")
       ShowAll_btn.grid(row=1, column=1, padx=2)
       # table frame
       table_frame = Frame(Right_frame, bd=2, bg="green", relief=RIDGE)
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
       self.staff_table.bind("<ButtonRelease>", self.get_cursor)
       self.fetch_data()

       # ======FUNCTION DECRATION=====
    def add_data(self):
        if (self.var_dep.get() == "" or self.var_name.get() == "" or self.var_Emp_Id.get() == ""):
              messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                  database="staff")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_name.get(),
                    self.var_Emp_Id.get(),
                    self.var_dep.get(),
                    self.var_Bloods_Group.get(),
                    self.var_Gender.get(),
                    self.var_dob.get(),
                    self.var_Email.get(),
                    self.var_Phone.get(),
                    self.var_Phone_no.get(),
                    self.var_address.get(),
                    self.var_Father.get(),
                    self.var_Radiobutton1.get()
                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Staff details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

                   # _____fetch data___

    def fetch_data(self):
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
           # =======get cursor======

    def get_cursor(self, event=""):
           cursor_focus = self.staff_table.focus()
           content = self.staff_table.item(cursor_focus)
           data = content["values"]

           self.var_name.set(data[0]),
           self.var_Emp_Id.set(data[1]),
           self.var_dep.set(data[2]),
           self.var_Bloods_Group.set(data[3]),
           self.var_Gender.set(data[4]),
           self.var_dob.set(data[5]),
           self.var_Email.set(data[6]),
           self.var_Phone.set(data[7]),
           self.var_Phone_no.set(data[8]),
           self.var_address.set(data[9]),
           self.var_Father.set(data[10]),
           self.var_Radiobutton1.set(data[11])

       # updata function
    def update_data(self):
           if (self.var_dep.get() == "" or self.var_name.get() == "" or self.var_Emp_Id.get() == ""):
               messagebox.showerror("Error", "All Fields are required", parent=self.root)
           else:
               try:
                   update = messagebox.askyesno("Update", "Are You want to update this staff details",
                                                parent=self.root)
                   if update > 0:
                       conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                      database="staff")
                       my_cursor = conn.cursor()
                       my_cursor.execute(
                           "update staff set  Staff_Name=%s, dep=%s, Bloods_Group=%s,"
                           " Gender=%s, DOB=%s, Email=%s, Phone_No=%s,Phone_No2=%s, Address=%s,Father=%s, "
                           "PhotoSamples=%s where Emp_ID_No=%s", (
                               self.var_name.get(),
                               self.var_dep.get(),
                               self.var_Bloods_Group.get(),
                               self.var_Gender.get(),
                               self.var_dob.get(),
                               self.var_Email.get(),
                               self.var_Phone.get(),
                               self.var_Phone_no.get(),
                               self.var_address.get(),
                               self.var_Father.get(),
                               self.var_Radiobutton1.get(),
                               self.var_Emp_Id.get()

                           ))
                   else:
                       if not update:
                           return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success", "Staff details successfully update completed", parent=self.root)
               except Exception as es:
                   messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)
           # delete function

    def delete_data(self):
           if self.var_Emp_Id.get == "":
               messagebox.showerror("Error", "Staff id must be required", parent=self.root)
           else:
               try:
                   delete = messagebox.askyesno("Staff delete page", "Do You want to delete this Staff",
                                                parent=self.root)
                   if delete > 0:
                       conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                      database="staff")
                       my_cursor = conn.cursor()
                       sql = "delete from staff where Emp_Id_No=%s"
                       val = (self.var_Emp_Id.get(),)
                       my_cursor.execute(sql, val)
                   else:
                       if not delete:
                           return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete", "successfully deleted staff details", parent=self.root)
               except Exception as es:
                   messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)
           # reset functiom

    def reset_data(self):


           self.var_name.set("")
           self.var_dep.set("Select Department")
           self.var_Emp_Id.set("")
           self.var_Bloods_Group.set("Bloods_Group")
           self.var_Gender.set("Male")
           self.var_dob.set("")
           self.var_Email.set("")
           self.var_Phone.set("")
           self.var_Phone_no.set("")
           self.var_address.set("")
           self.var_Father.set("")
           self.var_Radiobutton1.set("")

       # Take Photos Samples or generate data
    def generate_dataset(self):
           if (self.var_dep.get() == "" or self.var_name.get() == "" or self.var_Emp_Id.get() == ""):
               messagebox.showerror("Error", "All Fields are required", parent=self.root)
           else:
               try:
                   conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                  database="staff")
                   my_cursor = conn.cursor()
                   my_cursor.execute("Select * from staff")
                   myresult = my_cursor.fetchall()
                   id = 0
                   for x in myresult:
                       id += 1
                   my_cursor.execute( "update staff set  Staff_Name=%s, dep=%s, Bloods_Group=%s,"
                           " Gender=%s, DOB=%s, Email=%s, Phone_No=%s,Phone_No2=%s, Address=%s,Father=%s, "
                           "PhotoSamples=%s where Emp_ID_No=%s", (
                       self.var_name.get(),
                       self.var_dep.get(),
                       self.var_Bloods_Group.get(),
                       self.var_Gender.get(),
                       self.var_dob.get(),
                       self.var_Email.get(),
                       self.var_Phone.get(),
                       self.var_Phone_no.get(),
                       self.var_address.get(),
                       self.var_Father.get(),
                       self.var_Radiobutton1.get(),
                       self.var_Emp_Id.get() == id + 1

                                     ))
                   conn.commit()
                   self.fetch_data()
                   self.reset_data()
                   conn.close()
                   # face open================================
                   faceCascade = cv2.CascadeClassifier("C:\\Users\\SENTHIL RK\\python\\Lib\\"
                                                       "site-packages\\cv2\\data\\"
                                                       "haarcascade_frontalface_default.xml")

                   def face_cropped(img):
                       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                       faces = faceCascade.detectMultiScale(gray, 1.3, 5)
                       for (x, y, w, h) in faces:
                           face_cropped = img[y:y + h, x:x + w]
                           return face_cropped

                   cap = cv2.VideoCapture(0)
                   img_id = 0
                   while True:
                       ret, my_frame = cap.read()
                       if face_cropped(my_frame) is not None:
                           img_id += 1
                           face = cv2.resize(face_cropped(my_frame), (450, 450))
                           face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                           file_name_path = "data/staff_data/user" + str(id) + "." + str(img_id) + ".jpg"
                           cv2.imwrite(file_name_path, face)
                           cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 225, 0), 2)
                           cv2.imshow("Crooped Face", face)
                       if cv2.waitKey(1) == 13 or int(img_id) == 100:
                           break
                   cap.release()
                   cv2.destroyAllWindows()
                   messagebox.showinfo("Result", "Generating data sets compeled!!!!")
               except Exception as es:
                   messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)


if __name__ == '__main__':
    root = tk.Tk()
    obj = Staff(root)
    root.mainloop()