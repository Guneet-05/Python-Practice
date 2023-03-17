package Bridge.solution;

public class PriorityMessage extends Message {
	int priority;
	
	PriorityMessage(String to,String from,String title, String body,MessageSender sender, int p) {
		super(to,from,title,body,sender);
		this.priority= p;
		
		if(priority >= 50) body += "Very Important Message";
		else body += "Not so urgent message";
	}
}
