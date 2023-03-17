package FactoryMethodDesignPattern;

public class MarutiService extends CarRentService {

	@Override
	ICar getCar() {
		// TODO Auto-generated method stub
		return new MarutiCar();
	}

}
