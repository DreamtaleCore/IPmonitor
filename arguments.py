"""
Configuration file
"""
# -*- coding: UTF-8 -*-
import argparse

args = argparse.ArgumentParser(description='STMP e-mail super-parameters')

args.add_argument('--host', type=str, default='smtp.qq.com',
                  help='The host name of sender\'s e-mail.')
args.add_argument('--port', type=int, default=25,
                  help='The host port of sender\'s e-mail. (e.g. QQ: 456 or 587)')
args.add_argument('--user', type=str, default='xxxxxxxxxx@qq.com',
                  help='The user\'s email name')
args.add_argument('--password', type=str, default='xxxxxxxxxxx',
                  help='The user\'s email pwd')

args.add_argument('--sender_name', type=str, default='DreamTale',
                  help='The user\'s cute name in email')
args.add_argument('--receiver_list', type=list,
                  default=[
                      'lyunfei@buaa.edu.cn',
                      'liuyunfei.cs@gmail.com'
                  ],
                  help='The receivers\' email address list')
args.add_argument('--interval_delay', type=float, default=10.,
                  help='The interval time of frequency on checking IP.')
args.add_argument('--timeout', type=float, default=5.,
                  help='The max time to wait web return the IP address (second).')


def get_args():
    return args.parse_args()
