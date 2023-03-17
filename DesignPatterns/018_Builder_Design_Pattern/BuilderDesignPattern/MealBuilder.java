package DesignPatterns.BuilderDesignPattern;

public abstract class MealBuilder {
    public abstract void addBurger();
    public abstract void addDrink();
    public abstract void addSweet();
    public abstract void addFries();
    public abstract Meal getMeal();
    public abstract void reset();
}
