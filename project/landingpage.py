from tkinter import *
from tkinter import messagebox
from tkinter import  ttk
import  random
import  time
import datetime
import back_end
import numpy as np
#from email.message import EmailMessage
#import smtplib
username_ = ""
password_ = ""
details = []   

def main():
    root = Tk()
    root.iconbitmap('bank.ico')
    app = Window1(root)
    #aps=Calculator(root)
#app.TIME()
#app.move()
    root.mainloop()


class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Banking Login System")
        self.master.geometry('1350x750+0+0')
        #self.master.resizable(height=False,width=False)
        frametop=Frame(self.master)
        Window1.flag='send'
        self.Username = StringVar()
        self.Password = StringVar()

        frametop.config(bg='#3b536f')
        label1=Label(frametop,text='Welcome!',font='sans-serif 10',fg='white',padx=2,bg='#3b536f')
        label1.pack(side=LEFT)
       
        label2=Label(frametop,text='UNIBANK',font='sans-serif 14 bold',fg='white',padx=15,bg='#3b536f')
        label2.pack(side=LEFT)
        
        label1=Button(frametop,text='Log In',font='sans-serif 15 bold',bg='white',fg='#3b536f',pady=7,cursor='hand2',relief='groove')
        label1.pack(side=LEFT,anchor=E,padx=220)
        

        self.timelabel=Label(frametop,font='sans-serif 13 bold',cursor='hand2',bg='#3b536f',fg='white')
        self.timelabel.pack(side=RIGHT,padx=10)
        self.TIME()
        clklabel=Label(frametop,text='Current Time : ',font='sans-serif 13 bold',cursor='hand2',bg='#3b536f',fg='lightgreen')
        clklabel.pack(side=RIGHT)
       
        
    
        
        frametop.pack(fill=X)

        frameside=Frame(self.master,padx=10,pady=10)
        frameside.pack(side=TOP,fill=X)
        

        frameside1=Frame(frameside,bg='black')
        frameside1.pack(side=LEFT,padx=10,pady=10)

        frame11=Frame(frameside1,bg='black')
        frame11.pack(side=TOP)
        label11=Label(frame11,text='Internet Banking',bg='blue',fg='white',font='sans-serif 11')
        label11.pack(side=TOP,padx=2,pady=2,fill=X,expand=YES)
        label12=Label(frame11,text='Personal',bg='black',fg='white',font='sans-serif 11')
        label12.pack(side=TOP,padx=2,pady=2,anchor=W)9+
        label13=Label(frame11,text='Corporate',bg='black',fg='white',font='sans-serif 11')
        label13.pack(side=TOP,padx=2,pady=2,anchor=W)
        label14=Label(frame11,text='Global',bg='black',fg='white',font='sans-serif 11')
        label14.pack(side=TOP,padx=2,pady=2,anchor=W)

        frame12=Frame(frameside1,bg='white',bd=2)
        frame12.pack(side=TOP,padx=2,pady=2,fill=X)
        label1=Label(frame12,text='Online Services',bg='black',fg='white',font='sans-serif 11')
        label1.pack(side=LEFT)
        label1=Label(frame12,text='onlineservicesn',bg='black',fg='black')
        label1.pack(side=LEFT)

        frame12=Frame(frameside1,bg='white',bd=2)
        frame12.pack(side=TOP,padx=2,pady=2,fill=X)
        label1=Label(frame12,text='Interested in Our Products',bg='black',fg='white',font='sans-serif 11')
        label1.pack(side=LEFT)
        label1=Label(frame12,text='on',bg='black',fg='black')
        label1.pack(side=LEFT)

        frame12=Frame(frameside1,bg='white',bd=2)
        frame12.pack(side=TOP,padx=2,pady=2,fill=X)
        label1=Label(frame12,text='Communication to BSE/NSE',bg='black',fg='white',font='sans-serif 11')
        label1.pack(side=LEFT)

        frame12=Frame(frameside1,bg='white',bd=2)
        frame12.pack(side=TOP,padx=2,pady=2,fill=X)
        label1=Label(frame12,text='Customer Care',bg='black',fg='white',font='sans-serif 11')
        label1.pack(side=LEFT)
        label1=Label(frame12,text='onlineservicesn',bg='black',fg='black')
        label1.pack(side=LEFT)




 ##### Login System    ############################################

        frameside2=Frame(frameside,bg='white')
        frameside2.pack(side=RIGHT,expand=YES,padx=5)

        labelframe=LabelFrame(frameside2,text='Login',font='sans-serif 12 bold')
        labelframe.pack(expand=YES,fill=X,padx=5,pady=5)

        idframe=Frame(labelframe,relief='groove')
        idframe.pack(side=LEFT,padx=5,pady=5)

        idlabel=Label(idframe,text='UserId',font='sans-serif 15 bold')
        idlabel.pack(side=LEFT,padx=5,pady=5)

        self.txtUsername=Entry(idframe,font='sans-serif 15 bold',textvariable=self.Username)
        self.txtUsername.pack(side=LEFT,padx=5,pady=5)
        self.txtUsername.focus()

        pasframe=Frame(labelframe)
        pasframe.pack(side=LEFT,padx=5,pady=5)
        paslabel=Label(pasframe,text='Password',font='sans-serif 15 bold')
        paslabel.pack(side=LEFT,padx=5,pady=5)
        self.txtPassword=Entry(pasframe,show='*',font='sans-serif 15 bold',textvariable=self.Password)
        self.txtPassword.pack(side=LEFT,padx=5,pady=5)

        framebtn1=Frame(frameside2)
        framebtn1.pack(padx=5,pady=5)
        ###########BUTTONS ###############
        self.btnExit=Button(framebtn1,text='Exit',font='sans-serif 16 bold',fg='white',bg='red',width=16,cursor='hand2',command=self.iExit)
        self.btnExit.pack(side=LEFT,padx=5,pady=5)
        self.btnReset=Button(framebtn1,text='Clear',font='sans-serif 16 bold',fg='white',bg='grey',width=16,cursor='hand2',command=self.Reset)
        self.btnReset.pack(side=LEFT,padx=5,pady=5)
        self.btnLogin=Button(framebtn1,text='Submit',font='sans-serif 16 bold',fg='white',bg='light green',width=16,cursor='hand2',command=self.Login_System)
        self.btnLogin.pack(side=LEFT,padx=5,pady=5)

        framebtn2=Frame(frameside2)
        framebtn2.pack(padx=5,pady=5)
        ############### admin user button ###################
        self.btnuser=Button(framebtn2,text='Employee Login System',font='sans-serif 15 bold',width=27,cursor='hand2',state=DISABLED,command=self.user_widow)
        self.btnuser.pack(side=LEFT,padx=5,pady=5)
        self.btnadmin=Button(framebtn2,text='Admin Login System',font='sans-serif 15 bold',width=27,cursor='hand2',state=DISABLED,command=self.banking_widow)
        self.btnadmin.pack(side=LEFT,padx=5,pady=5)


        labelmid=Label(self.master,text='UNIBANK MANAGEMENT SYSTEM',font='helvetica 28 bold',relief='raised',fg='#48d1cc')
        labelmid.pack(fill=BOTH,padx=10,pady=10)

        frametiles=Frame(self.master,bg='purple')

        lbl2=Frame(frametiles,width=60,bg='white',padx=2,pady=2)
        lbl2.pack(side=LEFT,padx=16,pady=16,expand=NO,fill=BOTH)
        lbl=Label(lbl2,text='BEWARE OF FRAUDANT',font='arial 19')
        lbl.pack(padx=4,pady=4,fill=X)
        lbl=Label(lbl2,text='Caution: ',font='arial 14', fg='red',bg='white')
        lbl.pack(padx=4,pady=4,anchor=W)
        lbl=Label(lbl2,text='Beware of Fraudster and save your hard money earned')
        lbl.pack(padx=4,pady=4,fill=X)
        lbl=Label(lbl2,text='Fake addresses and phone numbers of Bank"s branches .')
        lbl.pack(padx=4,expand=NO)
        lbl=Label(lbl2,text='are created by miscreants on google search.')
        lbl.pack(padx=4,pady=4,expand=NO,fill=X)
        lbl=Label(lbl2,text='Please do not search for any branch address .')
        lbl.pack(padx=4,pady=4,expand=NO,fill=X)
        lbl=Label(lbl2,text=' on google search or map.')
        lbl.pack(padx=4,pady=4,expand=NO,fill=X)
        lbl=Label(lbl2,text=' Use Bank"s own website only for any contact details')
        lbl.pack(padx=4,pady=4,expand=NO,fill=X)


        lbl3=Frame(frametiles,width=60,height=17,bg='white',padx=2,pady=2)
        lbl3.pack(side=LEFT,pady=16,expand=NO)
        lbl=Label(lbl3,text='Contact Us',font='arial 19')
        lbl.pack(expand=NO,pady=5,padx=4,fill=X)
        lbl=Label(lbl3,height=3,text='Shop No.205, 2nd Level, Unimall,LPU',font='arial 13')
        lbl.pack(padx=4,pady=2,fill=X)
        lbl=Label(lbl3,height=3,text='Call 1800 200 199 / 1800 183 299 ',font='arial 13')
        lbl.pack(padx=4,pady=4,fill=X)
        lbl=Label(lbl3,text='FIND US ON ',font='arial 11')
        lbl.pack(padx=4,pady=4,side=LEFT,fill=BOTH)
        lbl=Label(lbl3,text='FACEBOOK',font='arial 11',fg='SlateGray2')
        lbl.pack(pady=4,padx=4,side=LEFT,fill=BOTH)
        lbl=Label(lbl3,height=4,text='TWITTER ',font='arial 11',fg='SlateGray1')
        lbl.pack(padx=4,pady=4,side=LEFT,fill=X)

        lbl4=Frame(frametiles,width=60,height=17,bg='white',padx=2,pady=2)
        lbl4.pack(side=LEFT,padx=16,pady=16,expand=NO,fill=X)
        lbl=Label(lbl4,text='Calculate',font='arial 19')
        lbl.pack(padx=4,pady=4,fill=X)
        self.Calcbutton=Button(lbl4,width=14,height=5,text='Calculator', font='arial 25 bold',cursor='hand2',command=self.calculator_widow)
        self.Calcbutton.pack(pady=4,padx=4)
        #frametiles.pack(fill=X,side=BOTTOM,padx=5,pady=5)

        #SlateGray1,SlateGray2,SlateGray3,SlateGray4

        self.framebot=Frame(self.master)
        self.framebot.config(bg='#3b536f')
        self.message = Label(self.framebot,bg='orange', pady=5,padx=5,text = 'UNIBANK adds new features to international student travel card.  UNIBANK Bank crosses milestone of issuing 2 million FASTag, highest in India Standalone Financial Results : Quarter ended September 30, 2019 Performance Review: Quarter ended September 30, 2019')
        labelhelp=Label(self.master,text='Help?',font='sans-serif 20 bold',bg='lightgreen',fg='white',relief=RAISED,cursor='hand2')

        label1=Label(self.framebot,text='NEWS',font='sans-serif 10 ',padx=15,bg='orange',pady=5)
        label1.pack(side=LEFT)
        #label2=Label(framebot,text='UNIBANK adds new features to international student travel card',bg='orange')
        #label2.pack(side=LEFT)
        #label2=Label(framebot,text='UNIBANK Bank crosses milestone of issuing 2 million FASTag, highest in India Standalone Financial Results : Quarter ended September 30, 2019 Performance Review: Quarter ended September 30, 2019',bg='black',fg='orange')
        #label2.pack(side=LEFT)
        self.framebot.configure(bg='orange')
        self.framebot.pack(side=BOTTOM,fill=X)
        self.message.x_limit = 2000
        self.message.move = 1
        self.message.delay = 30
        self.message.pack(side=LEFT)
        self.message.after(5, self.move)

        labelhelp.pack(side=BOTTOM,anchor=W,padx=10,pady=2)
        frametiles.pack(side=BOTTOM,padx=15,pady=5)


# functions ################################
    def move(self):  
            
        if self.message.winfo_x() + self.message.move >= self.message.x_limit or self.message.winfo_x() + self.message.move < 0:
            self.message.move = -self.message.move
        self.message.place(x=self.message.winfo_x() + self.message.move)
        self.message.after(self.message.delay, self.move)                    
   
        #message.config (fg = 'white',bg = 'blue', font=('times','60'))
    

    def TIME(self):
        self.current_time=time.strftime('%H: %M : %S')
        self.timelabel.config(text=self.current_time)
        self.timelabel.after(200,self.TIME)

    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())
# OTP AUTHENTICATION SYSTEM ##########################
        if(user == str(1234) and (pas == str(1234))):
            self.top=Toplevel(self.master)
            self.top.geometry('400x160+400+300')
            self.top.title('Submit OTP')
            otplabel=Label(self.top,text='Enter OTP',font='helvetica 12 bold',relief='groove',bd=2)
            otplabel.pack(side=LEFT)
            self.otpentry=Entry(self.top,font='helvetica 12',width=12)
            self.otpentry.pack(side=LEFT)
            self.otpsendbutton=Button(self.top,text='Send OTP',font='helvetica 12 bold',bg='lightblue',fg='white',command=self.wind2)
            self.otpsendbutton.pack(side=LEFT)
            self.otpsubmitbutton=Button(self.top,text='Submit OTP',font='helvetica 12 bold',fg='green',command=self.wind3)
            self.otpsubmitbutton.pack(side=LEFT)
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
                messagebox.askokcancel("Try again", "please enter correct details")
                self.btnuser.config(state=DISABLED)
                self.btnadmin.config(state=DISABLED)
                self.Username.set("")
                self.Password.set("")
                self.txtUsername.focus()
            ############ sending otp #####################
    def wind2(self):
        if Window1.flag=='send':
            self.otp=np.random.randint(100000)
                    #print(self.otp)
            self.t1=time.asctime(time.localtime(time.time()))
                 #print(self.t1)
            Window1.flag='sent'
            try:
                email_addr='' #s ource account email id
                email_pass=''# source account password
                msg=EmailMessage()
                msg['Subject']='UniBank: Login OTP'
                msg['From']=email_addr
                msg['To']='as30982@outlook.in'
                msg.set_content(f"Dear User, {self.otp} is the OTP to login into your UNIBANK Admin Pannel.\nLogin attempted at {self.t1}.\nPlease, don't share it with anyone.")
            
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login(email_addr,email_pass)

                    smtp.send_message(msg)
            except:
                        
                messagebox.showerror('Network Error',"Couldn't send OTP. check Internet Connection")
                print('No intenet Found')
                print(self.otp)
                f=open('seck3y.txt','w')
                m1=f"{self.otp} at {self.t1}"
                f.write(m1)
                f.close()
                        #print(f.closed)
                print(self.t1)
                        #raise  #this describes the error occured why
                        
                        
        else:
            messagebox.showwarning('OTP ReAttempt',f"OTP has already been sent to your registered email id\nat : '{self.t1}'")
                
            ############ verifying otp ######################    
    def wind3(self):
        otp1=self.otpentry.get()
                #print("Generated OTP",self.otp)
                #print("Entered OTP",otp1)
        if Window1.flag=='sent':
                    
            if otp1==str(self.otp):
                messagebox.showinfo('Login','Logged in Successfully')
                self.top.destroy()
                        #self.master.destroy()
                self.t2=time.asctime(time.localtime(time.time()))
                self.btnuser.config(state=DISABLED)
                self.btnadmin.config(state=NORMAL)
                try:
                    email_addr='sourceemailid'
                    email_pass=''
                    msg=EmailMessage(sourceidpassword)
                    msg['Subject']='Security Alert: UniBank Login successful'
                    msg['From']=email_addr
                    msg['To']='destinatiom emailid'
                    msg.set_content(f"Dear User,you just logged in to your UNIBANK Admin Pannel.\n Login attempted at {self.t2}.\nYou're getting this email to make sure it was you.")
                

                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                        smtp.login(email_addr,email_pass)

                        smtp.send_message(msg)
                except:

                    messagebox.showerror('Network Error',"NO Internet Connection")
                    print('No intenet Found')
                            #raise  # this describes the error occured why

            else:
                    messagebox.showwarning('Wrong OTP','Authentication Failed. Enter correct OTP')
        else:
            messagebox.showwarning('Without Send OTP','OTP is not sent.First, Click "Send OTP" ')

            
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

    def calculator_widow(self):
        self.newWindow = Toplevel(self.master)
        self.app = Calculator(self.newWindow)  
    

# ############## class Calculator #################
class Calculator:
    def __init__(self,master):
        self.master=master
        self.master.title("Gratuity and annuity calcultor")
        self.master.geometry("800x350")

        Label(self.master,text="Current age: ").place(x=25,y=10)
        self.e1=Entry(self.master)
        self.e1.place(x=275,y=10)

        Label(self.master,text="Retirement age: ").place(x=525,y=10)
        self.e2=Entry(self.master)
        self.e2.place(x=615,y=10)

        Label(self.master,text="Contribution towards nps per month: ").place(x=25,y=50)
        self.e3=Entry(self.master)
        self.e3.place(x=275,y=50)

        Label(self.master,text="Expected rate of return on nps investment: ").place(x=25,y=90)
        self.e4=Entry(self.master)
        self.e4.place(x=275,y=90)

        Label(self.master,text="Annuity period: ").place(x=25,y=130)
        self.e5=Entry(self.master)
        self.e5.place(x=275,y=130)

        Label(self.master,text="% of pension wealth invested into annuity:").place(x=25,y=170)
        self.e6=Entry(self.master)
        self.e6.place(x=275,y=170)

        Label(self.master,text="Expected rate of return on annuity investment:").place(x=25,y=210)
        self.e7=Entry(self.master)
        self.e7.place(x=275,y=210)

        w=Canvas(self.master,height=5,width=800)
        w.place(x=0,y=260)
        w.create_line(40,2,760,2)

        Button(self.master,text="Submit",height=2,width=80,fg="green",command=self.chck).place(x=100,y=280)
    
    def chck(self):
        cage=self.e1.get()
        self.cage=int(cage)
        rage=self.e2.get()
        self.rage=int(rage)
        contri=self.e3.get()
        self.contri=int(contri)
        exprt=self.e4.get()
        self.exprt=int(exprt)/100
        anprd=self.e5.get()
        self.anprd=int(anprd)
        perann=self.e6.get()
        self.perann=int(perann)
        exprtann=self.e7.get()
        self.exprtann=int(exprtann)/100

        if self.cage<18:
            troot=Tk()
            Label(troot,text="Attention!!  Age can't be less than 18 years.",fg="red").place(x=20,y=15)
            Button(troot,text="OK, I understand.",command=troot.destroy).place(x=130,y=60)
            troot.geometry("350x100")
            troot.mainloop()
        elif self.rage>60:
            troot = Tk()
            Label(troot, text="Attention!!  Maximum age of retirement is 60.", fg="red").place(x=20, y=15)
            Button(troot, text="OK, I understand.", command=troot.destroy).place(x=130, y=60)
            troot.geometry("350x100")
            troot.mainloop()
        elif self.perann<60:
            troot = Tk()
            Label(troot, text="Attention!!  Annuity % can't be less than 60", fg="red").place(x=20, y=15)
            Button(troot, text="OK, I understand.", command=troot.destroy).place(x=130, y=60)
            troot.geometry("350x100")
            troot.mainloop()
        else:
            self.master.destroy()
            self.finalcalc(rage,cage,contri,exprt,anprd,perann,exprtann)
    def finalcalc(self,rage,cage,contri,exprt,anprd,perann,exprtann):
        servicetime=self.rage-self.cage                       #total no of investement years
        totalinvst=servicetime*12*contri                #total amount of money invested.
        final=0.0
        for i in range(servicetime*12):                                 #to calculate interested amount
            final+=self.contri*((1+(self.exprt/12))**i)
        gratuity=final*((100-self.self.perann)/100)           #gratuity
        amntinvstdannty=final*(self.perann/100)                  #amount from total amount after service years which will be invested into annuity service
        pnsnwgen=amntinvstdannty+(amntinvstdannty*self.exprtann*self.anprd)       #final amount from which pension will be calculated
        pension=pnsnwgen/(self.anprd*12)                         #final monthly pension



        from matplotlib import pyplot as plt        #To draw bar graph between total investment and total corpus
        y=[totalinvst,final]
        x=["Total investment","Total corpus"]
        w=[0.4]
        plt.bar(x,y,width=w,color=['red','green'])
        plt.show()

        #for pie chart
        labels =['Gratuity','Annuity']
        sizes = [gratuity,amntinvstdannty]
        explode = (0, 0.1)
        plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%',shadow=True, startangle=90)
        plt.show()

        fifig = Tk()                #To draw final pension report
        fifig.geometry("900x400")
        fifig.title("Pension Report")
        head = Label(fifig, text="Result")
        head.config(font=("Georgia", 28))
        head.place(x=400, y=10)

        head2 = Label(fifig, text="You will have accumulated ₹")
        head2.config(font=("Georgia", 18))
        head2.place(x=80, y=60)
        head3 = Label(fifig, text="%.2f"%final)
        head3.config(font=("Leelawadee UI", 18))
        head3.place(x=390, y=60)
        head4 = Label(fifig, text="by the time you retire")
        head4.config(font=("Georgia", 18))
        head4.place(x=520, y=60)

        w = Canvas(fifig, height=5, width=900)
        w.place(x=0, y=100)
        w.create_line(40, 2, 860, 2)

        Label(fifig, text="Principal amount invested by you :").place(x=70, y=120)
        Label(fifig, text="₹").place(x=70, y=140)
        Label(fifig, text="%.2f"%totalinvst).place(x=80, y=140)
        Label(fifig, text="Amount reinvested into Annuity :").place(x=610, y=120)
        Label(fifig, text="₹").place(x=610, y=140)
        Label(fifig, text="%.2f"%amntinvstdannty).place(x=620, y=140)
        Label(fifig, text="Interest earned on investment :").place(x=70, y=180)
        Label(fifig, text="₹").place(x=70, y=200)
        Label(fifig, text="%.2f"%(final-totalinvst)).place(x=80, y=200)
        Label(fifig, text="Gratuity (Lump sum amount withdrawn) :").place(x=610, y=180)
        Label(fifig, text="₹").place(x=610, y=200)
        Label(fifig, text="%.2f"%gratuity).place(x=620, y=200)
        Label(fifig, text="Pension wealth generated : ").place(x=70, y=240)
        Label(fifig, text="₹").place(x=70, y=260)
        Label(fifig, text="%.2f"%pnsnwgen).place(x=80, y=260)
        Label(fifig, text="Pension per month post retirement (Annuity) : ").place(x=610, y=240)
        Label(fifig, text="₹").place(x=610, y=260)
        Label(fifig, text="%.2f"%pension).place(x=620, y=260)
        fifig.mainloop()
        

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
        iExit =messagebox.askyesno("Emplyoee Database Details system", "confirm if you want to exit")
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
        iExit = messagebox.askyesno("Admin Database managment system", "confirm if you want to exit")
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



        
                
                


        
