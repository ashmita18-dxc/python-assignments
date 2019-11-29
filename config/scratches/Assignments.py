import xml.dom.minidom
import pymysql
db = pymysql.connect("localhost","root","","test" )
cursor = db.cursor()
root=xml.dom.minidom.parse("C://Users//asarkar34//Downloads//DXCTraining//Examples//11SampleModules//xml//sax//users.xml")
users=root.documentElement
f=""
l=""
'''
for user in users.getElementsByTagName('user'):
	fname=user.getElementsByTagName('fname')[0]		#user se fname(elementnode) extract kar rahe;fname has only one branch which returns a list with one element[0]
	f = fname.childNodes[0].data					#fname has a (textnode) branch, which contains one value-->it can be extracted by .data at index [0](only on elist element)
	lname=user.getElementsByTagName('lname')[0]
    l = lname.childNodes[0].data
    print(f,l)
    data = cursor.execute("""INSERT INTO CRICKET(FNAME,
                        LNAME)
                        VALUES (f.format(*, l.format)""")
    db.commit()
    db.close()
'''


'''data=cursor.execute("""CREATE TABLE CRICKET (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20) NOT NULL,
         CITY CHAR(10)) """)'''
'''data=cursor.execute("""INSERT INTO CRICKET(FNAME,
         LNAME)
         VALUES (f.format(*, l.format)""")'''
db.commit()
db.close()

#Assignment2
from tkinter import *

root = Tk()
text = Text(root)
Label(root, text='First Name').grid(row=0)
Label(root, text='Last Name').grid(row=1)
name1= StringVar()
e1 = Entry(root, textvariable= name1)
name2= StringVar()
e2 = Entry(root,textvariable=name2)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#for gender
var = IntVar()      #The Variable Classes (BooleanVar, DoubleVar, IntVar, StringVar)
Label(root, text='Gender: ').grid(row=2)
R1 = Radiobutton(root, text = "Female", variable = var, value = 1)
R2 = Radiobutton(root, text = "Male", variable = var, value = 2)
R1.grid(row=2, column=1)
R2.grid(row=2, column=2)

Button(root, text='Submit',width=20,bg='brown',fg='white').grid(row=3,column=1)
root.mainloop()
print("Registration successful!!")
print(name1.get()+" "+name2.get())
def sel():
   selection = "Gender: " + str(var.get())
   label.config(text = selection)
label = Label(root)
label.pack()





