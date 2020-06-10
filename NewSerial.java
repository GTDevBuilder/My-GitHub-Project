package sample;

import com.fazecast.jSerialComm.*;
import java.util.*;
import java.io.*;


public class NewSerial {

    public SerialPort userPort;
    public InputStream inStream;

    //constructor
    public NewSerial() {

    }

    public static void main(String args[]) throws IOException {
        NewSerial tstPort = new NewSerial();
        tstPort.OpenSerialPort("ttyUSB0");
        tstPort.getSerialStream();
       // System.out.println(new String(tstPort.getSerialStream()));
    }
    /*
     This returns an array of commport addresses, not useful for the client
     but useful for iterating through to get an actual list of com parts available
    */
    //Get serial port function
    public void getSerialPort() {
        Scanner input = new Scanner(System.in);
        SerialPort ports[] = SerialPort.getCommPorts();
        int i = 1;
        //User port selection
        System.out.println("COM Ports available on machine");
        for (SerialPort port : ports) {
            //iterator to pass through port array
            System.out.println(i++ + ": " + port.getSystemPortName()); //print windows com ports
        }
        System.out.println("Please select COM PORT: 'COM#'");
        SerialPort userPort = SerialPort.getCommPort(input.nextLine());
    }

    //Open Serial port
    public void OpenSerialPort(String portName) {
        userPort = SerialPort.getCommPort(portName);
        //Initializing port
        userPort.openPort();
      //IF port is open set up serial parameters
        if (userPort.isOpen()) {
            System.out.println("Port initialized!");
            userPort.setBaudRate(4800);
            userPort.setNumDataBits(8);
            userPort.setNumStopBits(SerialPort.ONE_STOP_BIT);
            userPort.setParity(SerialPort.NO_PARITY);
            //timeout not needed for event based reading
            //userPort.setComPortTimeouts(SerialPort.TIMEOUT_READ_SEMI_BLOCKING, 2000, 0);
            userPort.setComPortTimeouts(SerialPort.LISTENING_EVENT_DATA_RECEIVED, 1000, 0);
            inStream = userPort.getInputStream();
        } else {
            System.out.println("Port not available");
            return;
        }
    }

    public void getDataAvailable() {
        userPort.addDataListener(new SerialPortDataListener() {
            @Override
            public int getListeningEvents() {
                return SerialPort.LISTENING_EVENT_DATA_AVAILABLE;
            }

            public void serialEvent(SerialPortEvent event) {
                if (event.getEventType() != SerialPort.LISTENING_EVENT_DATA_AVAILABLE)
                    return;

                //Print data stream
                System.out.println(new String(getDataStream()));
            /*  byte[] newData = new byte[userPort.bytesAvailable()];
                int numRead = userPort.readBytes(newData, newData.length);
                System.out.println("Read " + numRead + " bytes.");
            */
            }
        });
    }

//Adding a receive listener, Not needed for GPS application
    public void getDataReceived() {
        userPort.addDataListener(new SerialPortDataListener() {
            @Override
            public int getListeningEvents() {
                return SerialPort.LISTENING_EVENT_DATA_RECEIVED;
            }

            public int getPacketSize() {
                return 100;
            }

            public void serialEvent(SerialPortEvent event) {
                byte[] newData = event.getReceivedData();
                int numRead = userPort.readBytes(newData, newData.length);
                System.out.println("Read data of size:  " + newData.length);

                //Printing one character at a time
                for (int i = 0; i < newData.length; i++) {
                    System.out.println((char) newData[i]);
                    System.out.println("\n");
                }
            }
        });
    }

    //Getting serial stream data.  Reading in NMEA stream
    public void getSerialStream() throws IOException {
        byte[] buffer = new byte[240];
        boolean end = false;
        String message = "blah";
//        String token[];
        while (!end) {
            Arrays.fill(buffer, (byte) 0);
            int len = inStream.read(buffer);
            if (len > 0) {
                message = new String(buffer);
             //   System.out.println(message);
                parseStream(message);
            }
            len = 0;
        }
    }

    public void parseStream(String msg) {
        String messages[];
        String token[];
        boolean end = false;
        //Split NMEA stream data
        messages = msg.split("\n");
        // System.out.println("Number of Messages" + messages.length);
        for (int i = 0; i < messages.length; i++) {
            // System.out.println("Message Number" + i);
            // System.out.println(message);
            //Stream of interest
            if (messages[i].contains("$GPRMC")) {
                System.out.println(messages[i]);
                token = messages[i].split(",");
                //Parsing out lat and long data
                if (token.length > 11) {
                    System.out.println("Lat: " + token[3] + token[4]);
                    System.out.println("Long: " + token[5] + token[6]);
                //Breaking out time
                    if(token[1].length() > 6){
                        System.out.println("Time is: " + token[1].substring(0, 2)
                                                        + ":" + token[1].substring(2, 4)
                                                        + ":" + token[1].substring(4,6));
                     }
                }
            }
            if (messages[i].equals("END")) {
                end = true;
            }
        }
    }

    public byte[] getDataStream() {

        int bytesAvailable = this.userPort.bytesAvailable();
        byte[] buffer = new byte[bytesAvailable];
        this.userPort.readBytes(buffer,bytesAvailable);
        return buffer;

    }

}
