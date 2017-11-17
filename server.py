import postfix_eval1 as pe
import infix_to_postfix as ip
import os
from socket import *
host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Waiting to receive messages..."

while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print "A request from ip: \t" + addr[0] 
   
    print "Received message: " + data
    if data == "exit":
        break
    else:
       data2=ip.InfixToPostfix(data)
       data3=pe.postfixEval(data2)
       UDPSock.sendto(str(data3), addr)
      
        
UDPSock.close()
os._exit(0)
