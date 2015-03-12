import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.DataInputStream;
import java.net.ServerSocket;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

class Server {

public static void main(String[] args) {
        //DownloadWebPageTask task = new DownloadWebPageTask();
        //task.execute(new String[] { "http://192.168.0.201/pinoff.php" });

        try {
            	String msg_received;

		ServerSocket socket = new ServerSocket(1755);
		Socket clientSocket = socket.accept();       //This is blocking. It will wait.
		DataInputStream DIS = new DataInputStream(clientSocket.getInputStream());
		msg_received = DIS.readUTF();
		clientSocket.close();
		socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
