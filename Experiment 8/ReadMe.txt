To run the udp server and client code go to two diffrent terminal and run server first and then client 
To run the code make two files server.log and client.log and run as 
python server.py > server.log
python client.py > client.log
This will make two seperate file cwnd_data.log and cwnd_data_all.log 
after this run plot_cwnd.py to save cwnd-ssthresh plot

NOTE: 1) The code use asyncio liberary so make sure it is installed
      2) The code will run only on python version >=3.7, in all the rest error will show up


