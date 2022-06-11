import smtplib
from email.message import EmailMessage

server = smtplib.SMTP("smtp-mail.outlook.com", '587')

server.ehlo() 
server.starttls()

server.login("mail", "pass")

message = EmailMessage()

message['Subject'] = "Subject"
message['From'] = "mail"
message['To'] = "mail-receptor"
message.set_content("Hello from python")

server.send_message(message)
server.quit()
