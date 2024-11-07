from collections import defaultdict
from logging import RootLogger
from multiprocessing.util import sub_debug
######## FIRST program ######
# from tkinter import  *
#
# first_root = Tk()
# lable = Label(text='FIRST WINDOW')
# lable.pack()
# first_root.geometry('900x750')
# first_root.minsize(200,200)
# first_root.maxsize(1000,1000)
# first_root.mainloop()


########### INSERTING IMAGE IN TO GUI ##########

from tkinter import *

from matplotlib.widgets import CheckButtons
from numpy.f2py.crackfortran import usermodules
from numpy.ma.extras import row_stack, column_stack

#from PIL import Image, ImageTk
#
#
# root = Tk()
# root.geometry('1250x900')
# image = Image.open('C:\\Users\\abhosage\\PycharmProjects\\Python_Pandas\\Tkinter_new\\images\\python-programming-2CFJA44.jpg')
# photo = ImageTk.PhotoImage(image)
# label = Label(image = photo)
# label.pack()
# root.mainloop()


########### Arguments in Lable  #########
# root = Tk()
# root.geometry('1300x500')
# root.title('welcome to TKINTER')
# # title_label = Label(text='''In this example, below Python code creates a Tkinter GUI window with a labeled text “Hello, World!”.
# # The label is styled with specific attributes such as font, color, and dimensions,
# # and it’s positioned at the center with a raised border.
# # Finally, the main event loop is started to display the GUI window until the user interacts with it.''',
# #                     background='orange', foreground='white', padx=30,pady=30, font=("Arial", 16, "bold"), relief=SUNKEN,
# #                     justify=CENTER)
# title_label = Label(text='READY',background='orange', foreground='white', padx=10,pady=10, font=("Arial", 6, "bold"), relief=SUNKEN,
#                     justify=CENTER)
# title_label.pack(side=BOTTOM,anchor=CENTER,fill=X,padx=10,pady=10)
# root.mainloop()


############## INSERTING FRAME #############

# root = Tk()
# root.geometry("500x500")
# f1 = Frame(root,background='grey',borderwidth=4,relief=SUNKEN)
# f1.pack(side=LEFT, fill=Y,anchor = CENTER)
# l = Label(f1, text='FRAME1',font=("Arial", 16, "bold"))
# l.pack(pady=250)
#
# f2 = Frame(root,background='grey',borderwidth=4,relief=SUNKEN)
# f2.pack(side=TOP, fill=X)
# l = Label(f2, text='FRAME2',font=("Arial", 16, "bold"),padx=20,pady=20)
# l.pack()
# root.mainloop()




###############   BUTTONS in GUI ##############

# root = Tk()
# root.geometry('500x500')
#
# def hello():
#     print('BUTTON1')
#
# def world():
#     print('BUTTON2')
#
# frame = Frame(root, borderwidth=6,background='gray')
# frame.pack(side=LEFT,anchor ='nw')
#
# b1 = Button(frame, fg='red',text='BTN1',command=hello)
# b1.pack(side = LEFT,padx=20)
#
# b2 = Button(frame,foreground='red', text='BTN2',command=world)
# b2.pack(side=LEFT,padx=10)
#
# root.mainloop()


############## CERATING TEXTBOX TAKING ENTRY FROM USER  AND SETTING GRID #########

# root = Tk()
# root.geometry('500x500')
#
# def getval():
#     print(eval(uservalue.get()))
#     print(passvalue.get())
#
#
# user = Label(root, text='username')
# passward = Label(root, text='passward')
# user.grid()
# passward.grid(row = 1)
#
#
# uservalue = StringVar()
# passvalue = StringVar()
#
# userentry = Entry(root, textvariable=uservalue)
# passentry = Entry(root, textvariable=passvalue)
#
# userentry.grid(row =0, column =1)
# passentry.grid(row =1, column =1)
#
# Button(text='SUBMIT', command=getval).grid()
#
# root.mainloop()


############ PRACTICE AND CHECKBOX CREATION #############

root = Tk()
root.geometry('500x500')
root.title('FORM FILL')
heading = Label(root, text='WELCOME', bg='red',font=("Arial", 16, "bold"))
heading.grid(row=0, column=3,pady=5)



def submited():
    # print(namevalue.get())
    # print(lastnamevalue.get())
    # print(gendervalue.get())
    # print(dobvalue.get())
    # print(phonevalue.get())
    # print('All values submited')

    info = {'name':[],'lastname':[]}
    info['name'].append(namevalue.get())
    info['lastname'].append(lastnamevalue.get())

    print(info)


name = Label(root, text='Name :')
lastname = Label(root, text='Last Name :')
gender = Label(root, text='Gender :')
dob = Label(root, text='DOB :')
phone = Label(root, text='Phone :')

name.grid(row=1, column=2)
lastname.grid(row=2, column=2)
gender.grid(row=3, column=2)
dob.grid(row=4, column=2)
phone.grid(row=5, column=2)

namevalue = StringVar()
lastnamevalue = StringVar()
gendervalue = StringVar()
dobvalue = StringVar()
phonevalue = StringVar()
checkbox = IntVar()

nameentry = Entry(root, textvariable=namevalue).grid(row=1, column=3)
lastnameentry = Entry(root, textvariable=lastnamevalue).grid(row=2, column=3)
genderentry = Entry(root, textvariable=gendervalue).grid(row=3, column=3)
dobentry = Entry(root, textvariable=dobvalue).grid(row=4, column=3)
phoneentry = Entry(root, textvariable=phonevalue).grid(row=5, column=3)


check = Checkbutton(text="click the checkbox", variable=checkbox).grid(row=6, column=3)

Button(text="Submit",pady=3, command=submited).grid(row=7, column=3)
root.mainloop()