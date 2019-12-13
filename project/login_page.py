from tkinter import *
import tkinter.messagebox
from tkinter import  ttk
import  random
import  time
import datetime
import back_end

username_ = ""
password_ = ""
details = []

def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()

class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Banking Login System")
        self.master.geometry('1350x750+0+0')
        self.master.resizable(height=False,width=False)
        #self.master.config(bg='light green')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text = "Banking Managment System",font = ('arial',38,'bold'))
        self.LabelTitle.grid(row=0,column=0,columnspan=3,pady=77)
        #=======================================================================================================
        self.Loginframe1 = Frame(self.master, bd=1,relief='ridge')
        self.Loginframe1.pack(fill=Y)

        self.Loginframe2 = Frame(self.master)
        self.Loginframe2.pack()
        helplabel=Label(self.master,text='Help ?',font='helvetica 25 bold', bg='lightgreen',fg='white')
        helplabel.place(x=20,y=690)

        self.Loginframe3 = Frame(self.master)
        self.Loginframe3.pack()

        #================================================================================================================
        self.lblUsername = Label(self.Loginframe1,width=10, text="Username:", font=('arial', 16, 'bold'))
        self.lblUsername.grid(row=4, column=0,pady=10)

        self.txtUsername = Entry(self.Loginframe1,width=20, font=('arial', 18),textvariable=self.Username,relief='flat')
        self.txtUsername.grid(row=4, column=1,columnspan=2,pady=10,padx=2)
        self.txtUsername.focus()

        self.lblPassword = Label(self.Loginframe1,width=10, text="Password:", font=('arial', 16, 'bold'))
        self.lblPassword.grid(row=5, column=0,pady=10)
        self.txtPassword = Entry(self.Loginframe1,width=20, font=('arial', 18),textvariable=self.Password,show='x',relief='flat')
        self.txtPassword.grid(row=5, column=1,columnspan=2,pady=10,padx=2)
        #================================================================================================================
        self.btnLogin = Button(self.Loginframe1,text='Login',width=10,font = ('arial',14,'bold'),command=self.Login_System,relief='groove',fg='green')
        self.btnLogin.grid(row=6,column=2)

        self.btnReset = Button(self.Loginframe1, text='Reset',width=10,font = ('helvetica',14,'bold'), command=self.Reset,relief='groove',fg='purple')
        self.btnReset.grid(row=6, column=1)

        self.btnExit = Button(self.Loginframe1, text='Exit',width=10,font = ('helevtica',14,'bold'), command=self.iExit,relief='groove',fg='red')
        self.btnExit.grid(row=6, column=0)
       #====================================================================================================================
        self.btnuser = Button(self.Loginframe1,text='Emplyoee Login System',width=21,state=DISABLED,font = ('arial',12),command=self.user_widow,relief='ridge')
        self.btnuser.grid(row=7,column=0,columnspan=2,sticky=W)

        self.btnadmin = Button(self.Loginframe1,text='Admin Login System',width=21,state=DISABLED,font = ('helvetica',12),command=self.banking_widow,relief='ridge')
        self.btnadmin.grid(row=7, column=1,pady=8,columnspan=2,sticky=E)
        
      # ====================================================================================================================
    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if(user == str(1234) and (pas == str(1234))):
            self.btnuser.config(state=DISABLED)
            self.btnadmin.config(state=NORMAL)
        else:
            details = back_end.searchUserPass(self.txtPassword.get(),self.txtUsername.get())
            if details:
                self.btnadmin.config(state=DISABLED)
                self.btnuser.config(state=NORMAL)
                global username_
                global password_
                username_=self.txtPassword.get()
                password_=self.txtUsername.get()
            else:
                tkinter.messagebox.askokcancel("Try again", "please enter correct details")
                self.btnuser.config(state=DISABLED)
                self.btnadmin.config(state=DISABLED)
                self.Username.set("")
                self.Password.set("")
                self.txtUsername.focus()




    def Reset(self):
        self.btnuser.config(state=DISABLED)
        self.btnadmin.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit =messagebox.askyesno("Banking Login System","confirm you want to exit")
        if self.iExit>0:
            self.master.destroy()
        return

    def user_widow(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def banking_widow(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)
class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Banking Mangament System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.EmpId = StringVar()
        self.Firstname = StringVar()
        self.surename = StringVar()
        self.Gender = StringVar()
        self.Age = StringVar()
        self.Mobile = StringVar()
        self.village = StringVar()
        self.password = StringVar()
        self.working_year = StringVar()
        self.base_salary = StringVar()
        self.username = StringVar()
        self.account_number = StringVar()
        self.gratuity = StringVar()
        self.DOB = StringVar()
        self.computaion = StringVar()
        self.pension = StringVar()
        self.ed = ""

        # =====================================================Frames==========================================================
        self.TitleFrame = Frame(self.frame, bd=10, width=1350, pady=8, bg="Ghost white", relief=RIDGE)
        self.TitleFrame.grid(row=0, column=0)

        self.lblTit = Label(self.TitleFrame, font=("arial", 40, 'bold'), text="  Bank Emplyoee Database Details   ",
                            bg="Ghost white")
        self.lblTit.grid()

        self.dataframe = Frame(self.frame, width=1350, height=520, padx=10, pady=10, bd=10, relief=RIDGE)
        self.dataframe.grid(row=1, column=0)

        self.ButtonFrame = Frame(self.frame, width=1350, height=70, padx=10, pady=15, bd=10, relief=RIDGE)
        self.ButtonFrame.grid(row=2, column=0)

        self.dataframeleft = Frame(self.dataframe, width=660, height=520, padx=10, pady=15, bd=10, bg='Ghost white',
                                   relief=RIDGE)
        self.dataframeleft.grid(row=0, column=0)

        self.dataframemid = Frame(self.dataframe, width=660, height=520, padx=10, pady=15, bd=10, bg='Ghost white',
                                  relief=RIDGE)
        self.dataframemid.grid(row=0, column=1)

        # ========================================Buttons====================================================================


        self.btnExit = Button(self.ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=20, bd=4,
                              command=self.iExit)
        self.btnExit.grid(row=0, column=1)



        # =============================================Labels & entry box==========================================================
        self.lblEmpID = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Emplyoee_ID:", padx=5, pady=6,
                              bg="Ghost white")
        self.lblEmpID.grid(row=0, column=0, sticky=W)
        self.txtEmpID = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.EmpId, width=25, bd=9,
                              relief=RIDGE)
        self.txtEmpID.grid(row=0, column=1)

        self.lblfna = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Firstname:", padx=10, pady=6,
                            bg="Ghost white")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.Firstname, width=25, bd=9,
                            relief=RIDGE)
        self.txtfna.grid(row=1, column=1)
        self.lblSna = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Surename:", padx=10, pady=6,
                            bg="Ghost white")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.surename, width=25, bd=9,relief=RIDGE)
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="DateofBirth:", padx=10, pady=6,
                            bg="Ghost white")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.DOB, width=25, bd=9,
                            relief=RIDGE)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Age:", padx=10, pady=6,
                            bg="Ghost white")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.Age, width=25, bd=9,
                            relief=RIDGE)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Gender:", padx=10, pady=6,
                               bg="Ghost white")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.Gender, width=25, bd=9,
                               relief=RIDGE)
        self.txtGender.grid(row=5, column=1)

        self.lblvill = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Village:", padx=10, pady=6,
                             bg="Ghost white")
        self.lblvill.grid(row=6, column=0, sticky=W)
        self.txtvill = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.village, width=25, bd=9,
                             relief=RIDGE)
        self.txtvill.grid(row=6, column=1)

        self.lblMobile = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Mobile:", padx=10, pady=6,bg="Ghost white")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.Mobile, width=25, bd=9,
                               relief=RIDGE)
        self.txtMobile.grid(row=7, column=1)

        self.lblusername = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Username:", padx=10, pady=6,
                                 bg="Ghost white")
        self.lblusername.grid(row=0, column=0, sticky=W)
        self.txtusername = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.username, width=25,
                                 bd=9, relief=RIDGE)
        self.txtusername.grid(row=0, column=1)

        self.lblpassword = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Password:", padx=10, pady=6,
                                 bg="Ghost white")
        self.lblpassword.grid(row=1, column=0, sticky=W)
        self.txtpassword = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.password, width=25,
                                 bd=9, relief=RIDGE)
        self.txtpassword.grid(row=1, column=1)

        self.lblsalary = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Last_salary:", padx=10, pady=6,
                               bg="Ghost white")
        self.lblsalary.grid(row=2, column=0, sticky=W)
        self.txtsalary = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.base_salary, width=25,
                               bd=9, relief=RIDGE)
        self.txtsalary.grid(row=2, column=1)

        self.lblaccount = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Account_number:", padx=10, pady=6,
                                bg="Ghost white")
        self.lblaccount.grid(row=3, column=0, sticky=W)
        self.txtaccount = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.account_number,
                                width=25, bd=9, relief=RIDGE)
        self.txtaccount.grid(row=3, column=1)

        self.lblyear = Label(self.dataframemid, font=("arial", 20, 'bold'), text="yearofservice:", padx=10, pady=6,
                             bg="Ghost white")
        self.lblyear.grid(row=4, column=0, sticky=W)
        self.txtyear = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.working_year, width=25,
                             bd=9, relief=RIDGE)
        self.txtyear.grid(row=4, column=1)

        self.lblcomputation = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Computation:", padx=10, pady=6,
                                    bg="Ghost white")
        self.lblcomputation.grid(row=5, column=0, sticky=W)
        self.txtcomputation = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.computaion,
                                    width=25, bd=9, relief=RIDGE)
        self.txtcomputation.grid(row=5, column=1)

        self.lblpension = Label(self.dataframemid, font=("arial", 20, 'bold'), text="pension:", padx=10, pady=6,
                                bg="Ghost white")
        self.lblpension.grid(row=6, column=0, sticky=W)
        self.txtpension = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.pension, width=25,
                                bd=9, relief=RIDGE)
        self.txtpension.grid(row=6, column=1)

        self.lblgrat = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Gratuity:", padx=10, pady=6,
                             bg="Ghost white")
        self.lblgrat.grid(row=7, column=0, sticky=W)
        self.txtgrat = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.gratuity, width=25, bd=9,
                             relief=RIDGE)
        self.txtgrat.grid(row=7, column=1)

        details = back_end.searchUserPass(username_, password_)
        self.EmpId.set(details[1])
        self.Firstname.set(details[2])
        self.surename.set(details[3])
        self.Gender.set(details[4])
        self.Age.set(details[5])
        self.Mobile.set(details[6])
        self.village.set(details[7])
        self.password.set(details[8])
        self.working_year.set(details[9])
        self.base_salary.set(details[10])
        self.username.set(details[11])
        self.account_number.set(details[12])
        self.gratuity.set(details[13])
        self.DOB.set(details[14])
        self.computaion.set(details[15])
        self.pension.set(details[16])

        self.txtEmpID.config(state='disabled')
        self.txtfna.config(state='disabled')
        self.txtSna.config(state='disabled')
        self.txtGender.config(state='disabled')
        self.txtAge.config(state='disabled')
        self.txtMobile.config(state='disabled')
        self.txtvill.config(state='disabled')
        self.txtpassword.config(state='disabled')
        self.txtyear.config(state='disabled')
        self.txtsalary.config(state='disabled')
        self.txtusername.config(state='disabled')
        self.txtaccount.config(state='disabled')
        self.txtgrat.config(state='disabled')
        self.txtDoB.config(state='disabled')
        self.txtcomputation.config(state='disabled')
        self.txtpension.config(state='disabled')



        # =================================================functions============================================================

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Emplyoee Database Details system", "confirm if you want to exit")
        if iExit > 0:
            self.master.destroy()
            return
class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("User Mangement System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.EmpId = StringVar()
        self.Firstname = StringVar()
        self.surename = StringVar()
        self.Gender = StringVar()
        self.Age = StringVar()
        self.Mobile = StringVar()
        self.village = StringVar()
        self.password = StringVar()
        self.working_year = StringVar()
        self.base_salary = StringVar()
        self.username = StringVar()
        self.account_number = StringVar()
        self.gratuity = StringVar()
        self.DOB = StringVar()
        self.computaion = StringVar()
        self.pension = StringVar()
        self.ed = ""

        # =====================================================Frames==========================================================
        self.TitleFrame = Frame(self.frame, bd=10, width=1350, pady=8, bg="Ghost white", relief=RIDGE)
        self.TitleFrame.grid(row=0, column=0)

        self.lblTit = Label(self.TitleFrame, font=("arial", 40, 'bold'), text="  Banking Database Managment system   ",bg="Ghost white")
        self.lblTit.grid()

        self.dataframe = Frame(self.frame, width=1350, height=520, padx=10, pady=10, bd=10, relief=RIDGE)
        self.dataframe.grid(row=1, column=0)

        self.ButtonFrame = Frame(self.frame, width=1350, height=70, padx=10, pady=15, bd=10, relief=RIDGE)
        self.ButtonFrame.grid(row=2, column=0)

        self.dataframeleft = Frame(self.dataframe, width=490, height=520, padx=10, pady=15, bd=10, bg='Ghost white',relief=RIDGE)
        self.dataframeleft.grid(row=0, column=0)

        self.dataframemid = Frame(self.dataframe, width=490, height=520, padx=10, pady=15, bd=10, bg='Ghost white',relief=RIDGE)
        self.dataframemid.grid(row=0, column=1)

        self.dataframeright = Frame(self.dataframe, width=280, height=520, padx=10, pady=15, bd=10, relief=RIDGE)
        self.dataframeright.grid(row=0, column=2)

        # ========================================Buttons====================================================================
        self.btnAddData = Button(self.ButtonFrame, text="Add EMP", font=('arial', 20, 'bold'), height=1, width=9, bd=4,command=self.addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplay = Button(self.ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=9, bd=4,command=self.DisplayData)
        self.btnDisplay.grid(row=0, column=1)

        self.btnclear = Button(self.ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=9, bd=4,command=self.clearData)
        self.btnclear.grid(row=0, column=2)

        self.btnDelete = Button(self.ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=9, bd=4, command=self.DeleteData)
        self.btnDelete.grid(row=0, column=3)

        self.btnsearch = Button(self.ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=9, bd=4,command=self.searchDatabase)
        self.btnsearch.grid(row=0, column=4)

        self.btnUpdate = Button(self.ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=9, bd=4,command=self.update)
        self.btnUpdate.grid(row=0, column=5)

        self.btnExit = Button(self.ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=6, bd=4,command=self.iExit)
        self.btnExit.grid(row=0, column=7)

        self.btncalculate = Button(self.ButtonFrame, text="Calculate", font=('arial', 20, 'bold'), height=1, width=9,bd=4, command=self.calc)
        self.btncalculate.grid(row=0, column=6)

        # =============================================Labels & entry box==========================================================
        self.lblEmpID = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="EmplyoeeID:", padx=2, pady=6,bg="Ghost white")
        self.lblEmpID.grid(row=0, column=0, sticky=W)
        self.txtEmpID = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.EmpId, width=17, bd=9,relief=RIDGE)
        self.txtEmpID.grid(row=0, column=1)


        self.lblfna = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Firstname:", padx=2, pady=6,bg="Ghost white")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.Firstname, width=17, bd=9,relief=RIDGE)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Surename:", padx=2, pady=6,bg="Ghost white")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.surename, width=17, bd=9,relief=RIDGE)
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Date/Birth:", padx=2, pady=6,bg="Ghost white")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.DOB, width=17, bd=9,relief=RIDGE)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Age:", padx=2, pady=6,bg="Ghost white")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.Age, width=17, bd=9,relief=RIDGE)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Gender:", padx=2, pady=6,bg="Ghost white")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.Gender, width=17, bd=9,relief=RIDGE)
        self.txtGender.grid(row=5, column=1)

        self.lblvill = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Village:", padx=2, pady=6,bg="Ghost white")
        self.lblvill.grid(row=6, column=0, sticky=W)
        self.txtvill = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.village, width=17, bd=9,relief=RIDGE)
        self.txtvill.grid(row=6, column=1)

        self.lblMobile = Label(self.dataframeleft, font=("arial", 20, 'bold'), text="Mobile:", padx=2, pady=6,bg="Ghost white")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(self.dataframeleft, font=("arial", 20, 'bold'), textvariable=self.Mobile, width=17, bd=9,relief=RIDGE)
        self.txtMobile.grid(row=7, column=1)

        self.lblusername = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Username:", padx=2, pady=6, bg="Ghost white")
        self.lblusername.grid(row=0, column=0, sticky=W)
        self.txtusername = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.username, width=17, bd=9,relief=RIDGE)
        self.txtusername.grid(row=0, column=1)

        self.lblpassword = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Password:", padx=2, pady=6,bg="Ghost white")
        self.lblpassword.grid(row=1, column=0, sticky=W)
        self.txtpassword = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.password, width=17, bd=9,relief=RIDGE)
        self.txtpassword.grid(row=1, column=1)

        self.lblsalary = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Last_salary:", padx=2, pady=6,bg="Ghost white")
        self.lblsalary.grid(row=2, column=0, sticky=W)
        self.txtsalary = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.base_salary, width=17,bd=9, relief=RIDGE)
        self.txtsalary.grid(row=2, column=1)

        self.lblaccount = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Acc_num:", padx=2, pady=6,bg="Ghost white")
        self.lblaccount.grid(row=3, column=0, sticky=W)
        self.txtaccount = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.account_number,width=17, bd=9, relief=RIDGE)
        self.txtaccount.grid(row=3, column=1)

        self.lblyear = Label(self.dataframemid, font=("arial", 20, 'bold'), text="yearofservice:", padx=2, pady=6, bg="Ghost white")
        self.lblyear.grid(row=4, column=0, sticky=W)
        self.txtyear = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.working_year, width=17,bd=9, relief=RIDGE)
        self.txtyear.grid(row=4, column=1)

        self.lblcomputation = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Computation:", padx=2, pady=6,bg="Ghost white")
        self.lblcomputation.grid(row=5, column=0, sticky=W)
        self.txtcomputation = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.computaion, width=17, bd=9, relief=RIDGE)
        self.txtcomputation.grid(row=5, column=1)

        self.lblpension = Label(self.dataframemid, font=("arial", 20, 'bold'), text="pension:", padx=2, pady=6,bg="Ghost white")
        self.lblpension.grid(row=6, column=0, sticky=W)
        self.txtpension = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.pension, width=17,bd=9, relief=RIDGE)
        self.txtpension.grid(row=6, column=1)

        self.lblgrat = Label(self.dataframemid, font=("arial", 20, 'bold'), text="Gratuity:", padx=2, pady=6,bg="Ghost white")
        self.lblgrat.grid(row=7, column=0, sticky=W)
        self.txtgrat = Entry(self.dataframemid, font=("arial", 20, 'bold'), textvariable=self.gratuity, width=17, bd=9,relief=RIDGE)
        self.txtgrat.grid(row=7, column=1)

        # ==================================== List Box & scroll bar================================= ================================

        self.scrollbar = Scrollbar(self.dataframeright)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.emplyoeeList = Listbox(self.dataframeright, width=25, height=21, font=('arial', 12, 'bold'),yscrollcommand=self.scrollbar.set)
        self.emplyoeeList.bind('<<ListboxSelect>>', self.empRec)
        self.emplyoeeList.grid(row=0, column=0, padx=5)
        self.scrollbar.config(command=self.emplyoeeList.yview)
        # ============================================================================================================================

        # =================================================functions============================================================

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Admin Database managment system", "confirm if you want to exit")
        if iExit > 0:
            self.master.destroy()
            return

    def clearData(self):
        self.EmpId.set("")
        self.Firstname.set("")
        self.surename.set("")
        self.Gender.set("")
        self.Age.set("")
        self.Mobile.set("")
        self.village.set("")
        self.password.set("")
        self.working_year.set("")
        self.base_salary.set("")
        self.username.set("")
        self.account_number.set("")
        self.gratuity.set("")
        self.DOB.set("")
        self.computaion.set("")
        self.pension.set("")
        self.txtEmpID.focus()

    def calc(self):
        self.x = (15 * (int(self.working_year.get()) * int(self.base_salary.get())) // 26)
        self.gratuity.set(str('Rs.')+str(self.x))

    def addData(self):
        if (len(self.EmpId.get()) != 0):
            back_end.AddEmpRec(self.EmpId.get(), self.Firstname.get(), self.surename.get(), self.Gender.get(),self.Age.get(), self.Mobile.get(), self.village.get(), self.password.get(),self.working_year.get(), self.base_salary.get(), self.username.get(),self.account_number.get(), self.gratuity.get(), self.DOB.get(), self.computaion.get(),self.pension.get())
            self.emplyoeeList.delete(0, END)
            self.emplyoeeList.insert(END, (self.EmpId.get(), self.Firstname.get(), self.surename.get(), self.Gender.get(), self.Age.get(),self.Mobile.get(), self.village.get(), self.password.get(), self.working_year.get(), self.base_salary.get(),self.username.get(), self.account_number.get(), self.gratuity.get(), self.DOB.get(), self.computaion.get(),self.pension.get()))

    def DisplayData(self):
        self.emplyoeeList.delete(0, END)
        for row in back_end.viewData():
            self.emplyoeeList.insert(END, row, str(""))

    def empRec(self, event):
        self.searchStd = self.emplyoeeList.curselection()[0]
        self.ed = self.emplyoeeList.get(self.searchStd)

        self.txtEmpID.delete(0, END)
        self.txtEmpID.insert(END, self.ed[1])

        self.txtfna.delete(0, END)
        self.txtfna.insert(END, self.ed[2])

        self.txtSna.delete(0, END)
        self.txtSna.insert(END, self.ed[3])

        self.txtGender.delete(0, END)
        self.txtGender.insert(END, self.ed[4])

        self.txtAge.delete(0, END)
        self.txtAge.insert(END, self.ed[5])

        self.txtMobile.delete(0, END)
        self.txtMobile.insert(END, self.ed[6])

        self.txtvill.delete(0, END)
        self.txtvill.insert(END, self.ed[7])

        self.txtpassword.delete(0, END)
        self.txtpassword.insert(END, self.ed[8])

        self.txtyear.delete(0, END)
        self.txtyear.insert(END, self.ed[9])

        self.txtsalary.delete(0, END)
        self.txtsalary.insert(END, self.ed[10])

        self.txtusername.delete(0, END)
        self.txtusername.insert(END, self.ed[11])

        self.txtaccount.delete(0, END)
        self.txtaccount.insert(END, self.ed[12])

        self.txtgrat.delete(0, END)
        self.txtgrat.insert(END, self.ed[13])

        self.txtDoB.delete(0, END)
        self.txtDoB.insert(END, self.ed[14])

        self.txtcomputation.delete(0, END)
        self.txtcomputation.insert(END, self.ed[15])

        self.txtpension.delete(0, END)
        self.txtpension.insert(END, self.ed[16])

    def DeleteData(self):
        if (len(self.EmpId.get()) != 0):
            back_end.deletRec(self.ed[0])
            self.clearData()
            self.DisplayData()

    def searchDatabase(self):
        self.emplyoeeList.delete(0, END)
        for row in back_end.searchData(self.EmpId.get(), self.Firstname.get(), self.surename.get(), self.Gender.get(),self.Age.get(), self.Mobile.get(), self.village.get(), self.password.get(), self.working_year.get(), self.base_salary.get(), self.username.get(),self.account_number.get(), self.gratuity.get(), self.DOB.get(), self.computaion.get(), self.pension.get()):
            self.emplyoeeList.insert(END, row, str(""))

    def update(self):
        if (len(self.EmpId.get()) != 0):
            back_end.deletRec(self.ed[0])

        if (len(self.EmpId.get()) != 0):
            back_end.AddEmpRec(self.EmpId.get(), self.Firstname.get(), self.surename.get(), self.Gender.get(),self.Age.get(), self.Mobile.get(), self.village.get(), self.password.get(), self.working_year.get(), self.base_salary.get(), self.username.get(),self.account_number.get(), self.gratuity.get(), self.DOB.get(), self.computaion.get(),self.pension.get())
            self.emplyoeeList.delete(0, END)
            self.emplyoeeList.insert(END, (self.EmpId.get(), self.Firstname.get(), self.surename.get(), self.Gender.get(), self.Age.get(),self.Mobile.get(), self.village.get(), self.password.get(), self.working_year.get(), self.base_salary.get(),self.username.get(), self.account_number.get(), self.gratuity.get(), self.DOB.get(), self.computaion.get(),self.pension.get()))

if __name__ == '__main__':
    main()

