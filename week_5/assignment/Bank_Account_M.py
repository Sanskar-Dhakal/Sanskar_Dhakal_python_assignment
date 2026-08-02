class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited into {self.account_number}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from {self.account_number}")

    def get_balance(self):
        print(f"Name: {self.name}")
        print(f"Account: {self.account_number}")
        print(f"Balance: NPR {self.balance}")
        print("-" * 30)


accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

bank_accounts = []

for acc in accounts:
    bank_accounts.append(BankAccount(*acc))

# Perform transactions
bank_accounts[1].deposit(3000)
bank_accounts[2].withdraw(15000)
bank_accounts[0].withdraw(2000)

print("\nFinal Account Balances")
for account in bank_accounts:
    account.get_balance()