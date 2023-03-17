package Bridge.solution;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MessageSender viaEmail = new EmailSender();
		Message msg = new EncryptedMessage("Iron Man", "Guneet", "I need your suit.", "Haven't you read the title yet. I need your suit.", viaEmail, "Love you 3000");
		msg.send();
	}

}
