package FactoryMethodDesignPattern;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CarRentService cs = new MarutiService();
		System.out.println(cs.rentCar(100));
	}

}
