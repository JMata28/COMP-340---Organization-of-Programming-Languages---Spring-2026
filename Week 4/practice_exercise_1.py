class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance -  amount

    def display_balance(self):
        print(f"The account of user {self.owner_name} has a balance of ${self.balance}")

account_1 = BankAccount("Jerry", 100)
account_1.display_balance()
account_1.deposit(20)
account_1.display_balance()
account_1.withdraw(30)
account_1.display_balance()