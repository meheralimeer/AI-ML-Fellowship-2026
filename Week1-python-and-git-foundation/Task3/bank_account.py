"""Bank Account System | OOP Concepts"""

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance
        self._transaction_history = []
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        
        self._balance += amount
        self._transaction_history.append(f"Deposit: +${amount}")
        print(f"Deposited ${amount}. New balance: ${self._balance}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        
        if amount > self._balance:
            print("Insufficient funds")
            return False
        
        self._balance -= amount
        self._transaction_history.append(f"Withdrawal: -${amount}")
        print(f"Withdrew ${amount}. New balance: ${self._balance}")
        return True
    
    def get_balance(self):
        return self._balance
    
    def get_transaction_history(self):
        return self._transaction_history
    
    def __str__(self):
        return f"Account({self._account_number}): {self._account_holder} - Balance: ${self._balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._transaction_history.append(f"Interest: +${interest:.2f}")
        print(f"Applied interest: ${interest:.2f}. New balance: ${self._balance:.2f}")
        return interest
    
    def __str__(self):
        return f"SavingsAccount({self._account_number}): {self._account_holder} - Balance: ${self._balance} (Rate: {self.interest_rate*100}%)"


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        
        if amount > self._balance + self.overdraft_limit:
            print(f"Exceeds overdraft limit of ${self.overdraft_limit}")
            return False
        
        self._balance -= amount
        self._transaction_history.append(f"Withdrawal: -${amount}")
        print(f"Withdrew ${amount}. New balance: ${self._balance}")
        return True
    
    def __str__(self):
        return f"CheckingAccount({self._account_number}): {self._account_holder} - Balance: ${self._balance} (Overdraft: ${self.overdraft_limit})"


if __name__ == "__main__":
    print("Bank Account System Demo =-\n")
    
    savings = SavingsAccount("SAV001", "Alice", 1000, 0.05)
    print(savings)
    savings.deposit(500)
    savings.apply_interest()
    print()
    
    checking = CheckingAccount("CHK001", "Bob", 500, 200)
    print(checking)
    checking.withdraw(600)
    checking.deposit(300)
    print()
    
    print("Transaction History:")
    for transaction in checking.get_transaction_history():
        print(f"  {transaction}")
