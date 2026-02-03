//Static type checking in C++

#include <iostream>
#include <string>
using namespace std;

int main(){
    int testVar = "Hello";       // ❌ Type error: can't assign a string to an int
    int result = 15 * "abc";     // ❌ Type error: can't multiply int by string
    string testResult = 14 * 150;  // ❌ Type error: can't assign int to string
    return 0;
}