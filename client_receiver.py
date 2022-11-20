#this program writes the data received by WEMOS D1 via UDP protocol into a file
#AUTHOR: gabrieleOrtolani
#DATE: 20/11/2022

import socket

 

msgFromClient       = "hello, i'm the client"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("*****SERVER-ID****", ***SERVER-PORT****)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

f = open("report.txt", "a")
 

# Send to server using created UDP socket
while 1:
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
    f.write(msg+"\n")

f.close()





 

