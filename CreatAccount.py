from tkinter import *
import sqlite3
from tkinter import filedialog
import pandas as pd

def main():
    cre = Tk()
    cre.title("Details for Student Enrollement")
    cre.geometry("1500x800")
    cre.configure(background="pink")
    cre.iconbitmap("Images//logo1.ico")



    # back function for create window
    def back():
        cre.destroy()
        #cre_acc.quit()
        import Student_Details as sd
        sd.main()



    # submit function for create window
    def submit():
        #create a db
        conn = sqlite3.connect('Student.db')
        # cursor
        c = conn.cursor()

        # Insert into table
        c.execute("INSERT INTO Std_Records VALUES (:reg, :fn, :ln, :sem)",
                  {
                      'reg': str(reg.get()),
                      'fn': fn.get(),
                      'ln': ln.get(),
                      'sem': str(sem.get())
                  })
        conn.commit()

        # close connection
        conn.close()

        #clear the text boxes
        reg.delete(0, END)
        fn.delete(0, END)
        ln.delete(0, END)
        sem.delete(0, END)

        import Acc_Successful as  sc
        sc.main()





    def open():
        cre.filename = filedialog.askopenfilename(initialdir="C:/Users/Asus/PycharmProject/Images-E", title="Select an image",
                                                      filetypes=(("png files", "*.png"), ("all files", "*.*")))
        global lbl
        lbl = cre.filename
        from CopyImage import CopyImg as ci
        ci(lbl)


    # Connecting to database
    conn = sqlite3.connect("Student.db")
    # cursor
    c = conn.cursor()

    # create table
    c.execute(
        "CREATE TABLE IF NOT EXISTS Std_Records(Reg_No TEXT NOT NULL PRIMARY KEY, First_Name TEXT NOT NULL, Last_Name TEXT, Sem TEXT)")

    #Frames
    Top = Frame(cre, bd=20, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Mid = Frame(cre, height=500, bd=30, relief=RIDGE)
    Mid.pack(side=TOP, fill=X, ipady=50, ipadx=200)
    Form = Frame(cre, height=50, bd=30, bg='pink')
    Form.pack(side=TOP, pady=20)



    #labels
    wc_lbl = Label(Top, text="Fill the form", font=('times', 50, 'bold italic'), padx=30, pady=30, bg='pink')
    wc_lbl.pack(fill=BOTH, expand=1)

    # Entry form labels
    reg_lbl = Label(Mid, text="Register Number:", bd=15)
    reg_lbl.grid(row=0, column=0, padx=10, pady=10)
    fn_lbl = Label(Mid, text="First Name:",  bd=15)
    fn_lbl.grid(row=1, column=0, padx=10, pady=10)
    ln_lbl = Label(Mid, text="Last Name:", bd=15)
    ln_lbl.grid(row=2, column=0, padx=10, pady=10)
    sem_lbl = Label(Mid, text="Current Semester:", bd=15)
    sem_lbl.grid(row=3, column=0, padx=10, pady=10)


    global reg
    global fn
    global ln
    global sem

    # Input Entry
    reg = Entry(Mid, width=40)
    reg.grid(row=0, column=1, padx=10, pady=10)
    fn = Entry(Mid, width=40)
    fn.grid(row=1, column=1, padx=10, pady=10)
    ln = Entry(Mid, width=40)
    ln.grid(row=2, column=1, padx=10, pady=10)
    sem = Entry(Mid, width=40)
    sem.grid(row=3, column=1, padx=10, pady=10)

    # Choosing Image
    img_btn = Button(Mid, text="Choose image", command=open)
    img_btn.grid(row=4, column=0, padx=10, pady=10)

    # submit button
    submit_btn = Button(Form, text="Submit", command=submit, bg='green', fg='white')
    submit_btn.grid(row=5, column=0)

    # back button
    back_btn = Button(Form, text="Back", command=back, bg='maroon', fg='white')
    back_btn.grid(row=5, column=1, padx=10, pady=10)



    cre.mainloop()