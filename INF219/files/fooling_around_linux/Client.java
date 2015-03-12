import java.io.Socket;
import java.io.DataOutputStream;
class Client {

public static void main(String[] args) {
        //DownloadWebPageTask task = new DownloadWebPageTask();
        //task.execute(new String[] { "http://192.168.0.201/pinoff.php" });

        try {
            	Socket socket = new Socket("192.168.0.1",1755);
		DataOutputStream DOS = new DataOutputStream(socket.getOutputStream());
		DOS.writeUTF("ON");
		socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
