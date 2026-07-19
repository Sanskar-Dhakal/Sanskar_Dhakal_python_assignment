# Taking inputs
purchase = float(input("Enter the total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ").lower()

# Determine purchase discount
if purchase < 1000:
    discount = 0
elif purchase < 5000:
    discount = 5
elif purchase < 15000:
    discount = 10
else:
    discount = 20

# Apply purchase discount
discounted_amount = purchase - (purchase * discount / 100)

# Apply extra loyalty discount
if member == "yes":
    discounted_amount = discounted_amount - (discounted_amount * 5 / 100)

# Display results
print("Original Purchase Amount: NPR", purchase)
print("Purchase Discount:", discount, "%")

if member == "yes":
    print("Loyalty Member Discount: 5%")
else:
    print("Loyalty Member Discount: 0%")

print("Final Payable Amount: NPR", round(discounted_amount, 2))