#include <iostream>
#include <string>

using namespace std;

int main(){


    // //Count based loop statement
    // int sum = 0;

    // for(int i = 1; i < 6; i ++) {
    //     sum = sum + i;
    //     cout << "The current value of sum is " << sum << endl;
    // }

    // //Collection based loop statement
    // int sum2 = 0;
    // int arr[] = {1, 2, 3, 4, 5};

    // for (int i2 : arr) {
    //     sum2 = sum2 + i2;
    //     cout << "The current value of sum2 is: " << sum2 << endl;
    // }

    //Condition-based loop (Post test loop)
    int sum3 = 0;
    int i3 = 1;

    do {
        sum3 = sum3 + i3;
        cout << "The current value of sum3 is: " << sum3 << endl;
        i3 = i3 + 1;
    } while (i3 < 6);


    return 0;
}
