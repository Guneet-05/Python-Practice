package FactoryMethodDesignPattern;

public class HyundaiCar implements ICar {

	@Override
	public void start() {
		// TODO Auto-generated method stub
		System.out.println("Hyundai Car Start Logic");
	}

	@Override
	public void stop() {
		// TODO Auto-generated method stub
		System.out.println("Hyundai Car stop logic");
	}
	
	@Override
	public int pricePerKm() {
		return 10;
	}

}
