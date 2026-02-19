// Protected items
//AI-generated example

#include <iostream>
using namespace std;

class Animal {
protected:
    int age;

public:
    Animal(int a) {
        age = a;
    }
};

class Dog : public Animal {
public:
    Dog(int a) : Animal(a) {}

    void printAge() {
        cout << age;   // Allowed (protected)
    }
};

int main() {
    Dog d(5);
    d.printAge();      // 5

    // d.age = 10;     Error: age is protected
}