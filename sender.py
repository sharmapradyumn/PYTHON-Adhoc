#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recvp_port=4444 # 0-1024 ---you can check free port  netstat -nulp
#creating udp socket
#1st argument ipv4 type 2nd UDP
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r=s.sendto("hello rr",(recv_ip,recvp_port))
print(r)
