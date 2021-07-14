
from tkinter import *
import tkinter as tk
import sqlite3


window = tk.Tk()
window.title("   WELCOME TO COLLEGOPEDIA   ")
window.geometry("1024x700")




def click_cancel(self):
    self.master.destroy()

NAME=StringVar()
SURNAME=StringVar()
PERCENTAGE=StringVar()
MOBILE_NO=StringVar()
EMAIL_ID=StringVar()
DOB=StringVar()
var=IntVar()
CITY=StringVar()
d=StringVar()
c=StringVar()

def database():
    name1=NAME.get()
    name2=SURNAME.get()
    percent=PERCENTAGE.get()
    mobile=MOBILE_NO.get()
    email=EMAIL_ID.get()
    gender=var.get()
    dob=DOB.get()
    city=CITY.get()
    state=d.get()
    country=c.get()
    conn = sqlite3.connect('regstd.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS sregg(NAME TEXT,SURNAME TEXT,PERCENTAGE TEXT,MOBILE_NO TEXT,EMAIL_ID TEXT,GENDER TEXT,DOB TEXT,CITY TEXT,STATE TEXT,COUNTRY TEXT)')
    cursor.execute('INSERT INTO sregg(NAME,SURNAME,PERCENTAGE,MOBILE_NO,EMAIL_ID,GENDER,DOB,CITY,STATE,COUNTRY) VALUES(?,?,?,?,?,?,?,?,?,?)',(name1,name2,percent,mobile,email,gender,dob,city,state,country))
    conn.commit()

#*******LABEL******

label1 = tk.Label(text = "REGISTRATION FORM")
label1.grid(column=0, row=0)

label2 = tk.Label(text="NAME")
label2.grid(column=0, row=1, sticky=E)

label3 = tk.Label(text="SURNAME")
label3.grid(column=0, row=2, sticky=E)

label10 = tk.Label(text="PERCENTAGE(12TH)")
label10.grid(column=0, row=3, sticky=E)


label4 = tk.Label(text="MOBILE NO")
label4.grid(column=0, row=4, sticky=E)



label6 = Label(window, text="GENDER") #width=20, #font=("bold", 10)
label6.grid(column=0,row=5, sticky=E)
#var = IntVar()
Radiobutton(window, text="Male",padx = 5, variable=var, value=1).grid(column=0, row=6, sticky=E)
Radiobutton(window, text="Female",padx = 20, variable=var, value=2).grid(column=1, row=6, sticky=E)
Radiobutton(window, text="Others",padx = 20, variable=var, value=3).grid(column=2, row=6, sticky=E)


label5 = tk.Label(text="EMAIL ID")
label5.grid(column=2, row=1, sticky=E)

label_7 = tk.Label(text="DOB")
label_7.grid(column=2, row=2, sticky=E)

label7 = tk.Label(text="CITY")
label7.grid(column=2, row=3, sticky=E)

label8 = tk.Label(text="STATE")
label8.grid(column=2, row=4, sticky=E)
#d = StringVar()
list1 = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattishgarh','Goa','Gujarat','haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']
droplist = OptionMenu(window,d, *list1)
droplist.config(width=15)
d.set("select your State")
droplist.grid(column=4,row=4, sticky=E)


label9 = tk.Label(text="COUNTRY")
label9.grid(column=2, row=5, sticky=E)
#c = StringVar()
list2 = ['Afghanistan','Bangladesh','China','India','Japan','Malaysia','Nepal','Saudi Arabia','Sri Lanka']

droplist = OptionMenu(window,c, *list2)
droplist.config(width=15)
c.set("select your country")
droplist.grid(column=4,row=5, sticky=E)


#------ENTRIES-----
entry1 = tk.Entry(window, textvar=NAME)
entry1.grid(column=1, row=1)

entry2 = tk.Entry(window, textvar=SURNAME)
entry2.grid(column=1, row=2)

entry2 = tk.Entry(window, textvar=PERCENTAGE)
entry2.grid(column=1, row=3)

entry3 = tk.Entry(window, textvar=MOBILE_NO)
entry3.grid(column=1, row=4)

entry4 = tk.Entry(window, textvar=EMAIL_ID)
entry4.grid(column=4, row=1)

entry5 = tk.Entry(window, textvar=DOB)
entry5.grid(column=4, row=2)

entry5 = tk.Entry(window, textvar=CITY)
entry5.grid(column=4, row=3)

#entry5 = tk.Entry()
#entry5.grid(column=1, row=7)



#entry7 = tk.Entry()
#entry7.grid(column=1, row=8)



#ch = Checkbutton(window, text="keep me notified")
#ch.grid(columnspan=2)

button_1 = Button(window, text="CREATE ACCOUNT", bg='brown', fg='white', command=database)
button_1.grid(column=2,row=10)
button_2 = Button(window, text="CANCEL", bg='brown', fg='white', command=window.destroy)
button_2.grid(column=4,row=10)

#window.config(bg='black')
window.mainloop()