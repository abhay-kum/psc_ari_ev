import postfix_eval1 as pe
import infix_to_postfix as ip
import os
from socket import *
host = ""
port = 13000
buf = 2048
addr = (host, port)
T = socket(AF_INET, SOCK_STREAM)
T.bind(addr)
T.listen(1)

while True:
    print "waiting for connection"
    c,c_a=T.accept()
    print "Received message from \n: " ,c_a
    while True:
       
       data1=c.recv(buf)
       print "Arithmatic Expression:\n",data1
       data2=ip.InfixToPostfix(data1)
       data3=pe.postfixEval(data2)
       #UDPSock.sendto(str(data3), addr)
       c.sendall(str(data3))
       if data1=="exit":
         break;
    c.close()
