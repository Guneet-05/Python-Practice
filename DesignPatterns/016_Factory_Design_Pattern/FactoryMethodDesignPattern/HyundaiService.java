package FactoryMethodDesignPattern;

public class HyundaiService extends CarRentService{

	@Override
	ICar getCar() {
		// TODO Auto-generated method stub
		return new HyundaiCar();
	}
	
}
