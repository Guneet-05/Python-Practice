package Bridge.problem;

//Extending because of implementation
public class EmailMessage extends Message{
	
	@Override
	public void send() {
		System.out.println("Title " + title);
		System.out.println("From " + from);
		System.out.println("To " + to);
		System.out.println("Body " + body);
		
		System.out.println("Sent via Email");
		
		//Logic to send this via email
	}
}
