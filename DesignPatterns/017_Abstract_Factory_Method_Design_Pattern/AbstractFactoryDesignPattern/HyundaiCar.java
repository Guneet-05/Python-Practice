package AbstractFactoryDesignPattern;

public class HyundaiCar implements ICar {

	@Override
	public void start() {
		System.out.println("Hyundai Car Start Logic");
	}

	@Override
	public void stop() {
		System.out.println("Hyundai Car stop logic");
	}
	
	@Override
	public int pricePerKm() {
		return 10;
	}

}