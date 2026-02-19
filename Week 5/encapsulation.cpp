//Public and private items
//AI-Generated example

#include <iostream>
using namespace std;

class BankAccount {
private:
    double balance;   // hidden (encapsulated)

public:
    BankAccount(double initialBalance) {
        balance = initialBalance;
    }

    void deposit(double amount) {
        if (amount > 0)
            balance += amount;
    }

    double getBalance() const {
        return balance;
    }
};

int main() {
    BankAccount account(1000);
    account.deposit(500);
    cout << account.getBalance();  // 1500
}