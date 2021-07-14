from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
#from tkinter.messagebox import showinfo




def connect():
    conn = sqlite3.connect("Nadding_course.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course_list(COLNAME TEXT,CNAME TEXT,No_of_Yrs TEXT,FEES TEXT,COMPULSORY_SUBS TEXT,CUTOFF_PERCENT TEXT)")
    conn.commit()
    conn.close()



t_n='addfinal_course'
c2='CNAME'


root = tk.Tk()
menu =Menu(root)
root.config(menu=menu)

def View():
    conn = sqlite3.connect("addfinal_course.db")
    cur = conn.cursor()
    if entry1.get() == "B.TECH":
        cur.execute('SELECT * FROM addfinal_course WHERE CNAME="B.TECH"'
                #format(addfinal_course=t_n, CNAME=c2)
                    )

        a_rows = cur.fetchall()
        print(":CollegeName:CourseName:Durations:Fees:COMPLUSORYSUBJECT:MIN%:Mob of Rep:")
        print('(1):',a_rows)

    elif entry1.get() == "B.COM":
        cur.execute('SELECT * FROM addfinal_course WHERE CNAME="B.COM"'
                #format(addfinal_course=t_n, CNAME=c2)
                    )
        a_rows = cur.fetchall()
        print(":CollegeName:CourseName:Durations:Fees:COMPLUSORYSUBJECT:MIN%:Mob of Rep:")
        print('(1):', a_rows)

    elif entry1.get() == "LLM":
        cur.execute('SELECT * FROM addfinal_course WHERE CNAME="LLM"'
                    # format(addfinal_course=t_n, CNAME=c2)
                    )
        a_rows = cur.fetchall()
        print(":CollegeName:CourseName:Durations:Fees:COMPLUSORYSUBJECT:MIN%:Mob of Rep:")
        print('(1):', a_rows)

    elif entry1.get() == "BBA":
        cur.execute('SELECT * FROM addfinal_course WHERE CNAME="BBA"'
                    # format(addfinal_course=t_n, CNAME=c2)
                    )
        a_rows = cur.fetchall()
        print(":CollegeName:CourseName:Durations:Fees:COMPLUSORYSUBJECT:MIN%:Mob of Rep:")
        print('(1):', a_rows)

    elif entry1.get() == "MCA":
        cur.execute('SELECT * FROM addfinal_course WHERE CNAME="MCA"'
                    # format(addfinal_course=t_n, CNAME=c2)
                    )
        a_rows = cur.fetchall()
        print(":CollegeName:CourseName:Durations:Fees:COMPLUSORYSUBJECT:MIN%:Mob of Rep:")
        print('1):',a_rows)

    elif entry1.get() == "BCA":
        cur.execute('SELECT * FROM addfinal_course WHERE CNAME="BCA"'
                    # format(addfinal_course=t_n, CNAME=c2)
                    )
        a_rows = cur.fetchall()
        print(":CollegeName:CourseName:Durations:Fees:COMPLUSORYSUBJECT:MIN%:Mob of Rep:")
        print('(1):', a_rows)

    elif entry1.get() == "BBM":
        cur.execute('SELECT * FROM addfinal_course WHERE CNAME="BBM"'
                    # format(addfinal_course=t_n, CNAME=c2)
                    )
        a_rows = cur.fetchall()
        print(":CollegeName:CourseName:Durations:Fees:COMPLUSORYSUBJECT:MIN%:Mob of Rep:")
        print('(1):', a_rows)
    else:
        print("INVALID")
    conn.close()

'''def View():
    conn = sqlite3.connect("addfinal_course.db")
    cur = conn.cursor()
    #cur.execute("SELECT * FROM adding_course")
    #cur.execute("SELECT addfinal_course.COLNAME from addfinal_course ")
    cur.execute("SELECT * FROM addfinal_course")
    # cur.execute("SELECT * FROM  course_list WHERE COLNAME='bca'")
    rows = cur.fetchall()
    columns = cur.fetchall()
    tree = ttk.Treeview(root, column=("column", "column1"))
    for row in rows:
        print(row)
    tree.insert(" ", tk.END, values=rows)

    for column in columns:
        print(column)
    tree.insert(" ", tk.END, values=columns)
    conn.close()
connect()
#def get_results():
#    print("ok i wont")


root.title('welcome')
tree=ttk.Treeview(root, column=("column","column1"))
tree.heading("#0", text = "COLLEGE NAME")
tree.heading("#1", text = "COURSE NAME")
tree.heading("#2", text = "NUMBER_OF_YEARS")
#tree.heading("#3", text = "FEES")
#tree.heading("#4", text = "COMPULSORY_SUBJECTS")
#tree.heading("#5", text = "CUT-OFF_%")
tree.grid()'''


'''class MenuFrame(Frame):
    def __init__(self,master):
        super().__init__(master)'''

'''S = Scrollbar(root)
T = Text(root, height=10, width=250,bg='skyblue')
S.config(command=T.yview)
def BBA():
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)

    T.config(yscrollcommand=S.set)
    quote = """
               :          COLLEGE NAME           :                 COURSE NAME                    :  DURATIONS :   FEES         :
               : PES University                  : BBA                                            : 3 Years    : 4.80 Lakhs     :
               : PES University                  : BBA Hospitality& Event MGT                     : 3 Years    : 4.80 Lakhs     :
               : PES University                  : BBA LLB Hons Integrated                        : 5 Years    : 4 Lakhs        :
               : Christ University               : BBA Hons                                       : 3 Years    : 2.55Lakhs      :
               : Christ University               : BBA Industry Integrated                        : 3 Years    : 2.25Lakhs      :
               : REVA University                 : BBA LLB Hons                                   : 5 Years    : 4.75 Lakhs     :
               : REVA University                 : BBA Hons                                       : 3 Years    : 2.55 Lakhs     :
               : REVA University                 : BBA Industry Integrated                        : 3 Years    : 2.25 Lakhs     :
    """
    T.insert(END, quote)
S.config(command=T.yview)


def BCOM_contents():
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)

    T.config(yscrollcommand=S.set)
    quote = """
:          College Name           :                 Course Name                    :  Durations :   Total Fees   :
: Christ University               : BCOM                                           : 3 Years    : 1.30 Lakhs     :
: Christ University               : BCOM Hons                                      : 3 Years    : 2.76 Lakhs     :
: Christ University               : BCOM Finance and Accountancy                   : 3 Years    : 2.07Lakhs      :
: Christ University               : BCOM International Finance                     : 3 Years    : 6.90Lakhs      :
: Christ University               : BCOM Professional                              : 3 Years    : 5.52Lakhs      :
: REVA University                 : BCOM Hons                                      : 3 Years    : 2.55 Lakhs     :
: REVA University                 : BCOM Industry Integrated                       : 3 Years    : 2.25 Lakhs     :
                      : 3 Years    : 2.25 Lakhs     :
       """
    T.insert(END, quote)'''


def BBA_contents():
    win = tk.Toplevel()
    win.wm_title("Window")
    win.geometry("1000x400")

    l = tk.Label(win, text="""
                :          College Name           :                 Course Name                    :  Durations :   Total Fees:Location   : URL
                : PES University                  : BBA                                            : 3 Years    : 4.80 Lakhs:Bangalore     :http://pes.edu/
                : PES University                  : BBA Hospitality& Event MGT                     : 3 Years    : 4.80 Lakhs :Bangalore     :http://pes.edu/
                : PES University                  : BBA LLB Hons Integrated                        : 5 Years    : 4 Lakhs   :Bangalore      :http://pes.edu/
                : Christ University               : BBA Hons                                       : 3 Years    : 2.55Lakhs :Bangalore      :https://christuniversity.in/
                : Christ University               : BBA Industry Integrated                        : 3 Years    : 2.25Lakhs :Bangalore      :https://christuniversity.in/
                : REVA University                 : BBA LLB Hons                                   : 5 Years    : 4.75 Lakhs:Bangalore      :https://reva.edu.in/
                : REVA University                 : BBA Hons                                       : 3 Years    : 2.55 Lakhs:Bangalore      :https://reva.edu.in/
                : REVA University                 : BBA Industry Integrated                        : 3 Years    : 2.25 Lakhs :Bangalore     :https://reva.edu.in/
                """)#,bg="black",fg="white")

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="OKAY", command=win.destroy)
    b.grid(row=1, column=0)



def BCOM_contents():
    win = tk.Toplevel()
    win.wm_title("Window")
    win.geometry("700x400")
    l = tk.Label(win, text="""
    :          College Name           :                 Course Name                    :   Durations   :   Total Fees :Location    : URL
    :    Christ University            :       BCOM                                     :   3 Years     :   1.30 Lakhs :Bangalore    :https://christuniversity.in/
    :    Christ University            :       BCOM Hons                                :   3 Years     :   2.76 Lakhs :Bangalore    :https://christuniversity.in/
    :    Christ University            :       BCOM Finance and Accountancy             :   3 Years     :   2.07Lakhs:Bangalore      :https://christuniversity.in/
    :    Christ University            :       BCOM International Finance               :   3 Years     :   6.90Lakhs :Bangalore     :https://christuniversity.in/
    :    Christ University            :       BCOM Professional                        :   3 Years     :   5.52Lakhs :Bangalore     :https://christuniversity.in/
    :    REVA University              :       BCOM Hons                                :   3 Years     :   2.55 Lakhs     :https://reva.edu.in/
    :    REVA University              :       BCOM Industry Integrated                 :   3 Years     :   2.25 Lakhs     :https://reva.edu.in/

               """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def MCOM_self():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
            :          College Name           :                 Course Name                    :  Durations :   Total Fees:Location   : URL
            : Christ University               : BCOM Hons                                      : 3 Years    : 2.76 Lakhs :Bangalore     :https://christuniversity.in/
            : Christ University               : BCOM Finance and Accountancy                   : 3 Years    : 2.07Lakhs  :Bangalore     :https://christuniversity.in/
            : Christ University               : BCOM International Finance                     : 3 Years    : 6.90Lakhs  :Bangalore     :https://christuniversity.in/
            : Christ University               : BCOM Professional                              : 3 Years    : 5.52Lakhs  :Bangalore     :https://christuniversity.in/
            : REVA University                 : BCOM Hons                                      : 3 Years    : 2.55 Lakhs :Bangalore     :https://reva.edu.in/
            : REVA University                 : BCOM Industry Integrated                       : 3 Years    : 2.25 Lakhs :Bangalore     :https://reva.edu.in/
            """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def MBA():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
:          College Name           :                 Course Name                    :  Durations :   Total Fees   : Locations :URL
: PES University                  : MBA                                            : 2 Years    : 8 Lakhs        : Bangalore :http://pes.edu/
: Christ University               : MBA Executive                                  : 2 Years    : 3.52 Lakhs     : Bangalore :https://christuniversity.in/
: Christ University               : MBA Financal MGT                               : 2 Years    : 7.54Lakhs      : Bangalore :https://christuniversity.in/
: Christ University               : MBA International Business                     : 2 Years    : 7.82Lakhs      : Bangalore :https://christuniversity.in/
: Christ University               : MBA Leadership & MGT                           : 2 Years    : 4.20Lakhs      : Bangalore :https://christuniversity.in/
: Christ University               : MBA Tourism MGT                                : 2 Years    : 3.38 Lakhs     : Bangalore :https://christuniversity.in/
:    IAME                         : MBA in Marketing Management                    : 2 Years    : 1.71 Lakhs     : Bangalore : http://www.iame.org.in/
:    IAME                         : MBA in Finance Management                      : 2 Years    : 1.71 Lakhs     : Bangalore : http://www.iame.org.in/
:    IAME                         : MBA in Human Resources Management              : 2 Years    : 1.71 Lakhs     : Bangalore : http://www.iame.org.in/
:    IAME                         : MBA International Business                     : 2 Years    : 1.71 Lakhs     : Bangalore : http://www.iame.org.in/
: Asia-Pacific Institute of Mngt  : MBA Leadership & MGT                           : 2 Years    : 4.20Lakhs      : New Delhi :
: Symbiosis Group Of Institutes   : MBA in Operations                              : 2 Years    : 8.53  Lakhs    : Pune      : https://siu.edu.in/about-us.php
: Symbiosis Group Of Institutes   : MBA in Human Resource Management               : 2 Years    : 8.53  Lakhs    : Pune      : https://siu.edu.in/about-us.php
: Symbiosis Group Of Institutes   : MBA in Marketing Management                    : 2 Years    : 8.53  Lakhs    : Pune      : https://siu.edu.in/about-us.php
: Symbiosis Group Of Institutes   : MBA in Financial Management                    : 2 Years    : 8.53  Lakhs    : Pune      : https://siu.edu.in/about-us.php
: Symbiosis Group Of Institutes   :MBA in Innovation & Entrepreneurship            : 2 Years    : 6.6  Lakhs    : Pune       : https://siu.edu.in/about-us.php



 """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def BE():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
      :          College Name           :                 Course Name                    :  Durations : Total Fees   : Location        :        URL                   :
      : Bangalore University            : BE Electronical & Electronics Engineering      : 4 Years    : 88000        : Bangalore       :  http://bangaloreuniversity.ac.in/
      : Bangalore University            : BE Computer Science & Engineering              : 4 Years    : 8800         :   Bangalore     :  http://bangaloreuniversity.ac.in/
      : Bangalore University            : BE Civil Engineering                           : 4 Years    : 88000        :    Bangalore    :  http://bangaloreuniversity.ac.in/
      : Bangalore University            : BE Electronics & Communication Engineering     : 4 Years    : 90000        :   Bangalore     :  http://bangaloreuniversity.ac.in/
      : Bangalore University            : BE Information Science & Engineering           : 4 Years    : 88000        :   Bangalore     :  http://bangaloreuniversity.ac.in/
      : Bangalore University            : BE Mechanical Engineering Part time            : 3 Years    : 73000        :   Bangalore     :  http://bangaloreuniversity.ac.in/
      : Birla Institute of Technology   : B.E in Biotechnology                           : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
      : Birla Institute of Technology   : B.E in Computer Science Engineering            : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
       :Birla Institute of Technology   : B.E in Civil Engineering                       : 4 Years    : 1.08Lakhs    : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
      : Birla Institute of Technology   : B.E in Information Science                     : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
      : Birla Institute of Technology   : B.E in Chemical Engineering                    : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
      : Birla Institute of Technology   :B.E in Electrical & Electronics Engineering     : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
      : Birla Institute of Technology   :B.E in Electronics & Communication Engineering  : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
      : Birla Institute of Technology   : B.E in Mechanical                              : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
      : Birla Institute of Technology   :B.E in Chemical Engineering (Plastic & Polymer) : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
      : Birla Institute of Technology   : B.E in Production                              : 4 Years    : 29k          : Mersa, Ranchi   :  https://www.bitmesra.ac.in/
    """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def BA():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
        : Chandigarh University    : Bachelor of Fine Arts                              : 3 Years    : 35k          : Chandigarh
        : Amity University   :Bachelor of Fine Arts                            : 4 Years    : 53k          : Jaipur
                  """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def MSC():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
               :          College Name           :                 Course Name         :  Durations :   Total Fees   :Locations:   URL
    : Bangalore University            : M.Sc Mathematics                               : 2 Years    : 17000          : Bangalore:http://bangaloreuniversity.ac.in/
    : Bangalore University            : M.Sc physics                                   : 2 Years    : 17000          :Bangalore:http://bangaloreuniversity.ac.in/
    : Bangalore University            : M.Sc Zoology                                   : 2 Years    : 17000          :Bangalore:http://bangaloreuniversity.ac.in/
    : Bangalore University            : M.Sc Chemistry                                 : 2 Years    : 17000          :Bangalore:http://bangaloreuniversity.ac.in/
    : REVA University                 : M.Sc Physics                                   : 2 Years    : 74,000         : Bangalore:https://reva.edu.in/
    : REVA University                 : M.Sc Mathematics                               : 2 Years    : 74,000         : Bangalore:https://reva.edu.in/
    : REVA University                 : M.Sc Chemistry                                 : 2 Years    : 74,000         : Bangalore:https://reva.edu.in/
    : REVA University                 : M.Sc Biotechnology                             : 2 Years    : 1.70 Lakhs     : Bangalore:https://reva.edu.in/
    : REVA University                 : M.Sc Applied Mathematics                       : 4 Years    : 1.70 lakhs     : Bangalore:https://reva.edu.in/
    : REVA University                 : M.Sc Biochemistry                              : 2 Years    : 1.70 lakhs     : Bangalore :https://reva.edu.in/
                """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def MA():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
               :          College Name  :                 Course Name                    :  Durations :   Total Fees :Location      :URL
    : Chandigarh University             : M.A. in English                                : 2 Years    : 17000        :  Chandigarh  :http://www.cuchd.in/
    : Chandigarh University             : M.A. in punjabi                                : 2 Years    : 17000        :    Chandigarh:http://www.cuchd.in/
    : Chandigarh University             :M.A in Journalism and Mass Communication        : 2 Years    : 17000        :  Chandigarh  :http://www.cuchd.in/
    : Chandigarh University             :M.A in English                                  : 2 Years    : 17000        :    Chandigarh:http://www.cuchd.in/
    : Chandigarh University             : M.A in Psychology                              : 2 Years    : 74,000       :   Chandigarh :http://www.cuchd.in/
    : D Y Patil University              : M.A in Education                               : -          : 15k          :Navi Mumbai   :http://www.dypatil.edu/
    : LPU                   :M.A. (English)                                              : 2 Years    : 69k          : Jalandhar    :https://www.lpu.in/
    : LPU                  : M.A. (Punjabi)                                              : 2 Years    : 69k          :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Psychology)                                           : 4 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Sociology)                                            : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Fine Arts)                                            : 2 Years    :79k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Journalism & Mass Communication)                      : 2 Years    :1.39 Lacs     :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Hindi)                                                : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Music Vocal)                                          : 2 Years    :79k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Theatre and Television)                               : 2 Years    :79k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Applied Psychology)                                   : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Clinical Psychology)                                  : 2 Years    :99k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Political Science)                                    : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Public Administration)                                : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Geography)                                            : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Education))                                           : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (Education - Leadership & Management))                 : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : LPU                  : M.A. (History)                                              : 2 Years    :69k           :Jalandhar     :https://www.lpu.in/
    : Amity University     : M.A.in Film & TV Production                                 : 2 Years    :3.38 Lacs     : Noida        :http://www.amity.edu/
    : Amity University     : M.A. in Economics                                           : 2 Years    :	1.74 Lacs    : Noida        :http://www.amity.edu/
    : Amity University     : M.A. in English                                             : 2 Years    :1.62 Lacs     : Noida        :http://www.amity.edu/
    : Amity University     : M.A. in Fashion & Textile Merchandising                     : 2 Years    :1.94 Lacs     : Noida        :http://www.amity.edu/
    : VELS University      : M.A. in English                                             : 2 Years    :30k           : Chennai      :http://www.velsuniv.ac.in/
    : VELS University      : M.A. in indian Music                                        : 2 Years    :25k           : Chennai      :http://www.velsuniv.ac.in/
    : VELS University      : M.A. in Bharatanatyam                                       : 3 Years    :20k           : Chennai      :http://www.velsuniv.ac.in/
    : VELS University      : M.A. in Astrology                                           : 3 Years    :25k           :Chennai       :http://www.velsuniv.ac.in/

                """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def BTech():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :          College Name           :                    Course Name                      :  Durations :   Total Fees :Location  :  URL
    : PES COLLEGE                     : B.Tech Computer Science and Engineering             : 4 Years    : 12.80 Lakhs  :Bangalore :http://pes.edu/
    : PES COLLEGE                     : B.Tech Electronics and Communication Engineering    : 4 Years    : 12.80 Lakhs  :Bangalore :http://pes.edu/
    : PES COLLEGE                     : B.Tech Computer Science and Engineering             : 4 Years    : 12.80 Lakhs  :Bangalore :http://pes.edu/
    : PES COLLEGE                     : B.Tech Mechanical Engineering                       : 4 Years    : 12.80 Lakhs  :Bangalore :http://pes.edu/
    : PES COLLEGE                     : B.Tech Electrical and Electronics Engineering       : 4 Years    : 12.80 Lakhs  :Bangalore :http://pes.edu/
    : PES COLLEGE                     : B.Tech Biotechnology Engineering                    : 4 Years    : 12.80 Lakhs  :Bangalore :http://pes.edu/
    : PES COLLEGE                     : B.Tech Civil Engineering                            : 4 Years    : 12.80 Lakhs  :Bangalore :http://pes.edu/
    : CHRIST University               : B.Tech Mechanical Engineering                       : 4 Years    : 7.90 Lakhs   :Bangalore :https://christuniversity.in/
    : CHRIST University               : B.Tech Computer Science and Engineering             : 4 Years    : 7.90 Lakhs   :Bangalore :https://christuniversity.in/
    : CHRIST University               : B.Tech Automobile Engineering                       : 4 Years    : 7.90 Lakhs   :Bangalore :https://christuniversity.in/
    : CHRIST University               : B.Tech Civil Engineering                            : 4 Years    : 7.90 Lakhs   :Bangalore :https://christuniversity.in/
    : CHRIST University               : B.Tech Electrical and Electronics Engineering       : 4 Years    : 7.90 Lakhs   :Bangalore :https://christuniversity.in/
    : CHRIST University               : B.Tech Electronics and Communication Engineering    : 4 Years    : 7.90 Lakhs   :Bangalore :https://christuniversity.in/
    : CHRIST University               : B.Tech Information Technology                       : 4 Years    : 7.90 Lakhs   :Bangalore :https://christuniversity.in/
    : REVA University                 : B.Tech Civil Engineering                            : 4 Years    : 9 Lakhs      :Bangalore :https://reva.edu.in/
    : REVA University                 : B.Tech Computer Science and Engineering             : 4 Years    : 12 Lakhs     :Bangalore :https://reva.edu.in/
    : REVA University                 : B.Tech Electrical and Electronics Engineering       : 4 Years    : 8 Lakhs      :Bangalore :https://reva.edu.in/
    : REVA University                 : B.Tech Electronics and Communication Engineering    : 4 Years    : 11 Lakhs     :Bangalore :https://reva.edu.in/
    : REVA University                 : B.Tech Mechanical Engineering                       : 4 Years    : 10 lakhs     :Bangalore :https://reva.edu.in/

                        """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def MTech():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
:        College Name        :                    Course Name                      :  Durations :   Total Fees:Location      :  URL
: PES COLLEGE                : M.Tech Biotechnology Engineering                    : 2 Years    : 6 Lakhs      :  Bangalore  :http://pes.edu/
: PES COLLEGE                : M.Tech Civil Engineering                            : 2 Years    :  6 Lakhs     :  Bangalore  :http://pes.edu/
: PES COLLEGE                : M.Tech Computer Science and Engineering             : 2 Years    : 6 Lakhs      :  Bangalore  :http://pes.edu/
: PES COLLEGE                : M.Tech Electrical and Electronics Engineering       : 2 Years    : 6 Lakhs      :  Bangalore  :http://pes.edu/
: PES COLLEGE                : M.Tech Electronics and Communication Engineering    : 2 Years    : 6 Lakhs      :  Bangalore  :http://pes.edu/
: PES COLLEGE                : M.Tech Mechanical Engineering                       : 2 Years    : 6 Lakhs      :  Bangalore  :http://pes.edu/
: REVA University            : M.Tech Advanced Power Electronics                   : 2 Years    : 3.20 Lakhs   :  Bangalore  :https://reva.edu.in/
: CHRIST University          : M.Tech Communication Systems                        : 2 Years    : 2.64 Lakhs   :  Bangalore  :https://christuniversity.in/
: CHRIST University          : M.Tech Computer Science and Engineering             : 2 Years    : 2.64 Lakhs   :  Bangalore  :https://christuniversity.in/
: CHRIST University          : M.Tech Information Technology                       : 2 Years    : 2.64 Lakhs   :  Bangalore  :https://christuniversity.in/
: CHRIST University          : M.Tech Machine Design                               : 2 Years    : 2.64 Lakhs   :  Bangalore  :https://christuniversity.in/
: CHRIST University          : M.Tech Power Systems                                : 2 Years    : 2.64 Lakhs   :  Bangalore  :https://christuniversity.in/
: CHRIST University          : M.Tech Structural Engineering                       : 2 Years    : 2.64 Lakhs   :  Bangalore  :https://christuniversity.in/
: REVA University            : M.Tech Mechanical Engineering                       : 4 Years    : 10 lakhs     :  Bangalore  :https://reva.edu.in/
                    """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def MCA():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
       :          College Name           :                    Course Name                      :  Durations :   Total Fees   :
        : AIM                            : MCA                                                 : 2 Years    : 30k        :

                    """)

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)



def BPT():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :   College Name                  :                    Course Name                 :  Durations :   Total Fees   : Location
    : Lovely Professional University  : Bachelor of Physiotherapy (BPT)                : 4 Years    : 1.29 Lakhs     : Jalandhar:https://www.lpu.in/
    : Lovely Professional University  : Bachelor of Physiotherapy (BPT) [Lateral Entry]: 3 Years    : 1.29 Lakhs     : Jalandhar:https://www.lpu.in/
    : VELS University                 : B.P.T                                          : 42 Months  :  80K           : Chennai:http://www.velsuniv.ac.in/
    : K. R. Mangalam University       : Bachelor of Physiotherapy (B.P.T.)             : 54 Months  :  1.21 Lakhs    : Gurgaon:
    : AIM                             : PGDM in Banking and Financial Services (PGDM- BFS): 2 Years : 4.85 Lakhs     : New Delhi:http://krmangalam.edu.in/
    : Symbiosis Group Of Institutes   : PGDM in Innovation & Corporate Entrepreneurship: 12.0 Months: 83 K           : Pune:- https://siu.edu.in/about-us.php
    : Symbiosis Group Of Institutes   : PGDM in Operations Management  : 2 Years       : 12.0 Months: 83 K           : Pune:- https://siu.edu.in/about-us.php
    : Symbiosis Group Of Institutes   : PGDM in Marketing Management (PGDM- BFS)       : 12.0 Months: 83 K           : Pune:- https://siu.edu.in/about-us.php
    : Symbiosis Group Of Institutes   : PGDM in Human resource managment               : 12.0 Months: 83 K           : Pune:- https://siu.edu.in/about-us.php
    : Symbiosis Group Of Institutes   : PGDM in Finance                                : 12.0 Months: 83 K           : Pune:- https://siu.edu.in/about-us.php




""")

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)




def PGDM():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :   College Name                  :                    Course Name                      :  Durations :   Total Fees   : Location
    : IAME                            : PGDM                                                : 2 Years    : 1.91 Lakhs     : Lucknow: http://www.iame.org.in/
    : AIM                             : PGDM General                                        : 2 Years    : 4.85 Lakhs     : New Delhi
    : AIM                             : PGDM in Marketing                                   : 2 Years    :  4.85 Lakhs    : New Delhi
    : AIM                             : PGDM in International Business (PGDM- IB)           : 2 Years    :  4.85 Lakhs    : New Delhi
    : AIM                             : PGDM in Banking and Financial Services (PGDM- BFS)  : 2 Years    : 4.85 Lakhs     : New Delhi
    : Symbiosis Group Of Institutes   : PGDM in Innovation & Corporate Entrepreneurship     : 12.0 Months: 83 K           : Pune:http://www.velsuniv.ac.in/
    : Symbiosis Group Of Institutes   : PGDM in Operations Management  : 2 Years            : 12.0 Months: 83 K           : Pune:http://www.velsuniv.ac.in/
    : Symbiosis Group Of Institutes   : PGDM in Marketing Management (PGDM- BFS)            : 12.0 Months: 83 K           : Pune:http://www.velsuniv.ac.in/
    : Symbiosis Group Of Institutes   : PGDM in Human resource managment                    : 12.0 Months: 83 K           : Pune:http://www.velsuniv.ac.in/
    : Symbiosis Group Of Institutes   : PGDM in Finance                                     : 12.0 Months: 83 K           : Pune:http://www.velsuniv.ac.in/




""")

    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def LLM():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :   College Name                  :                    Course Name                      :  Durations :   Total Fees   : Location:URL
    : Amity University                : LLM                                                 : 1 Years    : 58k            : Lucknow:https://www.lpu.in/
    : Mangalayatan University         : LLM                                                 : 1 Years    : 50k            : Aligarh: http://mangalayatan.in/
    : Amity University                : LLM                                                 : 1 Years    : 56K            : Jaipur:https://www.lpu.in/
    : K. R. Mangalam University       : LLM                                                 : 1 Years    : 1.43 Lakhs     : Gurgaon:http://krmangalam.edu.in/
    : Amity University                : LLM in (Business Law)                               : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (Constitutional Law)                         : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (Corporate Banking & Insurance Law)          : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (Criminal Law)                               : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (Family Law)                                 : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (Human Rights)                               : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (Intellectual Property)                      : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (International Environmental Law)            : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (International Trade & Economic Law)         : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : Amity University                : LLM in (Media & Entertainment Law)                  : 1 Years    : 82 K           : Noida:http://www.amity.edu/
    : LPU                             : LLM                                                 : 1 Years    : 1.19Lakhs      : Jalandhar:https://www.lpu.in/


""")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)




def BSC():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :   College Name                  :                    Course Name                :  Durations :   Total Fees   : Location  :URL
    : Birla Institute of Technology   : B.Sc.in Animation & Multimedia                : 3 Years    : 1.24 Lakhs     : Noida     :https://www.bitmesra.ac.in/
    : D Y Patil  University           : Basic B.Sc Nursing                            : 4 Years    : 55K            : Navi Mumbai:https://www.lpu.in/
    :D Y Patil  university            :B.Sc in Hotel Mngt Catering & Travel Operations: 3 Years    : 10K            : Navi Mumbai:https://www.lpu.in/
    : D Y Patil  University           : B.Sc in (Exercise Sciences) – 3 Years         : 3 Years    : 1 Lakhs        : Navi Mumbai:https://www.lpu.in/
    : D Y Patil  University           : Post Basic B.Sc. Nursing                      : 2 Years    : 55K            : Navi Mumbai:https://www.lpu.in/
    : D Y Patil  University           : B. Sc In Bioinformatics                       : 3 Years    : 2.35Lakhs      : Navi Mumbai:https://www.lpu.in/
    : D Y Patil  University           : B.Sc Culinary Studies                         : 3 Years    : 2 Lakhs        : Navi Mumbai:https://www.lpu.in/
    : D Y Patil  University            : B.Sc in Hospitality Studies                  : 3 Years    : 1.29 Lakhs     : Navi Mumbai:https://www.lpu.in/
    : Lovely Professional University   : B.Sc. (Design - Fashion) [Lateral Entry]     : 2 Years    : 1.49 Lakhs     : Jalandhar  :https://www.lpu.in/
    : Lovely Professional University   : B.Sc. (Information Technology)               : 3 Years    : 1.09 Lakhs     : Jalandhar  :https://www.lpu.in/
    : Lovely Professional University   : B.Sc. (Hotel Management)                     : 3 Years    : 1.39 Lakhs     : Jalandhar  :https://www.lpu.in/
    : Amity University   :B.Sc. + M.Sc. - Actuarial Science                           : 5 Years    : 5.9 Lakhs      :  Noida     :http://www.amity.edu/
    : Amity University    : B.Sc. (Hons.) - Anthropology                              : 3 Years    : 30K            : Noida      :http://www.amity.edu/







""")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def MPHIL():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :   College Name                  :                    Course Name                     :  Durations :   Total Fees   : Location:URL
    : Amity University                : M.Phil(Child & Adolescent Psychology)              : 2 Years    : 58k            : Lucknow: http://www.amity.edu/
    : Amity University                :M.Phil (Clinical Psychology)                        :     -      : 66k            : Lucknow: http://www.amity.edu/
    :Amity University                 : M. Phil (Clinical Psychology)                      : 2 Years    : 1 Lakhs        : Noida: http://www.amity.edu/
    : Amity University                : M.Phil in Anthropology                             : 18 Months  : 1.4 Lakhs      : Noida: http://www.amity.edu/
    : Amity University                :Phil in English                                     : 18 Months  : 1.46 Lakh      : Noida: http://www.amity.edu/
    l.grid(row=0, column=0)
""")
    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def BFA():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :   College Name                  :                    Course Name                 :  Durations :   Total Fees : Location     : URL
    : Amity University                : BFA                                            : 4 Years    : 58K           : Lucknow     :http://www.amity.edu/
    : Amity University                : BFA (Animation)                                : 4 Years    : 69K           : Lucknow     :http://www.amity.edu/
    : PIET                            : BFA (Animation & VFX)                          : 3 Years    : 90K           : Jaipur      :http://www.piet.poornima.org/
    : Lovely Professional University  : Bachelor of Physiotherapy (BPT)                : 4 Years    : 1.29 Lakhs    : Jalandhar   :https://www.lpu.in/
    : Lovely Professional University  : Bachelor of Physiotherapy (BPT) [Lateral Entry]: 3 Years    : 1.29 Lakhs    : Jalandhar   :https://www.lpu.in/
    : Lovely Professional University  : Bachelor of Fine Arts (BFA)                    : 4 Years    : 79K           : Jalandhar   :https://www.lpu.in/

""")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def PHD():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :   College Name                  :                    Course Name                  :  Durations :   Total Fees   : Location:URL
    : Lovely Professional University  : Ph.D. (Computer Science & Engineering)          : 3 Years    : 99K    : Jalandhar:https://www.lpu.in/
    : Lovely Professional University  : Ph.D. (Electronics & Communication Engineering) : 3 Years    : 89K     : Jalandhar:https://www.lpu.in/
    :Lovely Professional university   : Ph.D. (Electrical Engineering)                  : 3 Years    : 89K     : Jalandhar:https://www.lpu.in/
    : Lovely Professional University  : Ph.D. (Mechanical Engineering)                  : 3 Years    : 89K     : Jalandhar:https://www.lpu.in/
    : Lovely Professional University  : Ph.D. (Civil Engineering)                       : 3 Years    : 89K     : Jalandhar:https://www.lpu.in/
    : Lovely Professional University  : Ph.D. (Chemical Engineering)                    : 3 Years    : 99K     : Jalandhar:https://www.lpu.in/
    : Lovely Professional University  : Ph.D. (Civil Engineering)                       : 3 Years    : 89K     : Jalandhar:https://www.lpu.in/
    : Invertis University             : Ph.D. in Management                             : 2 Years    : 50K     : Bareilly :
    : Invertis University             : Ph.D. in Computer Science & Engineering         : 2 Years    : 50K     : Bareilly :
    : Invertis University             : Ph.D. in Pharmacy                               : 2 Years    : 50K     : Bareilly :
    : Invertis University             : Ph.D. in Law                                    : 2 Years    : 50K     : Bareilly :



""")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)




def LLB():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="""
    :   College Name                  :                    Course Name                      :  Durations :   Total Fees   : Location:URL
    : Amity University                : LLB                                                 : 3 Years    : 1.17 Lakhs     : Lucknow:http://www.amity.edu/
    : VELS University                 : LLB                                                 : 3 Years    : 1.5 Lakhs      : Chennai:http://www.velsuniv.ac.in/
    :Invertis university              : LLB                                                 : 3 Years    : 35K            : Bareilly
    : Amity University                : LLB                                                 : 3 Years    : 1.65 Lakhs     : Noida:http://www.amity.edu/
    : Lovely Professional University  : LLB                                                 : 3 Years    : 1.29 Lakhs     : Jalandhar:https://www.lpu.in/
""")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)



#homeMenu = Menu(menu)
#menu.add_cascade(label="    HOME   ", menu=homeMenu)
#engMenu = Menu(menu)



manMenu = Menu(menu)
menu.add_cascade(label="  MANAGEMENT  ", menu=manMenu)
manMenu.add_command(label="BBA", command=BBA_contents)  # command=doNothing)
manMenu.add_command(label="BBM", )  # command=doNothing)
manMenu.add_command(label="MBA",command= MBA )
manMenu.add_command(label="PGDM", command=PGDM)
manMenu.add_command(label="EXECUTIVE MBA", )

engMenu = Menu(menu)
menu.add_cascade(label="   ENGINEERING   ", menu=engMenu)
engMenu.add_command(label="BE",command=BE)
engMenu.add_command(label="B.TECH",command=BTech)
engMenu.add_command(label="ME")
engMenu.add_command(label="M.TECH",command=MTech)

medMenu = Menu(menu)
menu.add_cascade(label="    MEDICAL    ", menu=medMenu)
medMenu.add_command(label="BAMS")
medMenu.add_command(label="B.SC",command=BSC)
medMenu.add_command(label="BHMS")
medMenu.add_command(label="BPT",command=BPT)

artMenu = Menu(menu)
menu.add_cascade(label="    ARTS    ", menu=artMenu)
artMenu.add_command(label="BA",command=BA)
artMenu.add_command(label="BFA",command=BFA)
artMenu.add_command(label="MA",command=MA)
artMenu.add_command(label="M.PHIL",command=MPHIL)
artMenu.add_command(label="PH.D")

lawMenu = Menu(menu)
menu.add_cascade(label="    LAWS    ", menu=lawMenu)
lawMenu.add_command(label="LLB",command=LLB)
lawMenu.add_command(label="LLM",command=LLM)
#lawMenu.add_command(label="LLD")

scienceMenu = Menu(menu)
menu.add_cascade(label="    SCIENCE    ", menu=scienceMenu)
scienceMenu.add_command(label="B.SC",command=BSC)
scienceMenu.add_command(label="M.SC",command= MSC)

commerceMenu = Menu(menu)
menu.add_cascade(label="    COMMERCE    ", menu=commerceMenu)
commerceMenu.add_command(label="B.COM",command=BCOM_contents)
commerceMenu.add_command(label="M.COM",command=MCOM_self)

comMenu = Menu(menu)
menu.add_cascade(label="  COMPUTER APPLICATION   ", menu=comMenu)
comMenu.add_command(label="BCA",)
comMenu.add_command(label="MCA",command=MCA)


abtMenu = Menu(menu)
menu.add_cascade(label="   ABOUT US   ", menu=abtMenu)

moreMenu = Menu(menu)
menu.add_cascade(label="   MORE   ", menu=moreMenu)






label1 = ttk.Label(root, text='Query')
label1.pack(padx=5,pady=5)
entry1 = ttk.Entry(root, width=50)
entry1.pack(padx=5,pady=5)






MyButton1 = ttk.Button(root, text='Search',command=View, width=10).pack(padx=5,pady=5)
# it acts same way as search button
entry1.bind('<Return>')


root.config(bg='skyblue')
root.mainloop()









#def line(event):
 #   canvas.create_line(15,15,event.x, event.y)5

#canvas = tk.Canvas(root, bg='skyblue',)
#canvas.grid()

#root.bind("<Button-1>", line)







'''
btn2 = tk.StringVar()
def callback():
    if btn2.get() == 'google':
      webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'duck':
      webbrowser.open('http://duckduckgo.com/search?q=' + entry1.get())

def get(event):
    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q=' + entry1.get())
    elif btn2.get() == 'duck':
        webbrowser.open('http://duckduckgo.com/search?q=' + entry1.get())



MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
MyButton2.grid(row=1, column=1)

MyButton3 = ttk.Radiobutton(root, text='Duck', value="duck", variable=btn2)
MyButton3.grid(row=1, column=2)

root.wm_attributes('-topmost', 1)'''