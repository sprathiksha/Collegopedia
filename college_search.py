from tkinter import *
import tkinter as tk



window = tk.Tk()
window.title("   WELCOME TO COLLEGOPEDIA   ")
window.geometry("1024x700")

d=StringVar()
c=StringVar()
b=StringVar()
a=StringVar()

def ok():
    print("loading")




label8 = tk.Label(text="Location")
label8.grid(column=1, row=1, sticky=E)

list1 = ['Delhi','Bangalore','U.P','Mumbai','Kolkata','Chennai','Kerala']
droplist = OptionMenu(window,d, *list1)
droplist.config(width=15)
d.set("select your Location")
droplist.grid(column=2,row=1, sticky=E)

label9 = tk.Label(text="Budget")
label9.grid(column=1, row=2, sticky=E)


list2 = ['Above 4,00000', 'Above 300000', 'Above 200000','Above 100000','Above 50000']
droplist = OptionMenu(window,c, *list2)
droplist.config(width=15)
c.set("select your Budget")
droplist.grid(column=2,row=2, sticky=E)

label20 = tk.Label(text="Percentage in 12th")
label20.grid(column=1, row=3, sticky=E)

list3 = ['Above 90%', 'Above 80%', 'Above 70%','Above 65%',]
droplist = OptionMenu(window,b, *list3)
droplist.config(width=15)
b.set("select your Percentage")
droplist.grid(column=2,row=3, sticky=E)

label21 = tk.Label(text="Course Requirement")
label21.grid(column=1, row=4, sticky=E)


list3 = ['B.Tech', 'B.Sc', 'BCA','BBA','B.Com']
droplist = OptionMenu(window,a, *list3)
droplist.config(width=15)
a.set("select your Required Subject")
droplist.grid(column=2,row=4, sticky=E)


addbutton1 = Button(window, text="Submit", width=6, bg='black', fg='white', command=ok).grid(row=10, column=2, sticky=W)
window.mainloop()

