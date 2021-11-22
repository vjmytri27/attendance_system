from tkinter import *

def main():
    suc=Tk()
    suc.title("Creation successful")
    suc.geometry("1500x800")
    suc.configure(background='pink')
    suc.iconbitmap("Images//logo1.ico")


    #Back function
    def back():
        suc.destroy()
        import Student_Details as sd
        sd


    #Frames
    Top = Frame(suc, bd=30, relief=RIDGE, bg='pink')
    Top.pack(side=TOP, fill=X)
    Mid = Frame(suc, height=400, relief=RIDGE, bg='pink')
    Mid.pack(side=TOP, pady=300)
    #Mid.pack(side=TOP, fill=X, ipady=50, ipadx=200)
    Form = Frame(suc, height=50, bd=30, bg='pink')
    Form.pack(side=TOP)

    #labels
    lbl = Label(Mid, text='SUCCESSFUL!!!', font=('Times', 40, 'bold italic'), bg='pink', fg='purple')
    lbl.grid()

    back_btn = Button(Form, text="Back", command=back, bg='maroon', fg='white')
    back_btn.grid()

    suc.mainloop()