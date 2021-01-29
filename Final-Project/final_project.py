##################################################################################################################
#   Reference :                                                                                                   #
#   - https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975                       #
#   - https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib  #
#   - https://www.youtube.com/watch?v=JRCJ6RtE3xU&t=1313s                                                        #
##################################################################################################################

import os
import smtplib
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = input("email: ")
password = input('password: ')

receiver = open('receiver_list.txt', 'r') 
dataReceiver = receiver.read().splitlines()
# print(','.join(receiver.read().splitlines()))

msg = EmailMessage()
# msg = MIMEMultipart()
msg['Subject'] = 'Sharingan'
msg['From'] = email
msg['To'] = ','.join(dataReceiver)
# body = MIMEText('example')
# msg.attach(body)

msg.set_content('Anda terkena genjutsu')
with open('a.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
msg.add_attachment(file_data, maintype='image', subtype =file_type, filename=file_name)
 
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    # smtp.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
    smtp.send_message(msg)