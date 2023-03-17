package Bridge.solution;

public class Message {
	String from;
	String to;
	String title;
	String body;
	MessageSender sender;
	
	Message() {
		
	}
	
	Message(String to,String from,String title,String body,MessageSender sender) {
		this.to = to;
		this.from = from;
		this.title = title;
		this.body = body;
		this.sender = sender;
	}
	
	void send() {
		sender.send(from,to,title,body);
	}
}
