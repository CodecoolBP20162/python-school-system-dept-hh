import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail:
    def __init__(self, recipient_list, message, subject):
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.user = 'codecool.depth@gmail.com'
        self.password = 'Creative4'
        self.recipient_list = recipient_list
        self.sender = 'codecool.depth@gmail.com'
        self.message = MIMEText(message.encode('utf-8'), _charset='utf-8')
        self.message['Subject'] = Header(subject, charset='utf-8')

    def send(self):
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.user, self.password)
        self.server.sendmail(self.sender, self.recipient_list, self.message.as_string())
        self.server.quit()


"""
recipient_list = ['recipient@gmail.com', 'recipient2@gmail.com']

message = '''
blablabla
blabla
blablablablabla
blablablablablabla
'''

subject = 'subject of the email'

testmail = Mail(recipient_list, message, subject)
testmail.send()
"""
