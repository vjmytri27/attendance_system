from tkinter import *

def main():

    TL = Tk()
    TL.title("Punctuality")
    TL.geometry("500x500")
    TL.configure(background="pink")
    TL.iconbitmap("Images//logo1.ico")

    def back():
        TL.destroy()
        # import Attendance as at
        # at.main()

    lbl = Label(TL, text="Please be punctual!!!", fg='dark blue', bg='pink', font=('times',24,'bold'),bd=10)
    lbl.grid(row=0,column=0, padx=110, pady=200)

    back = Button(TL, text='BACK', font=('times',10,'bold'), bg='maroon', fg='white', command=back)
    back.grid(row=2,column=0)

    TL.mainloop()