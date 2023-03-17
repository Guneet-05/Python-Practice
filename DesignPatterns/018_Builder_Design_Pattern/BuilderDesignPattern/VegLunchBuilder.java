package DesignPatterns.BuilderDesignPattern;

public class VegLunchBuilder extends MealBuilder{
    
    private Meal meal = new Meal();

    public void reset() {
        meal = new Meal();
    }

    public void addBurger() {
        meal.burger = "Cheese Veg Burger";
    }

    public void addDrink() {
        meal.drink = "Thumbs Up";
    }

    public void addSweet() {
        meal.sweet = "Vanilla Ice Cream";
    }

    public void addFries() {
        meal.fries = "Small Fries";
    }

    public Meal getMeal() {
        return meal;
    }
}
