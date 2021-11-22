from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import messagebox
import Student_Details as sd

import cv2
import numpy as np
import face_recognition
import os


def main():
    att = Tk()
    att.title("Attendence Menus")
    att.geometry("1500x800")
    att.configure(background='pink')
    att.iconbitmap("Images//logo1.ico")


    #take function helps in marking the attendance of thebased on face recognition
    def take():
        limit = "12:37:00"
        global now
        global dtString
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')
        if dtString < limit:
            f = open('Records.csv', "w")
            f.writelines('Name,Date,Time')
            f.close()



        import attendanceProject as ap
        ap.main()

    #view function hepls to view the attendance sheet
    def view():
        vw = Tk()
        vw.geometry("500x300")
        vw.title("Verification")
        vw.configure(background="black")
        vw.iconbitmap("Images//logo1.ico")

        Form = Frame(vw, height=50, bd=30)
        Form.pack(side=TOP, pady=20)

        Pass = Entry(Form, font=('times', 12))
        Pass.grid(row=1, column=1)
        Pass.insert(0, "Passcode")
        Pass.configure(state=DISABLED)

        def on_click(event):
            Pass.configure(state=NORMAL, show='*')
            Pass.delete(0, END)

        Pass.bind("<Button-1>", on_click)

        def make_solid(event):
            att.attributes('-alpha', 1.0)



        def verify():
            if Pass.get() == "":
                lbl_text.config(text='Please complete the required field!', fg='red')

            elif Pass.get() == "Sanpoly@446":
                import Convert as cvt
                import Display as dis
                att.attributes('-alpha', 0.8)
                response = messagebox.showinfo('Welcome', 'Verfied Successfully')
                vw.destroy()

                cvt.main()

                dis.main()

            else:
                lbl_text.config(text="Invalid password", fg='red')

        att.bind('<Button-1>', make_solid)

        lbl_text = Label(Form)
        lbl_text.grid(row=4, column=1)

        Sub_btn = Button(Form, text="Verify", font=('times', 10, 'bold'), width=20, command=verify, bg='dark grey')
        Sub_btn.grid(row=5, column=1)

        vw.mainloop()




    def home():
        att.destroy()
        import Home as hm
        hm.main()


    #back function
    def back():
        att.destroy()
        sd.main()

    #Frames
    Top = Frame(att, bd=30, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Mid = Frame(att, height=500, relief=RIDGE, bg='grey')
    Mid.pack(side=TOP, ipady=50, ipadx=50, pady=10)
    Form = Frame(att, height=50, bd=30, bg='pink')
    Form.pack(side=TOP, pady=20)

    #lables and images
    lbl = Label(Top, text="CHOOSE YOUR OPTION", font=('times', 50, 'bold italic'), padx=30, pady=30, bg='pink')
    lbl.pack(fill=BOTH, expand=1)

    img_mark = ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\PycharmProject\\PycharmTest\\Project\\Images\\Mark.jpg"))
    img_mark_lbl = Label(Mid, image=img_mark)
    img_mark_lbl.grid(row=0, column=0, padx=100, pady=40)

    img_view = ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\PycharmProject\\PycharmTest\\Project\\Images\\View-3.jpg"))
    img_view_lbl = Label(Mid, image=img_view)
    img_view_lbl.grid(row=0, column=1, padx=70, pady=40)

    #buttons
    button_mark = Button(Mid, text="Mark Attendance", font=('times',18,'bold'), command=take, bg='light blue', fg='black')
    button_mark.grid(row=1, column=0, padx=10, pady=10)

    button_view = Button(Mid, text="View Attendance", font=('times',18,'bold'), command=view, bg='light blue', fg='black')
    button_view.grid(row=1, column=1, padx=10, pady=10)

    back_btn = Button(Form, text="Back",font=('times',18,'bold'), command=back, bg='maroon', fg='white')
    back_btn.grid(row=3,column=0)

    home_btn = Button(Form, text="Home", command=home,font=('times',18,'bold'), bg='maroon', fg='white')
    home_btn.grid(row=3,column=1)

    att.mainloop()