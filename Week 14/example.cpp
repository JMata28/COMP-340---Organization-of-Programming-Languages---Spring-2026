//Example generated using AI (ChatGPT)

#include <iostream>
#include <vector>
using namespace std;

// Base class (OOP)
class Animal {
public:
    virtual string speak() {
        return "Some generic animal sound";
    }
};

// Single inheritance
class Dog : public Animal {
public:
    string speak() override {
        return "Bark";
    }
};

class Cat : public Animal {
public:
    string speak() override {
        return "Meow";
    }
};

// Another base class (for multiple inheritance)
class Walker {
public:
    string walk() {
        return "Walking on land";
    }
};

// Multiple inheritance
class RobotDog : public Dog, public Walker {
public:
    string speak() override {
        return "Electronic bark";
    }
};


//In C++, you must use virtual in the base class to get polymorphism
// Without it, you’d get static binding (wrong behavior)
int main() {
    // --- Polymorphism in action ---
    vector<Animal*> animals;
    animals.push_back(new Dog());
    animals.push_back(new Cat());
    animals.push_back(new RobotDog());

    for (Animal* a : animals) {
        cout << a->speak() << endl; // Same method call, different behavior
    }

    // Using multiple inheritance method
    RobotDog r;
    cout << r.walk() << endl;

    return 0;
}