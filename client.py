# Save as client.py 
# Message Sender
import os
from socket import *
host = "127.0.0.1" # set to IP address of target computer
port = 13000
addr = (host, port)
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("Enter the artmatic expression for evaluation or type 'exit': ")
    UDPSock.sendto(data, addr)
    (data1, addr) = UDPSock.recvfrom(buf)
    if data1== "exit":
         break
    else:
          print"the ans is :\t" + data1
    if data == "exit":
        break
   
UDPSock.close()
os._exit(0)
