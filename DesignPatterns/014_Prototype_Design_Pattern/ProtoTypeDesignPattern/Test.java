package ProtoTypeDesignPattern;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Circle c1 = new Circle();
		c1.rad = 10;
		c1.x = 100;
		Circle c2 = (Circle) c1.cloneShape();
		System.out.println(c1);
		System.out.println(c2);
		System.out.println(c2.rad);
		System.out.println(c2.x);
	}

}

//There is a way in which the objects will always be deep copied
//This is called serialize and deserialize. First, we will serialize an object i.e.
// convert it to bits and then create an object and deserialize it.

//Java gives clone() method in the Object class
// and also has an ICloneable interface for implementing the prototype design pattern.