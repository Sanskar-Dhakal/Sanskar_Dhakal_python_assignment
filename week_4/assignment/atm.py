accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500, "pin": "5678"},
    "A003": {"name": "Bikash Rai", "balance": 22000, "pin": "9012"}
}


def atm(account_id, pin, action, amount=0):
    # Check if account exists
    if account_id not in accounts:
        print("Account not found")
        return

    account = accounts[account_id]

    # Check PIN
    if account["pin"] != pin:
        print("Incorrect PIN")
        return

    # Balance inquiry
    if action == "balance":
        print(f"Account Holder: {account['name']}")
        print(f"Balance: NPR {account['balance']}")

    # Deposit
    elif action == "deposit":
        account["balance"] += amount
        print(f"Deposit successful.")
        print(f"New Balance: NPR {account['balance']}")

    # Withdraw
    elif action == "withdraw":
        if account["balance"] >= amount:
            account["balance"] -= amount
            print(f"Withdrawal successful.")
            print(f"Remaining Balance: NPR {account['balance']}")
        else:
            print("Insufficient funds")


    else:
        print("Invalid action")


# Test cases
atm("A001", "1234", "balance")
print()

atm("A002", "0000", "withdraw", 2000)   # Wrong PIN
print()

atm("A002", "5678", "deposit", 3000)
print()

atm("A003", "9012", "withdraw", 25000)  # Insufficient funds
print()

atm("A004", "1111", "balance")          # Account not found