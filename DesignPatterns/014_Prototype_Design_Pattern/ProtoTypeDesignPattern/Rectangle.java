package ProtoTypeDesignPattern;

import java.util.ArrayList;

public class Rectangle implements Shape {

	int tlx;
	int tly;
	int width;
	int height;
	ArrayList<Integer> list = new ArrayList<>();
	Rectangle() {
		
	}
	
	private Rectangle(int tlx, int tly, int width, int height,ArrayList<Integer> list) {
		this.tlx = tlx;
		this.tly = tly;
		this.width = width;
		this.height = height;
		//Deep copy
		for(int x : list) {
			this.list.add(x);
		}
	}
	
	@Override
	public Shape cloneShape() {
		// TODO Auto-generated method stub
		return new Rectangle(this.tlx,this.tly,this.width,this.height,this.list);
	}

}
