#include <iostream>
using namespace std;

int main() {
    int x = 3.7;        // implicit conversion: double → int
    char c = 65;        // implicit conversion: int → char ('A') 
    bool flag = 10;     // implicit conversion: int → bool (true)

    cout << x << endl;     // prints 3
    cout << c << endl;     // prints A
    cout << flag << endl;  // prints 1 (true)

    return 0;
}

//Why was 65 converted to A?
//Because that is the ASCII value! See the table here: https://www.asciitable.com/ 