package AbstractFactoryDesignPattern;

public class MarutiCarFactory implements ICarFactory{
    @Override
    public ICar getCar() {
        return new MarutiCar();
    }
}
