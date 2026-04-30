//Example generated using AI (ChatGPT)

// Base class (OOP)
class Animal {
    speak() {
        return "Some generic animal sound";
    }
}

// Single inheritance
class Dog extends Animal {
    speak() {
        return "Bark";
    }
}

class Cat extends Animal {
    speak() {
        return "Meow";
    }
}

// Another base class (for multiple inheritance)
class Walker {
    walk() {
        return "Walking on land";
    }
}

// Multiple inheritance workaround (JS doesn't support it directly)
// We use a mixin
function mixin(targetClass, sourceClass) {
    Object.getOwnPropertyNames(sourceClass.prototype).forEach(name => {
        if (name !== "constructor") {
            targetClass.prototype[name] = sourceClass.prototype[name];
        }
    });
}

// "Multiple inheritance"
class RobotDog extends Dog {
    speak() {
        return "Electronic bark";
    }
}

// Apply Walker behavior to RobotDog
mixin(RobotDog, Walker);

// --- Polymorphism in action ---
const animals = [new Dog(), new Cat(), new RobotDog()];

animals.forEach(a => {
    console.log(a.speak()); // Same method call, different behavior
});

// Using "multiple inheritance" method. Multiiple inheritance is not native in JS so we simulate using a mixin
const r = new RobotDog();
console.log(r.walk());