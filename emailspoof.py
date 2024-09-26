import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders 
import traceback


def send_mail(receiver_email, spoofed_email, spoofed_name, message, subject):
    try:
        msg = MIMEMultipart("related")
        msg['From'] = f"{spoofed_name} <{spoofed_email}>"
        msg['To'] = receiver_email
        msg['Subject'] = subject
        body = message
        msg.attach(MIMEText(body, 'plain'))
        
        smtp_host = "smtp-relay.brevo.com"
        smtp_port = 587
        smtp_username = "USERNAME"
        smtp_password = "PASSWORD"

        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(spoofed_email, receiver_email, text)
        server.quit()
        print('Spoofed Email sent successfully to '+ str(receiver_email) + ' from ' + str(spoofed_name))
    except Exception as e:
        print(traceback.format_exc())

receiver_email = ['MAILS']
spoofed_email = 'abc@abc.com'
 
spoofed_name = 'xyz' 
message = 'MESSAGE'
subject = 'this is the title of the spoofed email'

for i in range(len(receiver_email)):
    send_mail(receiver_email[i],spoofed_email,spoofed_name, message, subject)
