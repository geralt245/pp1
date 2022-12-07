class Account:

    def __init__(self, number):
        self.number = number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        new_balance = self.balance - amount

        if new_balance >= 0:
            self.balance = new_balance
        else:
            print("Insufficient funds on the account")

    def display_balance(self):
        print(f"Balance: PLN {self.balance}")

    def __str__(self):
        print("Bank Account no: {self.number}\nBalance: PLN {self.balance}")
