from tkinter import *
import sqlite3
from tkinter import messagebox

with sqlite3.connect("page.db") as db:
    cursur = db.cursor()
cursur.execute("CREATE TABLE IF NOT EXISTS logs(username TEXT NOT NULL, password TEXT NOT NULL);")
cursur.execute("SELECT * FROM logs")
db.commit()
db.close()

class Main:
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def login(self):
         with sqlite3.connect("page.db") as db:
             cursur = db.cursor()
         find_user = ("SELECT * FROM logs WHERE username = ? AND password = ?")
         cursur.execute(find_user,[(self.username.get()),(self.password.get())])
         results = cursur.fetchall()
         if results:
             self.logf.pack_forget()
             self.head["text"] = self.username.get() + "\n  you have successfully LOGGED IN"
             self.head['pady'] = 150
         else:
              messagebox.showinfo("-- ERROR --","Oops!! username not matched", icon="error")

    def new_user(self):
        with sqlite3.connect("page.db") as db:
              cursur = db.cursor()
        find_user = ("SELECT * FROM logs WHERE username = ?")
        cursur.execute(find_user,[(self.username.get())])
        if cursur.fetchall():
            messagebox.showinfo("-- ERROR --","username already exists", icon="error")
        else:

            messagebox.showinfo("-- COMPLETE --","account created successfully!!", icon="info")
            self.log()
            insert = 'INSERT INTO logs(username,password) VALUES(?,?)'
            cursur.execute(insert,[(self.n_username.get()),(self.n_password.get())])
            db.commit()

    def log(self):
           self.username.set("")
           self.password.set("")
           self.crf.pack_forget()
           self.head['text'] = "Login "
           self.logf.pack()

    def cr(self):
           self.n_username.set("")
           self.n_password.set("")
           self.head['text'] = "Create an Account"
           self.logf.pack_forget()
           self.crf.pack()


    def widgets(self):
        self.head = Label(self.master,text = " LOGIN TO COLLEGOPEDIA",font = ('bold',25),pady=40)
        self.head.pack()

        self.logf = Frame(self.master,padx = 10,pady = 10)
        Label(self.logf,text = "Username: ",font = ('freesansbold',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.logf,textvariable = self.username,bd=8,font  = ('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
        Label(self.logf,text = "Password: ",font = ('freesansbold',20),padx=5,pady=5).grid(row=1,column=0,sticky=W)
        Entry(self.logf,textvariable = self.password,bd=8, font = ('calibri',15,'bold'),show = "*").grid(row=1,column=1,sticky=E)
        Button(self.logf,text = " Login ",bd=7, font = ("monaco",15,'bold'),padx=5,pady=5,command=self.login).grid(row=2)
        Button(self.logf,text = " make new account ",bd=7, font = ("monaco",15,'bold'),padx=5, pady=5,command=self.cr).grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx = 10, pady = 10)
        Label(self.crf,text = "Username: ",font = ('freesansbold',20), padx=5,pady=5).grid(sticky=W)
        Entry(self.crf,textvariable = self.n_username,bd=8,font = ('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
        Label(self.crf,text = "Password: ",font = ('freesansbold',20),padx=5,pady=5).grid(row=1,column=0,sticky=W)
        Entry(self.crf,textvariable = self.n_password,bd=8,font = ('calibri',15,'bold'),show = "*").grid(row=1,column=1,sticky=E)
        Button(self.crf,text = "Go to Login ",bd=7, font = ("monaco",15,'bold'),padx=5,pady=5,command=self.log).grid(row=2)
        Button(self.crf,text = " Create Account ",bd=7, font = ("monaco",15,'bold'),padx=5,pady=5, command=self.new_user).grid(row=2,column=1)
        self.logf.pack()
root = Tk()
Main(root)
root.geometry("400x350+350+150")
root.mainloop()




