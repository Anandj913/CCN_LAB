# Receiver.py
import time, socket, sys
import random

print("Initialising Receiver....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
port = int(input(str("Enter port number: ")))
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

prob_error = float(input("Enter probabiity of error"))


while True:
   m=s.recv(1024)
   m=m.decode()
   k=s.recv(1024)
   k=k.decode()
   k=int(k)
   i=0
   a=""
   b=""
   f=random.randint(0,1)
   message=""
   while i!=k:
      f=random.uniform(0,1)
      if(f< prob_error):
       b="ACK Lost"
       message = s.recv(1024)
       message = message.decode()
       s.send(b.encode())

      else:
       b="ACK "+str(i)
       message = s.recv(1024)
       message = message.decode()
       
       s.send(b.encode())
       a=a+message
       i=i+1
       
    

   print("The message received is :", m)
   break

   
