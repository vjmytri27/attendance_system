# Libraries used in this file

from tkinter import *
from tkinter import messagebox


def main():
    root = Tk()
    root.title("Home Page")
    root.geometry("1500x800")
    root.configure(background='pink')
    root.iconbitmap("Images//logo1.ico")



    #Login function to authenticate the user
    def Login():

        if username.get() == "" or password.get() == "":
            lbl_text.config(text='Please complete the required field!', fg='red')

        elif username.get() == "Maitri" and password.get() == "2002":
            root.attributes('-alpha', 0.7)
            response = messagebox.showinfo('Welcome', 'Successful login')
            root.destroy()

            import  Student_Details as sd
            sd.main()

        else:
            lbl_text.config(text="Invalid username or password",fg='red')




    #Frames
    Top = Frame(root, bd=30, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Mid = Frame(root, height=500, relief=RIDGE)
    Mid.pack(side=TOP, fill=X, ipady=50, ipadx=200)
    Form = Frame(root, height=50, bd=30)
    Form.pack(side=TOP, pady=20)



    #labels
    wc_lbl = Label(Top, text="WELCOME TO SANPOLY FACECAM", font=('times', 50, 'bold italic'), padx=30, pady=30, bg='pink')
    wc_lbl.pack(fill=BOTH, expand=1)

    cre = Label(Mid, text="Enter your credentials: ", fg="pink", bg="black", font=('times', 28, 'bold'))
    cre.pack(fill=BOTH, expand=1)
    lbl_username = Label(Form, text="Username:", font=('times', 14, 'bold'), bd=15)
    lbl_username.grid(row=0, sticky='e')
    lbl_password = Label(Form, text="Password:", font=('times', 14, 'bold'), bd=15)
    lbl_password.grid(row=1, sticky='e')
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, font=('times', 14))
    username.grid(row=0, column=1)
    password = Entry(Form, show="*", font=('times', 14))
    password.grid(row=1, column=1)

    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Login", font=('times', 20, 'bold'), width=20, command=Login)
    btn_login.grid(pady=25, row=3, columnspan=2)



    root.mainloop()

