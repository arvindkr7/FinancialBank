import os
from email.message import EmailMessage
import smtplib

#email_addr=os.environ.get('email_userid')
#email_pass=os.environ.get('email_pass')
email_addr='kgrvnd@gmail.com'
email_pass='Bind@@s123'
msg=EmailMessage()
msg['Subject']='Grab the offer soon'
msg['From']=email_addr
msg['To']='ag30982@gmail.com'
msg.set_content('How about the offer in your account, you can have the maximum discount Today, SO grab it before expire')

with smtlplib.SMTP_SSL('smtp.gmail.com',587) as smtp:
    smtp.login(email_addr,email_pass)
    
    smtp.send_message(msg)