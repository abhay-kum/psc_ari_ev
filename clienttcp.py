import os
from socket import *
host = "127.0.0.1"
port = 13000
buf = 2048
addr = (host, port)
T = socket(AF_INET, SOCK_STREAM)
print" connecting to server"
T.connect(addr)

while (1):
       data=raw_input("Enter the Arithmatic expression for evaluation\n")
       T.sendall(data)
       data1=T.recv(buf)
       print" solution of the arithmatic expression  is:",data1
       if data=="exit":
          break;
os._exit(0)
       
