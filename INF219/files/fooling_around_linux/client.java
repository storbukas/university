import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

class client {

public static void main(String[] args) {
        //DownloadWebPageTask task = new DownloadWebPageTask();
        //task.execute(new String[] { "http://192.168.0.201/pinoff.php" });

        try {
            SocketAddress address = new InetSocketAddress("192.168.0.101", 12345);
            Socket clientSocket = new Socket();
            clientSocket.connect(address, 20000);
            DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
            //BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            outToServer.writeBytes("OFF");
            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
