import datetime

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.created_at = datetime.datetime.now()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")

    def __str__(self):
        return f"Account('{self.owner}', Balance=${self.balance})"


if __name__ == "__main__":
    my_account = BankAccount("Aditya", 100)
    
    print(f"Created: {my_account}")
    my_account.deposit(50)
    my_account.withdraw(30)
    my_account.withdraw(200) 