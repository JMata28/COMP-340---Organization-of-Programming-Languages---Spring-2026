//Example generated using AI (ChatGPT)

using System;
using System.Collections.Generic;

// Base class (OOP)
class Animal
{
    // In C#, methods must be marked 'virtual' to allow overriding (polymorphism)
    public virtual string Speak()
    {
        return "Some generic animal sound";
    }
}

// Single inheritance
class Dog : Animal
{
    public override string Speak()
    {
        return "Bark";
    }
}

class Cat : Animal
{
    public override string Speak()
    {
        return "Meow";
    }
}

/*
 * In C#, multiple inheritance with classes is NOT allowed (similar to Java).
 * Example (this would cause an error):
 * class RobotDog : Dog, Walker  //  Not allowed if Walker is a class
 *
 * Why?
 * To avoid ambiguity (diamond problem) where multiple base classes
 * could define conflicting implementations.
 *
 * Instead, C# uses INTERFACES to achieve multiple inheritance-like behavior.
 * Unlike Python, where multiple inheritance is allowed directly,
 * C# separates "what you are" (class) from "what you can do" (interfaces).
 */
interface IWalker
{
    string Walk();
}

// "Multiple inheritance" using interface
class RobotDog : Dog, IWalker
{
    public override string Speak()
    {
        return "Electronic bark";
    }

    public string Walk()
    {
        return "Walking on land";
    }
}

class Program
{
    static void Main()
    {
        // --- Polymorphism in action ---
        List<Animal> animals = new List<Animal>
        {
            new Dog(),
            new Cat(),
            new RobotDog()
        };

        foreach (Animal a in animals)
        {
            Console.WriteLine(a.Speak()); // Same method call, different behavior
        }

        // Using "multiple inheritance" behavior via interface
        RobotDog r = new RobotDog();
        Console.WriteLine(r.Walk());
    }
}