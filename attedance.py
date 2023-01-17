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

mydata=[]
class Attendance:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title("ATTENDANCE STUDENT")
       #=========varabile========
       self.var_atten_id = StringVar()
       self.var_atten_Roll= StringVar()
       self.var_atten_name = StringVar()
       self.var_atten_department = StringVar()
       self.var_atten_time = StringVar()
       self.var_atten_date = StringVar()
       self.var_atten_attendance = StringVar()


       # first image
       img = Image.open("image\\sabg.jpg")
       img = img.resize((1272, 650), Image.ANTIALIAS)
       self.photoimg = ImageTk.PhotoImage(img)

       bg_image = Label(self.root, image=self.photoimg)
       bg_image.place(x=0, y=0, width=1272, height=650)
       title_lb1 = Label(bg_image, text="ATTENDANCE",
                         font=("time new roman", 25, "bold"), bg="green", fg="red")
       title_lb1.place(x=0, y=0, width=1280, height=45)

       main_frame = Frame(bg_image, bd=2, bg="white")
       main_frame.place(x=0, y=90, width=1272, height=600)

       # left label frame
       Left_frame = LabelFrame(main_frame, bd=2, bg="WHITE", relief=RIDGE,
                               font=("time new roman", 12, "bold"))
       Left_frame.place(x=20, y=10, width=590, height=535)

       img2_Left = Image.open("image\\SA3.png")
       img2_Left = img2_Left.resize((517, 97), Image.ANTIALIAS)
       self.photoimg2_Left = ImageTk.PhotoImage(img2_Left)
       b1 = Label(Left_frame, image=self.photoimg2_Left, cursor="hand2")
       b1.place(x=30, y=10, width=520, height=100)



       #labeland entry
       # Class student information
       Student_Attendance_frame = LabelFrame(Left_frame, bd=2, bg="white",
                                             relief=RIDGE, text="Student Attendance details",
                                             font=("time new roman", 12, "bold"))
       Student_Attendance_frame.place(x=0, y=163, width=585.5, height=368)
       # Attendance Id
       attendaneId_Label = Label(Student_Attendance_frame, text="Attendance Id:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       attendaneId_Label.grid(row=0, column=0,  pady=8)
       attendanceId_entry = ttk.Entry(Student_Attendance_frame, textvariable=self.var_atten_id,width=14, font=("time new roman", 12, "bold"))
       attendanceId_entry.grid(row=0, column=1,  pady=8)

       # Roll
       Roll_Label = Label(Student_Attendance_frame, text="Roll No:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       Roll_Label.grid(row=0, column=2,  pady=8)
       Roll_entry = ttk.Entry(Student_Attendance_frame, textvariable=self.var_atten_Roll,width=14, font=("time new roman", 12, "bold"))
       Roll_entry.grid(row=0, column=3,  pady=8)

       # name
       name_Label = Label(Student_Attendance_frame, text="Name:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       name_Label.grid(row=1, column=0,  pady=8)
       name_entry = ttk.Entry(Student_Attendance_frame,textvariable=self.var_atten_name, width=14, font=("time new roman", 12, "bold"))
       name_entry.grid(row=1, column=1,  pady=8)

       # Department
       dep_Label = Label(Student_Attendance_frame, text="Department:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       dep_Label.grid(row=1, column=2,  pady=8)
       dep_entry = ttk.Entry(Student_Attendance_frame, textvariable=self.var_atten_department,width=14, font=("time new roman", 12, "bold"))
       dep_entry.grid(row=1, column=3,  pady=8)

       # time
       time_Label = Label(Student_Attendance_frame, text="Time:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       time_Label.grid(row=2, column=0,  pady=8)
       time_entry = ttk.Entry(Student_Attendance_frame,textvariable=self.var_atten_time, width=14, font=("time new roman", 12, "bold"))
       time_entry.grid(row=2, column=1,  pady=8)

       # date
       date_Label = Label(Student_Attendance_frame, text="Date:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       date_Label.grid(row=2, column=2, pady=8)
       date_entry = ttk.Entry(Student_Attendance_frame, textvariable=self.var_atten_date,width=14, font=("time new roman", 12, "bold"))
       date_entry.grid(row=2, column=3, pady=8)
       # Attendance
       attendane_Label = Label(Student_Attendance_frame, text="Attendance Status", font=("time new roman", 11, "bold"),
                                 bg="WHITE", width=0)
       attendane_Label.grid(row=3, column=0)

       self.atten_status = ttk.Combobox(Student_Attendance_frame,
                                   font=("time new roman", 13, "bold"), textvariable=self.var_atten_attendance,
                                   state="read only", width=12)
       self.atten_status["values"] = ("Status", "Present", "Absent")
       self.atten_status.current(0)
       self.atten_status.grid(row=3, column=1, pady=8)

       # button frame
       btn_Frame = Frame(Student_Attendance_frame, bd=2, relief=RIDGE, bg="white")
       btn_Frame.place(x=0, y=180, width=715, height=36)
       Importcsv_btn = Button(btn_Frame, text="Import csv",command=self.importCsv ,width=18, font=("time new roman", 12, "bold"),
                         bg="blue", fg="white")
       Importcsv_btn.grid(row=0, column=0)

       Exportcsv_btn = Button(btn_Frame, command=self.exportCsv,text="Export csv", width=19,
                           font=("time new roman", 12, "bold"), bg="blue", fg="white")
       Exportcsv_btn.grid(row=0, column=1)



       reset_btn = Button(btn_Frame, text="Reset",  width=19,command=self.resetdata,
                          font=("time new roman", 12, "bold"), bg="blue", fg="white")
       reset_btn.grid(row=0, column=2)



       # right label frame
       Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("time new roman", 12, "bold"))
       Right_frame.place(x=620, y=10, width=620, height=535)
       #scroll bar table
       scroll_x = ttk.Scrollbar(Right_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(Right_frame, orient=VERTICAL)

       self.AttendanceReportTable= ttk.Scrollbar(Right_frame, orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(Right_frame, orient=VERTICAL)

       self.AttendanceReportTable=ttk.Treeview(Right_frame, columns=("Id", "Roll", "name", "department", "time", "date",
                                                              "attendance"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)

       scroll_x.config(command=self.AttendanceReportTable.xview)
       scroll_y.config(command=self.AttendanceReportTable.yview)

       self.AttendanceReportTable.heading("Id", text="Attendance ID")
       self.AttendanceReportTable.heading("Roll", text="Roll no ")
       self.AttendanceReportTable.heading("name", text="Name")
       self.AttendanceReportTable.heading("department", text="Department")
       self.AttendanceReportTable.heading("time", text="Time")
       self.AttendanceReportTable.heading("date", text="Date")
       self.AttendanceReportTable.heading("attendance", text="Attendance")
       self.AttendanceReportTable["show"] = "headings"

       self.AttendanceReportTable.column("Id", width=100)
       self.AttendanceReportTable.column("Roll", width=100)
       self.AttendanceReportTable.column("name", width=100)
       self.AttendanceReportTable.column("department", width=100)
       self.AttendanceReportTable.column("time", width=100)
       self.AttendanceReportTable.column("date", width=100)
       self.AttendanceReportTable.column("attendance", width=100)


       self.AttendanceReportTable.pack(fill=BOTH, expand=1)
       self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
       #self.fetch_data()
       # ====================================fetch data ==============================================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File" ,"*.csv"),
                                       ("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export", parsent=self.root)
                return  False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("ALL File", "*.*")),parent=self.root)
            with open(fln, mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
            messagebox.showinfo("DATA Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)


    def get_cursor(self, event=""):
        curses_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(curses_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_Roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_department.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def resetdata(self):
        self.var_atten_id.set("")
        self.var_atten_Roll.set("")
        self.var_atten_name.set("")
        self.var_atten_department.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")







if __name__ == '__main__':
    root = tk.Tk()
    obj = Attendance(root)
    root.mainloop()