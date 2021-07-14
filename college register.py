
from tkinter import *
import sqlite3
import tkinter as tk

coll = tk.Tk()
coll.title("College Registration Form")
coll.geometry("1000x800")


def click_cancel(self):
    self.master.destroy()

College_Name = StringVar()
Col_Rep_Name = StringVar()
Post_of_Col_Rep = StringVar()
Mob_of_Col_Reg = StringVar()
Col_URL = StringVar()
Col_Reg_No = StringVar()
Col_Rep_email_id = StringVar()
Col_Reg_Date = StringVar()
Col_Location = StringVar()
#Password = StringVar()

def database1():
    cname=College_Name.get()
    col_rep_name=Col_Rep_Name.get()
    post_of_rep=Post_of_Col_Rep.get()
    mob_of_rep=Mob_of_Col_Reg.get()
    url=Col_URL.get()
    reg_number=Col_Reg_No.get()
    rep_email=Col_Rep_email_id.get()
    register_date=Col_Reg_Date.get()
    location=Col_Location.get()

    conn = sqlite3.connect('form_regcol.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Cregister(Col_Name TEXT,Col_Rep_Name TEXT,Post_of_Col_Rep TEXT,Mob_of_Col_Reg TEXT,Col_Rep_email_id TEXT,Col_Reg_No TEXT,Col_URL TEXT,Col_Reg_Date TEXT,Col_Location TEXT)')
    cursor.execute('INSERT INTO Cregister(Col_Name,Col_Rep_Name,Post_of_Col_Rep,Mob_of_Col_Reg,Col_Rep_email_id,Col_Reg_No,Col_URL,Col_Reg_Date,Col_Location) VALUES(?,?,?,?,?,?,?,?,?)',(cname,col_rep_name,post_of_rep,mob_of_rep,rep_email,reg_number,url,register_date,location))
    conn.commit()



label1 = tk.Label(text="Fill your college Details:")
label1.grid(row=0, column=0,sticky=W)
label2 = tk.Label(text="College Name")
label2.grid(row=1,column=0,sticky=W)
label3 = tk.Label(text="College Representative Name")
label3.grid(row=2,column=0, sticky=W)
label4 = tk.Label(text="Post of College Representative")
label4.grid(row=3, column=0, sticky=W)
label5 = tk.Label(text="Mobile Number of College Representative")
label5.grid(row=4,column=0, sticky=W )
label6 = tk.Label(text= "College Representative email id")
label6.grid(row=5, column=0, sticky=W)

label7 = tk.Label(text="College Registration Number")
label7.grid(row=1, column=6, sticky=W)
label8 = tk.Label(text="College URL")
label8.grid(row=2,column=6, sticky=W)
label9 = tk.Label(text= "College Registration Date")
label9.grid(row=3, column=6, sticky=W)
label10 = tk.Label(text= "College Location")
label10.grid(row=4, column=6, sticky=W)


entry1 = tk.Entry(coll,textvar=College_Name)
entry1.grid(row=1, column=1, sticky=W)
entry2 = tk.Entry(coll,textvar=Col_Rep_Name)
entry2.grid(row=2, column=1, sticky=W)
entry3 = tk.Entry(coll,textvar=Post_of_Col_Rep)
entry3.grid(row=3, column=1, sticky=W)
entry4 = tk.Entry(coll,textvar=Mob_of_Col_Reg)
entry4.grid(row=4, column=1, sticky=W)
entry7 = tk.Entry(coll,textvar=Col_Rep_email_id)
entry7.grid(row=5, column=1, sticky=W)
entry6 = tk.Entry(coll,textvar=Col_Reg_No)
entry6.grid(row=1, column=8, sticky=W)
entry5 = tk.Entry(coll,textvar=Col_URL)
entry5.grid(row=2, column=8, sticky=W)
entry8 = tk.Entry(coll,textvar=Col_Reg_Date)
entry8.grid(row=3, column=8, sticky=W)
entry9 = tk.Entry(coll,textvar=Col_Location)
entry9.grid(row=4, column=8, sticky=W)

button1 = Button(coll, text="SUBMIT", width=6,bg='brown', fg='white', command=database1)
button1.grid(row=12, column=2, sticky=W)
button2 = Button(coll, text="CANCEL", width=6,bg='brown', fg='white', command=coll.destroy)
button2.grid(row=12, column=5, sticky=E)

coll.mainloop()

