#!/usr/bin/python2
import socket
recv_ip="127.0.0.1"
recvp_port=4444 # 0-1024 ---you can check free port  netstat -nulp
#creating udp socket
#1st argument ipv4 type 2nd UDP
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4>3 :
    msg=raw_input("enter your message")
    r=s.sendto(msg,(recv_ip,recvp_port))
    print(s.recvfrom(20))
