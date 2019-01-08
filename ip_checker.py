from urllib import request
import re
import socket
import arguments


args = arguments.get_args()
def _get_public_ip():
    ip_pool = []
    try:
        my_ip = request.urlopen('http://ip.42.pl/raw', timeout=args.timeout).read()
        ip_pool.append(my_ip.decode('utf-8'))
    except Exception:
        pass
    try:
        text = request.urlopen('http://ifconfig.me', timeout=args.timeout).read()
        my_ip = re.search(r'\d+.\d+.\d+.\d+', str(text)).group(0)
        ip_pool.append(my_ip)
    except Exception:
        pass

    if len(ip_pool) == 0:
        print('Get IP address failed, need next turn and try again.')
        my_ip = None
    else:
        print('Find such public ip: [{}], using the first one.'.format(';'.join(ip_pool)))
        my_ip = ip_pool[0]

    return my_ip


def _get_local_ip():
    ip_addr = None
    try:
        # get the ip address at first
        # get the computer's name
        computer_name = socket.getfqdn(socket.gethostname())
        # get the IP address
        ip_addr = socket.gethostbyname(computer_name)
    except Exception:
        print('Get IP address failed, need next turn and try again.')
    return ip_addr


def get_ip(mode='public'):
    if mode == 'public':
        my_ip = _get_public_ip()
    else:
        my_ip = _get_local_ip()
    return my_ip


if __name__ == '__main__':
    my_ip = get_ip()
    print(my_ip)
