import smtplib
import ssl
from email.message import EmailMessage

subject = 'Email from python'
body = 'Test e-mail'
email_from = "aaravshah0011@gmail.com"
email_to = "aaravshah0011@gmail.com"
with open('pswd.txt', 'r') as file:
    pswd = file.read()


message = EmailMessage()
message["From"] = email_from
message["To"] = email_to
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, pswd)
    server.sendmail(from_addr=email_from, to_addrs=email_to, msg=message.as_string()) 
    
print("Done!")
    