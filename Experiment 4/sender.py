# Sender.py
import time, socket, sys


print("Initialising server....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = int(input("Enter port number"))
s.bind((host, port))
print(host, "(", ip, ")\n")

           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

message = input(str("Enter message: "))
# message = str("First msg to send the other side")
conn.send(message.encode())

f = str(int(input(str("Enter number of packets: "))))


lis = []
packet_size = int(len(message)/int(f))
while message:
    lis.append(message[:packet_size])
    message = message[packet_size:]

message = lis
f = len(message)-1
conn.send(str(f).encode())


i=0
j=0
j=int(input("Enter the window size: "))


b=""

j=j-1
f=int(f)
k=j

send_time = 0
start_time = time.time()*1000
while i!=f:
    while(i!=(f-j)):
        temp = time.time()*1000
        conn.send(message[i].encode())
        send_time = send_time + (time.time()*1000 - temp)
        b=conn.recv(1024)
        b=b.decode()
        print(b)
        if(b!="ACK Lost"):
            print("Acknowledgement Received! Window range [{0} to {1}]".format(i, k))
            i=i+1
            k=k+1
            time.sleep(1)
        else:
            print("Acknowledgement LOST! Window remains in the range [{0} to {1}]".format(i, k))
            time.sleep(1)
    while(i!=f):
        temp = time.time()*1000
        conn.send(message[i].encode())
        send_time = send_time + (time.time()*1000 - temp)
        b=conn.recv(1024)
        b=b.decode()
        print(b)
        if(b!="ACK Lost"):
            print("Acknowledgement Received! Window range [{0} to {1}]".format(i, k))
            i=i+1
            time.sleep(1)
        else:
            print("Acknowledgement LOST! Window remains in the range [{0} to {1}]".format(i, k))
            time.sleep(1)
print("Sending complete")
print("Total Sending time: {}".format(send_time))
print("Total time: {}".format(time.time()*1000 - start_time))
s.close()
        
 
