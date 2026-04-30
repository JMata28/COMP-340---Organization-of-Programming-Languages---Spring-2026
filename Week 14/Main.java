//Example generated using AI (ChatGPT)

import java.util.*;

// Base class (OOP)
class Animal {
    public String speak() {
        return "Some generic animal sound";
    }
}

// Single inheritance
class Dog extends Animal {
    @Override
    public String speak() {
        return "Bark";
    }
}

class Cat extends Animal {
    @Override
    public String speak() {
        return "Meow";
    }
}

/*
 * In Java, multiple inheritance with classes is NOT allowed.
 * Example (this would cause an error):
 * class RobotDog extends Dog, Walker { }  // Not allowed
 *
 * Why?
 * Because it can create ambiguity (the "diamond problem"),
 * where a class could inherit conflicting implementations
 * of the same method from multiple parent classes.
 *
 * Instead, Java uses INTERFACES to achieve similar behavior safely.
 * Interfaces define behavior (method signatures) without implementation,
 * so there is no ambiguity.
 */
interface Walker {
    String walk();
}

// "Multiple inheritance" using an interface
class RobotDog extends Dog implements Walker {
    @Override
    public String speak() {
        return "Electronic bark";
    }

    @Override
    public String walk() {
        return "Walking on land";
    }
}

public class Main {
    public static void main(String[] args) {
        // --- Polymorphism in action ---
        List<Animal> animals = Arrays.asList(
            new Dog(),
            new Cat(),
            new RobotDog()
        );

        for (Animal a : animals) {
            System.out.println(a.speak()); // Same method call, different behavior
        }

        // Using "multiple inheritance" behavior via interface
        RobotDog r = new RobotDog();
        System.out.println(r.walk());
    }
}