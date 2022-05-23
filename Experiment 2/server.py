#Python library to use socket communication
import socket

#Host and port number to host server to
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

'''
socket.socket() creates the socket object, socket.AF_INET specify the address 
family, here Internet address family for IPv4 and SOCK_STREAM is the socket type 
for TCP, i.e TCP protocol will be used to transport messages
'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #bind the server object to the host nad port provided
    s.bind((HOST, PORT))
    #Make the listening socket
    s.listen()

    #Wait for the connection with client
    conn, addr = s.accept()

    #if connection is established 
    with conn:
        #Prind connected message
        print('Connected to client with', addr)
        #In loop
        while True:
            #Receive the data from the client
            data = conn.recv(1024)
            #If nothing is received i.e empty bytes object, b'' then break communication
            if not data:
                break
            #Else print data after converting into string
            print("Received: " + repr(data))
            #Now take the data from the user which needs to be sent to client
            new_data = str(input("Type the data to send back to client: "))
            #Convert the data from string to bytes and then send it to client
            conn.sendall(bytes(new_data, 'utf-8'))


#Note: Since I have used (with) to open a server, so I don't need to close it explicitly