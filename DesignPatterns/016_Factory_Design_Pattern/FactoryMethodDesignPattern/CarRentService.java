package FactoryMethodDesignPattern;

public abstract class CarRentService {
	int rentCar(int kms) {
		ICar car = getCar();
		car.start();
		int bill = car.pricePerKm() * kms;
		car.stop();
		return bill;
	}
	
//	Factory Method
	abstract ICar getCar();
}
