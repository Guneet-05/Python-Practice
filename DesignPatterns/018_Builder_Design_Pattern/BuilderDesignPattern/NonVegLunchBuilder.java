package DesignPatterns.BuilderDesignPattern;

public class NonVegLunchBuilder extends MealBuilder {
    private Meal meal = new Meal();

    public void reset() {
        meal = new Meal();
    }

    public void addBurger() {
        meal.burger = "Chicken Burger";
    }

    public void addDrink() {
        meal.drink = "McFlurry";
    }

    public void addSweet() {
        meal.sweet = "Gulab Jamun";
    }

    public void addFries() {
        meal.fries = "Chicken Fries";
    }

    public Meal getMeal() {
        return meal;
    }
}
