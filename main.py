"""
Main logic: if the IP address changed, send the new IP-address as an e-mail to all users
"""
# -*- coding: UTF-8 -*-
import socket
import threading
import email_factory
import arguments

interval_delay = arguments.get_args().interval_delay
email_sender = email_factory.get_mail_manager()


def check_ip_address():
    ip_addr = None
    try:
        # get the ip address at first
        # get the computer's name
        computer_name = socket.getfqdn(socket.gethostname())
        # get the IP address
        ip_addr = socket.gethostbyname(computer_name)
    except Exception:
        print('Get IP address failed, need next turn and try again.')

    is_need_to_send = False
    with open('IP_address.txt', 'r') as fid:
        lines = fid.readlines()
        if len(lines) == 0:
            is_need_to_send = True
        else:
            if lines[0] != ip_addr:
                is_need_to_send = True
            else:
                is_need_to_send = False

    # if need to send the ip address, send it
    if is_need_to_send or not email_sender.send_success:
        # insure the connection is ok.
        print('='*50)
        print('IP changed to {}'.format(ip_addr))
        global email_sender
        email_sender = email_factory.get_mail_manager()
        email_sender.send(header='服务器IP变更通知', text='新的IP地址更新为：{}'.format(ip_addr))

        if email_sender.send_success:
            # update the IP_address file if and only if new ip address send successfully
            with open('IP_address.txt', 'w') as fid:
                fid.write(ip_addr)
        print('='*50)

    threading.Timer(interval_delay, check_ip_address).start()


if __name__ == '__main__':
    print('IP monitor is on, begin to detecting ...')
    check_ip_address()
