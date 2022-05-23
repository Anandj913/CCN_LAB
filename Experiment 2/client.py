#Python library to use socket communication
import socket

#Host and port number of the server
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

'''
socket.socket() creates the socket object, socket.AF_INET specify the address 
family, here Internet address family for IPv4 and SOCK_STREAM is the socket type 
for TCP, i.e TCP protocol will be used to transport messages
'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	#Connect to the host
    s.connect((HOST, PORT))

    #Take input from the user to send to server
    data = str(input("Type the data to send to Server: "))

    #Convert the string type data into bytes to send to server
    data = bytes(data, 'utf-8')

    #Send data to server
    s.sendall(data)

    #Receive incoming data from server 
    data = s.recv(1024)

#Close the client and print the data received from server after converting into string
print('Received', repr(data))

#Note: Since I have used (with) to open a client, so I don't need to close it explicitly