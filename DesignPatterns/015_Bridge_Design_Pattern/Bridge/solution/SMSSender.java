package Bridge.solution;

public class SMSSender implements MessageSender {

	@Override
	public void send(String from, String to, String title, String body) {
		// TODO Auto-generated method stub
		System.out.println("From = " + from);
		System.out.println("To = " + to);
		System.out.println("Title = " + title);
		System.out.println("Body = " + body);
		System.out.println("This message was sent by an SMS");
	}
	
}
