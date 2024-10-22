
# Bank Account

class BankAccount:
    def __init__(self, account_holder, bank_name="Default Bank", interest_rate=0.0):
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.interest_rate = interest_rate
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}.")



if __name__ == "__main__":
    account1 = BankAccount("Alice")

    # Perform operations
    account1.deposit(100.0)
    account1.check_balance()
    account1.withdraw(50.0)
    account1.check_balance()
    account1.withdraw(70.0)
