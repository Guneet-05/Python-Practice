package Bridge;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		The classes are extended due to 2 reasons
//		One is changing the API of the class i.e. adding more data members or method
//		removing or changing names of data members or methods, etc.
//		This is called changing the abstraction.
//		Another reason is for implementation i.e. no change in the number of
//		methods or members, just implementing a method i.e. changing its body
		
//		When a class is extended for both the reasons i.e. changing the API and 
//		implementation, the classes blast i.e. the number of classes increase a lot.
		
//		For instance, we have EncryptedMessage,IssueMessage,PriorityMessage classes derived from Message class
//		to change API i.e. add a String key data member.
//		We have a class EmailMessage,SMSMessage,VoiceMessage derived from the Message class
//		to implement the send() method.
//		Message is being derived for both the reasons. Now, no of classes increase
//		as follows
//		EncryptedEmail class, IssueMessageEmail class, PriorityEmail class,
//		EncryptedSMS, IssueMessageSMS, PrioritySMS, EncryptedVoice, 
//		IssueVoice, PriorityVoice	
//		So, No of classes = no of Subclasses due to abstraction * no of subclasses due to implementation
		
		
	}

}
