import smtplib
import imghdr
import os
from email.message import EmailMessage
import face_recognition 

def mail():
    msg=EmailMessage()
    msg['from']='intrusion.alert.system@gmail.com'
    msg['to'] = 'intrusion.alert.system@gmail.com'
    msg['subject'] = 'ALERT'
    msg.set_content('unknown face detected')

#plebibsrhnhsfcki
    path=face_recognition.fr()
    with open('C:\\Users\\RamyaJyosna\\Desktop\\fr\\frame1.jpg','rb') as img:
        image_type=imghdr.what(img.name)
        msg.add_attachment(img.read(),maintype= 'image',subtype=image_type)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as s:
 
        s.login('intrusion.alert.system@gmail.com' ,'plebibsrhnhsfcki')
        s.send_message(msg)

    print('mailsent')


mail()