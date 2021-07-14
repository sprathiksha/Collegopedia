from tkinter import *
import sqlite3



cou= Tk()
cou.title("Course Details")
cou.geometry("1000x500")


#def click_cancel(self):
#   self.master.destroy()

COLNAME=StringVar()
CNAME=StringVar()
No_of_Yrs=StringVar()
FEES=StringVar()
ENTRANCE_EXAM=StringVar()
Mob_of_Col_Reg=StringVar()
COMPULSORY_SUBS=StringVar()
CUTOFF_PERCENT=StringVar()


def database():

    collegename=COLNAME.get()
    colname=CNAME.get()
    no_of_yrs=No_of_Yrs.get()
    fees=FEES.get()
    subjects=COMPULSORY_SUBS.get()
    percentage=CUTOFF_PERCENT.get()
    mob_of_rep = Mob_of_Col_Reg.get()
    entrance=ENTRANCE_EXAM.get()
    conn = sqlite3.connect('addfinal_course.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS addfinal_course(COLNAME TEXT, CNAME TEXT,No_of_Yrs TEXT,FEES TEXT,COMPULSORY_SUBS TEXT,CUTOFF_PERCENT TEXT,Mob_of_Col_Reg TEXT,ENTRANCE_EXAM TEXT)')
    cursor.execute('INSERT INTO addfinal_course(COLNAME, CNAME ,No_of_Yrs ,FEES ,COMPULSORY_SUBS ,CUTOFF_PERCENT,Mob_of_Col_Reg,ENTRANCE_EXAM) VALUES(?,?,?,?,?,?,?,?)',(collegename, colname,no_of_yrs,fees,subjects,percentage, mob_of_rep,entrance))
    conn.commit()


add1= Label(cou, text="ENTER COURSE DETAILS PROVIDED BY YOU COLLEGE").grid(row=0, column=1, sticky=W)
add7 = Label(cou, text= "college Name").grid(row=1, column=2,sticky=W)
add2= Label(cou, text= "Course Name").grid(row=2, column=2, sticky=W)
add3= Label(cou, text= "Number of Years").grid(row=3, column=2,sticky=W)
add4= Label(cou, text= "Fee Charge per of Course per Year").grid(row=4, column=2, sticky=W)
add5= Label(cou, text="Compulsory Subject in Class 12th").grid(row=5, column=2,sticky=W )
add6= Label(cou, text="Cutoff Percentage for Course").grid(row=6, column=2,sticky=W)
add9= Label(cou, text="Mob_of_Col_Reg").grid(row=7, column=2,sticky=W)
add8= Label(cou, text="Entrance Exam").grid(row=8, column=2,sticky=W)

txtadd6= Entry(cou, textvar=COLNAME).grid(row=1, column=3, sticky=W)
txtadd1= Entry(cou, textvar=CNAME).grid(row=2, column=3, sticky=W)
txtadd2= Entry(cou, textvar=No_of_Yrs).grid(row=3, column=3, sticky=W)
txtadd3= Entry(cou, textvar=FEES).grid(row=4, column=3, sticky=W)
txtadd4= Entry(cou, textvar=COMPULSORY_SUBS).grid(row=5, column=3, sticky=W)
txtadd5= Entry(cou, textvar=CUTOFF_PERCENT).grid(row=6, column=3, sticky=W)
txtadd7= Entry(cou, textvar=Mob_of_Col_Reg).grid(row=7, column=3, sticky=W)
txtadd8= Entry(cou, textvar=ENTRANCE_EXAM).grid(row=8, column=3, sticky=W)


addbutton1 = Button(cou, text="Submit", width=6, bg='black', fg='white', command=database).grid(row=12, column=3, sticky=W)
#addbutton2 = Button(cou, text="Cancel",width=6, bg='black', fg='white', command=self.click_cancel).grid(row=10, column=3, sticky=W)
cou.mainloop()
