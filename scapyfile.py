#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 14:44:38 2025

@author: kali
"""

from scapy.all import *
import concurrent.futures

target = '192.168.1.1'
def packet(flag,port):
    return IP(dst=target)/TCP(dport=port,flags=flag)

def scanport(port):
    pack= packet("S",port)
    res = sr1(pack,timeout=1,verbose=0)
    
    if res != None:
        if res.haslayer(TCP):
            if res.getlayer(TCP).flags == 0x12:
                print(f'[+] Port {port} is Open!!')
                p = pack('R',port)
                send(p,verbose=0)
    
    

if __name__ == '__main__':
    startPort = int(input())
    endPort = int(input())
    
    for i in range(startPort,endPort+1):
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as th:
            th.submit(scanport,i)
    

    
    
    