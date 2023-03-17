package AbstractFactoryDesignPattern;

public class MarutiCar implements ICar {

	@Override
	public void start() {
		System.out.println("Maruti car start logic");
	}

	@Override
	public void stop() {
		System.out.println("Maruti Car stop logic");
	}
	
	@Override
	public int pricePerKm() {
		return 10;
	}

}
