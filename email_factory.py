"""
The factory to generate mail_obj
------
::author    DreamTale
::date      2019/1/8
::mail      dreamtalewind@gmail.com
"""
# -*- coding: UTF-8 -*-
import smtplib
import arguments
from email.mime.text import MIMEText
from email.header import Header


class MyEmail:
    def __init__(self, config):
        self.host = config.host
        self.port = config.port
        self.user = config.user
        self.pswd = config.password
        self.sender_name = config.sender_name
        self.receiver_name_list = config.receiver_list

        self.smtp_obj = None
        self.connection_ok = True
        self.send_success = True

    def config(self):
        # 25 is the port number of SMTP protocol
        self.smtp_obj = smtplib.SMTP()
        self.connection_ok = True
        try:
            self.smtp_obj.connect(self.host, self.port)
            print('Connect to server successful.')
        except Exception:
            print('Cannot connect the SMTP server: {}'.format(self.host))
            self.connection_ok = False
        try:
            self.smtp_obj.login(self.user, self.pswd)
            print('Login successful.')
        except Exception:
            print('Cannot login to {}, check user name and its password.'.format(self.user))
            self.connection_ok = False

    def send(self, header, text):
        if self.smtp_obj is None:
            self.config()

        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = Header(self.sender_name)
        msg['Subject'] = Header(header, 'utf-8')
        msg['To'] = Header(','.join(self.receiver_name_list))
        try:
            self.smtp_obj.sendmail(self.user, self.receiver_name_list, msg.as_string())
            print('Send mail to {} successful!'.format(';'.join(self.receiver_name_list)))
            self.send_success = True
        except smtplib.SMTPException:
            print('Error: cannot send mail to {}.'.format(','.join(self.receiver_name_list)))
            self.send_success = False

    def close(self):
        self.smtp_obj.quit()


def get_mail_manager():
    g = arguments.get_args()
    return MyEmail(config=g)


def test_send_email():
    me = get_mail_manager()
    me.send(header='发送邮件测试', text='这里是测试内容')


if __name__ == '__main__':
    test_send_email()
