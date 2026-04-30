//Example generated using AI (ChatGPT)

// In Rust, there is no classical OOP inheritance like Python/Java/C++.
// Instead, Rust uses TRAITS (similar to interfaces) + composition.


// Base "class" behavior using a trait
trait Animal {
    fn speak(&self) -> String;
}

// Single inheritance equivalent (struct + trait implementation)
struct Dog;

impl Animal for Dog {
    fn speak(&self) -> String {
        "Bark".to_string()
    }
}

struct Cat;

impl Animal for Cat {
    fn speak(&self) -> String {
        "Meow".to_string()
    }
}

/*
 * In Rust:
 * ❌ No class inheritance at all (single or multiple)
 * ❌ No "extends" or "base class"
 *
 * ✅ Instead, we use TRAITS to define shared behavior
 * ✅ Multiple "inheritance-like" behavior is done by implementing multiple traits
 *
 * This avoids problems like the diamond problem entirely.
 */

// Another trait (like Walker behavior)
trait Walker {
    fn walk(&self) -> String;
}

// "Multiple inheritance" equivalent: implement multiple traits
struct RobotDog;

impl Animal for RobotDog {
    fn speak(&self) -> String {
        "Electronic bark".to_string()
    }
}

impl Walker for RobotDog {
    fn walk(&self) -> String {
        "Walking on land".to_string()
    }
}

fn main() {
    // --- Polymorphism in action ---
    // Rust uses trait objects for runtime polymorphism
    let animals: Vec<Box<dyn Animal>> = vec![
        Box::new(Dog),
        Box::new(Cat),
        Box::new(RobotDog),
    ];

    for a in animals {
        println!("{}", a.speak()); // Same method call, different behavior
    }

    // Using "multiple inheritance" behavior via second trait
    let r = RobotDog;
    println!("{}", r.walk());
}