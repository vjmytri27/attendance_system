from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import sqlite3

def main():
    di = Tk()
    di.title("Attendance List")
    di.geometry("500x500")
    di.iconbitmap("Images//logo1.ico")

    # di.configure(background='light grey')

    # lbl = Label(di, text="", font=('times',14), fg='black', bd=10, padx=10, pady=10)
    # lbl.pack()
    #
    #
    # f = pd.read_excel('Records.xlsx', index_col=0)
    # print(f)
    # lbl.configure(text=f)

    conn = sqlite3.connect('Student.db')

    c = conn.cursor()
    c.execute("SELECT * FROM Std_Records")
    records = c.fetchall()

    df1 = pd.read_csv('Records.csv')
    df2 = pd.read_sql_query("SELECT * FROM Std_Records",conn)

    conn.close()

    path = 'C:\\Users\\Asus\\PycharmProject\\PycharmTest\\Project\\Records.xlsx'


    frame1 = Frame(di, height=600, bd=5, relief=RIDGE)
    frame1.pack(side=TOP, ipady=200, ipadx=200)







    try:
            excel_filename = r"{}".format(path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

    except ValueError:
            di.messagebox.showerror("Information", "The file you have chosen is invalid")

    except FileNotFoundError:
            di.messagebox.showerror("Information", f"No such file as {path}")

    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = Scale(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
    treescrollx = Scale(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
    treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget





    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert




    di.mainloop()