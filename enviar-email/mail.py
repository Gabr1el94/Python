import smtplib
import config

def send_mail(subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS,config.PASSWORD,message)
        server.quit()
        print("Success:Email Sent!")
    except Exception as e:
        print(e)
        print("Email failed to send.")

subject = "Test subject"
msg = "Hello there, How are you today?"

send_mail(subject,msg)