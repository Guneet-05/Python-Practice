package Bridge.problem;

//Extending because of implementation
public class VoiceMailMessage extends Message{
	@Override
	void send() {
		// TODO Auto-generated method stub
		System.out.println("Title " + title);
		System.out.println("From " + from);
		System.out.println("To " + to);
		System.out.println("Body " + body);
		
		System.out.println("Sent via Voice Mail");
	}
}
