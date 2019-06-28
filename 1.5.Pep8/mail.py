import imaplib
import email
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailSendReceive:

    def __init__(self, login, password, smtp_server, imap_server):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server

    def send_message(self, to_message, subject_message, body_message):
        # send message
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(to_message)
        msg['Subject'] = subject_message
        msg.attach(MIMEText(body_message))
        context_ssl = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, 465, context=context_ssl) as server:
            server.login(self.login, self.password)
            server.sendmail(self.login, to_message, msg.as_string())
        print('Message sended ...')

    def receive_message(self):
        # receive
        header = None
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        print('Received messages ...', email_message)
        mail.logout()


def main():
    mail_worker = MailSendReceive('muder75@gmail.co', '**********', 'smtp.gmail.com', 'imap.gmail.com')
    mail_worker.send_message(['muder75@gmail.com', 'dukov@icloudpocket.ru'],
                             'Пробная тема по отправке сообщения',
                             'Само сообщение, вот все что нужно ...')
    mail_worker.receive_message()


if __name__ == '__main__':
    main()
