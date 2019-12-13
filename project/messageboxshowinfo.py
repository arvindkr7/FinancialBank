from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('500x300+5+5')
root.title('Messgagebox')

def info():
    top=Toplevel(root)
    top.geometry('300x200+400+200')
    name='Vivek Yadav'
    l2=Label(top,text=name,font='helvetica 15 bold',br=20,ng='light red')
    l2.place(x=30,y=60)

b1=Button(root,text="submit",command=info)
b1.pack()
root.mainloop()