"""
Main logic: if the IP address changed, send the new IP-address as an e-mail to all users
"""
# -*- coding: UTF-8 -*-
import datetime
import threading
import email_factory
import arguments
import ip_checker

interval_delay = arguments.get_args().interval_delay


def check_ip_address():
    print('Getting the recent IP address, it may take a while ...')
    ip_addr = ip_checker.get_ip()
    print('The recent IP address is {}.'.format(ip_addr))

    email_sender = email_factory.get_mail_manager()
    is_need_to_send = False
    with open('IP_address.txt', 'r') as fid:
        lines = fid.readlines()
        if ip_addr is None:
            is_need_to_send = False
        elif len(lines) == 0:
            is_need_to_send = True
        else:
            if lines[0] != ip_addr:
                is_need_to_send = True
            else:
                is_need_to_send = False

    # if need to send the ip address, send it
    time_info = '[{}]'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    if is_need_to_send or not email_sender.send_success:
        # insure the connection is ok.
        print('='*75)
        print(time_info + ' IP address changes to {}'.format(ip_addr))

        email_sender.config()
        email_sender.send(header='服务器IP变更通知', text='新的IP地址更新为：{}\r\n\t时间: {}'.format(ip_addr, time_info))

        if email_sender.send_success:
            # update the IP_address file if and only if new ip address send successfully
            with open('IP_address.txt', 'w') as fid:
                fid.write(ip_addr)
        print('='*75)
    else:
        print('='*50)
        print(time_info + ' IP address not change.')
        print('='*50)

    threading.Timer(interval_delay, check_ip_address).start()


if __name__ == '__main__':
    print('IP monitor is on, start to detect ...')
    check_ip_address()
