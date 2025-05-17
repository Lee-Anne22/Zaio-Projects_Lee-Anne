class BankAccount:
    def __init__(self, initial_balance: float, account_number: str):
        self.__account_balance = initial_balance
        self.__account_number = account_number

    def deposit(self, amount: float):
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Invalid transaction: Insufficient funds or negative amount.")

    def get_balance(self):
        return self.__account_balance

# Creating an instance of BankAccount
account1 = BankAccount(1000.0, "123456789")

# Performing transactions
account1.deposit(500.0)
account1.withdraw(200.0)

# Printing final account balance
print("Final Account Balance:", account1.get_balance())
