from tkinter import *
from tkinter import  ttk

def stdsearch1():
 pass
def stdclear1():
 pass

def stdexit1():
 pass

sea=Tk()
sealab1= Label(sea,text="Search Students who are elegible to your colleges according to certain criteria and can do advertisement by sending college brouchers to their email id ").grid(row=0, column=0, sticky=W)
stdlab2= Label(sea, text="Location").grid(row=1, column=0, sticky=W)
stdlab3= Label(sea, text="12th Precentage").grid(row=2, column=0, sticky=W)
sea.stdcombo1 = ttk.Combobox(sea, width=15)
sea.stdcombo2 = ttk.Combobox(sea, width=15)
sea.stdcombo1['values']=("Delhi","Bangalore","Mumbai","U.P", "Kolkata","Chennai","Kerala")
sea.stdcombo2['values']=("above 90", "above 80", "above 70")

sea.stdcombo1.grid(row=1, column=2)
sea.stdcombo2.grid(row=2, column=2)

stdbut1 = Button(sea, text="Search", width=6, command=stdsearch1).grid(row=20, column=7, sticky=W)
#stdbut2 = Button(sea, text="Clear", width=6, command=stdclear1).grid(row=20,column=8,sticky=W)
stdbut3 = Button(sea, text="Exit", width=6, command=stdexit1).grid(row=20, column=9, sticky=W)


sea.mainloop()
