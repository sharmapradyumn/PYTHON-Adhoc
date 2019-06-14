#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recvp_port=4444 # 0-1024 ---you can check free port  netstat -nulp
#creating udp socket
#1st argument ipv4 type 2nd UDP
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#fitting ip and port with udp socket

s.bind((recv_ip,recvp_port))
while 4>3 :
   data=s.recvfrom(100)
   print("message from sender",data[0])
   print("ip of sender", data[1])
   print(data)
#reply
   reply=raw_input("reply the sender")
   s.sendto(reply,data[1])

