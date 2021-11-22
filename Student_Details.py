from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import numpy as np
from tkinter import messagebox

def main():

    std = Tk()
    std.title("Student Details")
    std.geometry("1500x800")
    std.configure(background="pink")
    std.iconbitmap("Images//logo1.ico")
    std.attributes('-alpha', 1.0)

    #Create and acttendance functions
    def Create():
        std.attributes('-alpha', 0.7)

        def make_solid(event):
            std.attributes('-alpha', 1.0)

        cre = Tk()
        cre.geometry("500x300")
        cre.title("Verification")
        cre.configure(background="black")
        cre.iconbitmap("Images//logo1.ico")

        str1 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = int(len(str1))
        # length = 5
        ver = ""
        for i in range(0, 5):
            ver = ver + str1[np.random.randint(0, n)];

        std.bind('<Button-1>', make_solid)

        def verify():
            if Pass.get() == "" and capcha_ver.get() == "":
                lbl_text.config(text='Please complete the required field!', fg='red')

            elif Pass.get() == "CSE123" and capcha_ver.get()==ver:
                cre.attributes('-alpha', 0.8)
                response = messagebox.showinfo('Welcome', 'Verfied Successfully')
                std.destroy()
                cre.destroy()
                import CreatAccount as ca
                ca.main()

            else:
                lbl_text.config(text="Invalid password or capcha", fg='red')



        Form = Frame(cre, height=50, bd=30)
        Form.pack(side=TOP, pady=20)

        Pass = Entry(Form, font=('times', 12))
        Pass.grid(row=1, column=1)
        Pass.insert(0, "Passcode")
        Pass.configure(state=DISABLED)
        def on_click(event):
            Pass.configure(state=NORMAL, show='*')
            Pass.delete(0, END)
        Pass.bind("<Button-1>", on_click)

        capcha = Label(Form, text=ver, bd=2)
        capcha.grid(row=2, column=1)
        capcha_ver = Entry(Form, width=15, font=('times', 10, 'bold'))
        capcha_ver.grid(row=3, column=1)

        lbl_text=Label(Form)
        lbl_text.grid(row=4, column=1)

        Sub_btn = Button(Form, text="Verify", font=('times', 10, 'bold'), width=20, command=verify, bg='dark grey')
        Sub_btn.grid(row=5, column=1)
        cre.mainloop()



    def Attendance():
        std.destroy()
        import Attendance as ads
        ads.main()

    def back():
        #std.destory()
        import Home as hm
        hm.main()

    #Frames
    Top = Frame(std, bd=30, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Mid = Frame(std, height=500, relief=RIDGE)
    Mid.pack(side=TOP, ipady=50, ipadx=50, pady=10)
    Form = Frame(std, height=50, bd=30, bg='pink')
    Form.pack(side=TOP, pady=20)

    #lables and images
    lbl = Label(Top, text="MENUS", font=('times', 50, 'bold italic'), padx=30, pady=30, bg='pink')
    lbl.pack(fill=BOTH, expand=1)

    img_create = ImageTk.PhotoImage(Image.open("Images/CREE.jpg"))
    img_create_lbl = Label(Mid, image=img_create)
    img_create_lbl.grid(row=0, column=0, padx=80, pady=40)

    img_attendance = ImageTk.PhotoImage(Image.open("Images/ATTNE2.jpg"))
    img_attendance_lbl = Label(Mid, image=img_attendance)
    img_attendance_lbl.grid(row=0, column=1, padx=80, pady=40)


    #buttons
    button_create = Button(Mid, text="Enroll",font=('times',18,'bold'), command=Create, bg='green', fg='white')
    button_create.grid(row=1, column=0, padx=10, pady=10)

    button_attendance = Button(Mid, text="Attendance", command=Attendance,font=('times',18,'bold'), bg='green', fg='white')
    button_attendance.grid(row=1, column=1, padx=10, pady=10)

    back_button = Button(Form, text='BACK',font=('times',18,'bold'), command=back)
    back_button.pack()



    std.mainloop()