import java.net.*;
import java.util.Arrays;
import java.util.List;
import java.io.*;

public class Server {
    public static void main(String[] args) throws IOException, InterruptedException {
        if (args.length != 3) {
            System.err.println("Usage: java Server <port number> <probability of error> <channel delay (ms)>");
            System.exit(1);
        }
	// Defining the port number, probability of delay and channel delay from user argument
        int portNumber = Integer.parseInt(args[0]);
        double probabilityOfError = Double.parseDouble(args[1]);
        long channeldelay = Long.parseLong(args[2]);

	//boolean flag for server active state
        boolean listening = true;
	// Variable to set message number
        int messageNumber = 0;
        System.out.println("Server started ...");
	
	// Start receiving the packets
        try (DatagramSocket socket = new DatagramSocket(portNumber)) {
            while (listening) {
                byte[] buf = new byte[512];
                DatagramPacket packet = new DatagramPacket(buf, buf.length);
                System.out.println("Waiting for client ...");
                socket.receive(packet);

                // wait for time = channel delay
                Thread.sleep(channeldelay);

                // Random variable for prop of error
                double choice = Math.random();
                String responseString;

		//If random variable < prop of error send NACK else ACK
                if(choice < probabilityOfError){
                    System.out.println("Erronous packet received");
                    responseString = "NACK";
                } else {
                    messageNumber++;
                    String received = new String(packet.getData(), 0 , packet.getLength());
		    // If end is received then stop the server 
                    if(received.equalsIgnoreCase("end")){
                        listening = false;
                    }
                    System.out.println("Received message number " + messageNumber +  ":\n" + received );
                    responseString = "ACK";
                }
                InetAddress address = packet.getAddress();
                byte[] response = responseString.getBytes(); 
                int port = packet.getPort();
                packet = new DatagramPacket(response, response.length, address, port);
                socket.send(packet);
            }
        }
    }

}
