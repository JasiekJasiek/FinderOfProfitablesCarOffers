import smtplib
import ssl
from email.mime.text import MIMEText


class Email_sender:
    
    @staticmethod
    def send_email(email='mierzickiszymon1@gmail.com') -> None:
        sender = 'finderofprofitablescaroffers@gmail.com'
        reciver = [str(email)]
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.connect()
        s.starttls()
        s.login(sender,'lxaf xyyi arwd blsv')
        msg = MIMEText('I FOUND NEW INTRESTING OFFER JUST FOR U <3')
        msg['subject'] = 'NEW CAR OFFER!'
        msg['from'] = sender
        msg['to'] = reciver
        s.sendmail(sender,reciver,msg.as_string())
        s.quit()
        print("email sent")
    
    
Email_sender.send_email()
