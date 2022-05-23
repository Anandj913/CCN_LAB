import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
public class Client {

    public static void main(String[] args) throws IOException {
        if (args.length != 3) {
            System.out.println("Usage: java Client <hostname> <port> <filepath>");
            System.exit(1);
        }
	// Variable to store time
        double sendingDelay = 0;
        long startTime = System.currentTimeMillis();
        try(DatagramSocket socket = new DatagramSocket()){
	    // Set port address from user 
            InetAddress address = InetAddress.getByName(args[0]);
            int port = Integer.valueOf(args[1]);

	    // Read message from file 
            try(BufferedReader in = new BufferedReader(new FileReader(args[2]))){
                String value;
                while ((value = in.readLine())!=null) {
                    byte[] buf = value.getBytes();
                    DatagramPacket packet = new DatagramPacket(buf, buf.length, address, port);
                    boolean retransmit;
                    do {
			// Note sending time 
                        long timeBeforeSend = System.currentTimeMillis();
                        System.out.println("Trying to send below message in a packet: \n" + value);
                        socket.send(packet);
                        sendingDelay += System.currentTimeMillis() - timeBeforeSend;
			
			//Receive ACK or NACK
                        byte[] receiveBuf = new byte[256];
                        DatagramPacket receivePacket = new DatagramPacket(receiveBuf, receiveBuf.length);
                        socket.receive(receivePacket);
                        String received = new String(receivePacket.getData(), 0 , receivePacket.getLength());
                        
			// If NACK is received retransmit, else receive the packet
			if(received.equals("NACK")){
                            System.out.println("NACK received: retransmitting");
                            retransmit = true;
                        } else if(received.equals("ACK")){
                            System.out.println("ACK received: successfully transmitted ");
                            retransmit = false;
                        } else {
                            System.err.println("can't identify the received message: " + received);
                            return;
                        }
                    } while (retransmit);
                    System.out.println("transmission of current packet is complete...");
                }
                System.out.println("Closing Datagram socket ...");
            } catch(FileNotFoundException ex){
                System.err.println("Couldn't open the file " + args[2] + ". Please Check the path");
                return;
            }

	    // Print dealy and link Utilization 
            long totalDelay = System.currentTimeMillis() - startTime;
            double linkUtilization = sendingDelay / totalDelay;
            System.out.println("total sending delay is: " + sendingDelay + "ms");
            System.out.println("total delay is: " + totalDelay + "ms");
            System.out.println("link utilization is: " + linkUtilization);
        }
    }
}

