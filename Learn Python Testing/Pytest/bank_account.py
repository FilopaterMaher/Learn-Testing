class BankAccount:
    def __init__(self, initial_balance = 0) -> None:
        self.balance = initial_balance
        self.transactions = []
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
        return self.balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw {amount}")
        return self.balance
    
    