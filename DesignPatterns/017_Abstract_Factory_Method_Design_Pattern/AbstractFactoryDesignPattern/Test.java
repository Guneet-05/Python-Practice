package AbstractFactoryDesignPattern;

public class Test {
    public static void main(String[] args) {
        CarRentService rs = new CarRentService();
        rs.setCarFactory(new HyundaiCarFactory());
        System.out.println(rs.rentCar(1000));
    }
}

// When factory method is implemented using composition, it becomes abstract factory method

// Factory + Bridge = Abstract Factory