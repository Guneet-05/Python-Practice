package Bridge.solution;

public class EncryptedMessage extends Message{
	String encryptionKey;
	
	EncryptedMessage(String to,String from,String title, String body,MessageSender sender, String key) {
		super(to,from,title,body,sender);
		this.encryptionKey = key;
		this.body = key + body;
	}
}
