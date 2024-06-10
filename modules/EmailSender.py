import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class EmailSender:
    
    @staticmethod
    def send_email(email,url) -> None:
       
        port = 587 
        smtp_server = "smtp.gmail.com" #host for gmail
        sender_email = "" #sender email adress
        receiver_email = email #receiver email adress
        password = '' #app password for sender email account
        body = 'I FOUND NEW INTRESTING OFFER JUST FOR U <3 '+' '+ str(url)
        price_chart_path = 'resources\price_chart.jpg'
        course_chart_path = 'resources\course_chart.jpg'
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = "NEW CAR OFFER!"
        msg.attach(MIMEText(body,"plain"))

        with open(price_chart_path,"rb") as attachment: #price_chart
            part = MIMEBase('application','octet-stream')

            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',f"attachment; filename={price_chart_path}")
            msg.attach(part)
        
        with open(course_chart_path,"rb") as attachment: #course_chart
            part = MIMEBase('application','octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',f"attachment; filename={course_chart_path}")
            msg.attach(part)

        context = ssl.create_default_context()
        
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            
