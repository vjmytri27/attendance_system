import sqlite3
import face_recognition
import cv2
from tkinter import *

conn = sqlite3.connect("Student.db")

c = conn.cursor()

c.execute("DELETE FROM Std_Records WHERE Reg_No='446CS18022'")
# c.execute("DELETE FROM Std_Records WHERE Reg_No='02'")
# c.execute("DELETE FROM Std_Records WHERE Reg_No='03'")
# c.execute("DELETE FROM Std_Records WHERE Reg_No='04'")
# c.execute("DELETE FROM Std_Records WHERE Reg_No='06'")
# c.execute("DELETE FROM Std_Records WHERE Reg_No='07'")
# c.execute("DELETE FROM Std_Records WHERE Reg_No='446CS18014'")
# c.execute("DELETE FROM Std_Records WHERE Reg_No='09'")

#c.execute("ALTER TABLE Encoding DROP COLUMN Test")
#c.execute("DROP TABLE Encoding")
#c.execute("ALTER TABLE Encoding ADD Test FLOAT DEFAULT '0'")
c.execute("SELECT *,Reg_No FROM Std_Records")
#
records = c.fetchall()
#
for record in records:
    print(record[0])
    print(record[1])
    print(record[2])
    print(record[3])

# path = 'C:/Users/Asus/PycharmProject/Images-E/Maitri.jpg'
# curImg = cv2.imread(f'{path}')
# img = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
# encoding = face_recognition.face_encodings(img)
#
# for record in records:
#     if float(record[2]) == encoding:
#         print("True")
#     else:
#         print("False")

# print(bin(int(encoding[0][0])))

conn.commit()

conn.close()