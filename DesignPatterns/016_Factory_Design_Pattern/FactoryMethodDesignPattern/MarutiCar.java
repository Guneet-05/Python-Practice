package FactoryMethodDesignPattern;

public class MarutiCar implements ICar {

	@Override
	public void start() {
		// TODO Auto-generated method stub
		System.out.println("Maruti car start logic");
	}

	@Override
	public void stop() {
		// TODO Auto-generated method stub
		System.out.println("Maruti Car stop logic");
	}
	
	@Override
	public int pricePerKm() {
		return 10;
	}

}
