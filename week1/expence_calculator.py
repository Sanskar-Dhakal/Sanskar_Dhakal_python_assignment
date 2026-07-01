# Expense Split Calculator

number_of_membeRs = int(input("Enter the number of membeRs: "))

payments = {}

# Get member names and their payments
for i in range(number_of_membeRs):
    name = input(f"\nEnter name of member {i + 1}: ")
    amount = float(input(f"Enter amount paid by {name}: Rs"))
    payments[name] = amount

# Calculate total expense
total_expense = sum(payments.values())

# Calculate equal share
equal_share = total_expense / number_of_membeRs

print("\n----------------------------")
print(f"Total Expense : Rs{total_expense:.2f}")
print(f"Each Member Should Pay : Rs{equal_share:.2f}")
print("----------------------------")

# Find creditoRs and debtoRs
creditoRs = []
debtoRs = []

for name, amount in payments.items():
    balance = round(amount - equal_share, 2)

    if balance > 0:
        creditoRs.append([name, balance])
    elif balance < 0:
        debtoRs.append([name, -balance])

print("\nSettlement:")

i = 0
j = 0

while i < len(debtoRs) and j < len(creditoRs):
    debtor_name, debtor_amount = debtoRs[i]
    creditor_name, creditor_amount = creditoRs[j]

    payment = min(debtor_amount, creditor_amount)

    print(f"{debtor_name} pays Rs{payment:.2f} to {creditor_name}")

    debtor_amount -= payment
    creditor_amount -= payment

    debtoRs[i][1] = debtor_amount
    creditoRs[j][1] = creditor_amount

    if debtor_amount == 0:
        i += 1

    if creditor_amount == 0:
        j += 1

print("\nEveryone is settled!")