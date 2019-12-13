import sqlite3

def emplyoee_data():
    con = sqlite3.connect("emplyoee.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS emp (id INTEGER PRIMARY KEY, EmpId text, Firstname text, Surname text, Gender text, Age text, Mobile text, village text,password text,working_year text,base_salary text,username text,account_number text,gratuity text,DOB text,computaion text,pension text)")
    con.commit()
    con.close()

def AddEmpRec(EmpId , Firstname , Surname , Gender , Age , Mobile ,village ,password ,working_year,base_salary ,username ,account_number,gratuity ,DOB ,computaion ,pension ):
    con=sqlite3.connect("emplyoee.db")
    cur=con.cursor()
    cur.execute("INSERT INTO emp VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(EmpId,Firstname , Surname , Gender , Age , Mobile , village ,password ,working_year,base_salary ,username ,account_number,gratuity ,DOB ,computaion ,pension ))
    con.commit()
    con.close()


def viewData():
    con=sqlite3.connect("emplyoee.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM emp")
    row = cur.fetchall()
    con.close()
    return row

def deletRec(id):
    con = sqlite3.connect("emplyoee.db")
    cur = con.cursor()
    cur.execute("DELETE FROM emp WHERE id=?",(id,))
    con.commit()
    con.close()

def searchData(EmpId="" , Firstname="" , Surname="" , Gender="" , Age="" , Mobile="" ,village="" ,password="" ,working_year="",base_salary="" ,username="" ,account_number="",gratuity="" ,DOB="" ,computaion="" ,pension=""):
    con = sqlite3.connect("emplyoee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM emp WHERE EmpId=? OR  Firstname=? OR  Surname=? OR  Gender=? OR  Age=? OR  Mobile=? OR village=? OR password=? OR working_year=? OR base_salary=? OR username=? OR account_number=? OR gratuity=? OR DOB=? OR computaion=? OR pension=?",(EmpId , Firstname , Surname , Gender , Age , Mobile ,village ,password ,working_year,base_salary ,username ,account_number,gratuity ,DOB ,computaion ,pension ))
    rows=cur.fetchall()
    con.close()
    return  rows

def searchUserPass(password="" ,username="" ):
    con = sqlite3.connect("emplyoee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM emp WHERE  password=?  AND username=? ",(password ,username))
    rows=cur.fetchone()
    con.close()
    return  rows

def dataUpdate(id,EmpId="" , Firstname="" , Surname="" , Gender="" , Age="" , Mobile="" ,village="" ,password="" ,working_year="",base_salary="" ,username="" ,account_number="",gratuity="" ,DOB="" ,computaion="" ,pension=""):
    con=sqlite3.connect("students.db")
    cur=con.cursor()
    cur.execute("UPDATE student SET EmpId=? , Firstname=? , Surname=? , Gender=? , Age=? , Mobile=? ,village=? ,password=? ,working_year=?,base_salary=? ,username=? ,account_number=?,gratuity=? ,DOB=? ,computaion=? ,pension=?",(EmpId,Firstname , Surname , Gender , Age , Mobile , village ,password ,working_year,base_salary ,username ,account_number,gratuity ,DOB ,computaion ,pension ))
    con.commit()
    con.close()

emplyoee_data()
