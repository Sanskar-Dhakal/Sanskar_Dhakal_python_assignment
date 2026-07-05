number = 1245
count = 3

for i in range(count):
    pin = int(input("Enter the PIN: "))

    if pin == number:
        print("PIN accepted")
        amount = float(input("Enter the amount: "))
        print("You entered:", amount)
        break
    else:
        print("Invalid PIN")

        if i == count - 1:
            print("Card blocked")