package AbstractFactoryDesignPattern;

public class CarRentService {
	
	private ICarFactory cf;

	void setCarFactory(ICarFactory cf) {
		this.cf = cf;
	}
	
	int rentCar(int kms) {
		ICar car = cf.getCar();
		car.start();
		int bill = car.pricePerKm() * kms;
		car.stop();
		return bill;
	}
	
}
