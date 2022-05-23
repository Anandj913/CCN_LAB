Instructions to run the code:

Step 1: Compile Server using javac Server.java
Step 2: Compile Client using javac Client.java. 
Step 3: Create a messages.txt file which contains the messages that the client will read and send to the server

Open two seperate terminals: 

In 1st terminal 
Run server using java Server <port number> <probability of error> <channel delay (ms)>
Example: java Server 8080 0.2 500

In second terminal
Run Client using java Client <hostname> <port> <messages filepath>
Example: java Client localhost 8080 ./messages.txt

Communication will start and you can see the results in the terminal output. 


