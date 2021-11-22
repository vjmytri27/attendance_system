from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import sqlite3
import numpy as np
from csv import writer

conn = sqlite3.connect('Student.db')

c = conn.cursor()


df1 = pd.read_csv('Records.csv')

comparision = c.execute("SELECT *,Reg_No FROM Std_Records")
df2 = pd.read_sql_query("SELECT * from Std_Records", conn)
#
# print(df1)

df2.rename(columns = {'First_Name' : 'Name'}, inplace = True)
df1['Name'] = df1['Name'].str.capitalize()
pre = df1['Name']
# print(pre)
# print(df2)
df_abs = df2.merge(df1.drop_duplicates(), on = 'Name', how = 'left', indicator = 'True')
# # print(df_abs)
#
# df_abs['_merge'] == 'left_only'
df_abs = np.logical_not(df2.Name.isin(pre))
df2.ignore_index=True
# print(df_abs)

# df1.append(df2[df_abs].Name, ignore_index=True)#[df_abs], ignore_index = True)
# print(df1)
# df2.index_col=False

Names = df2[df_abs].Name
Names.index_col = True
print(Names)


# with open('Records.csv', 'a') as f:
#
#
#
#     # write_object = csv.writer(f)
#     f.writelines(f'\n{df2[df_abs].Name+", -, -"}')
#
#     # write_object.writerow(row[:-1])
#     # write_object.writerow()
#     # df2
#     # df2[df_abs].Name.to_csv(f_object, header=False)
#     # f = f.drop('dtype')
#
#     f.close()

#
# print(df1)



conn.close()
