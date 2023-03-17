package DesignPatterns.BuilderDesignPattern;

public class Test {
    public static void main(String[] args) {
        Director dir = new Director();
        dir.setMealBuilder(new VegLunchBuilder());
        Meal meal = dir.construct();
        System.out.println(meal.burger);
        System.out.println(meal.drink);
        System.out.println(meal.sweet);
        System.out.println(meal.fries);

        dir.setMealBuilder(new NonVegLunchBuilder());
        meal = dir.construct();
        System.out.println(meal.burger);
        System.out.println(meal.drink);
        System.out.println(meal.sweet);
        System.out.println(meal.fries);
    }   
}
