package ProtoTypeDesignPattern;

public class Circle implements Shape{
	
	int x;
	int rad;
	
	Circle() {
//		makes hit to the the DB to set x and radius.
	}
	
	private Circle(int x, int rad) {
		this.x = x;
		this.rad = rad;
	}
	
	public Shape cloneShape() {
		return new Circle(this.x,this.rad);		
	}
}
