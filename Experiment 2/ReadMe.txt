This document specifies the process to run the code

System requirements
**
To run the server client code, you need to have socket library installed and your python version should be above 3.5
**

Step 1: Open two separate terminals

Step 2: In terminal 1, run the server code first to host the server
		For doing so, run python3 server.py
        This is necessary to run server first, o.w connection will be refused
        After this the terminal will freeze and will wait for the client

Step 3: In terminal 2, run the client code 
        For doing so, run python3 client.py
        Then client will ask for the data to send type that and enter

Step 4: This data will appear in server side, then server will ask for data to send
        to client, type that and enter

Step 5: This data will appear in client side, and connection will close.


