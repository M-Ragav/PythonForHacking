#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 17:16:21 2025

@author: kali
"""

import socket
import concurrent.futures

def grab_banner(target,port):
    try:
        pack = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        pack.settimeout(2)
        pack.connect((target,port))
        ban = pack.recv(1024)
        print(f'Port No.[{port}] Banner ==> {ban.decode().strip()}')
        pack.close()
    except Exception as e:
        print(f'Fail to captured banner in port no.[{port}] == [{e}]!!')

def port_scan(target,port):
    pack= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    pack.settimeout(1)
    res = pack.connect_ex((target,port))
    if res == 0:
        print(f'--> Port No.[{port}] Open!!')
        grab_banner(target,port)
    pack.close()


if __name__ == "__main__":

    target = '192.168.1.21'

    print(f'Started scanning the ports of {target}....')

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as th:
        for port in range(1,1001):
            th.submit(port_scan, target, port)
    
    print('[*] Scanning compeleted!!..')