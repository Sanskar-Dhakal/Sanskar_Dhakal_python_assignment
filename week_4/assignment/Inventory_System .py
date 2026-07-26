# Given data
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}


def process_order(inventory, cart):
    grand_total = 0
    purchased_items = []

    # Process each item in the cart
    for item, quantity in cart.items():
        if item in inventory:
            if inventory[item]["stock"] >= quantity:
                item_total = inventory[item]["price"] * quantity
                grand_total += item_total

                # Update stock
                inventory[item]["stock"] -= quantity

                purchased_items.append((item, quantity, item_total))
            else:
                print(f"Sorry, not enough stock for {item}")
        else:
            print(f"{item} is not available in inventory")

    # Print Bill
    print("---- Bill ----")
    for item, quantity, total in purchased_items:
        print(f"{item} x{quantity} = NPR {total}")

    print(f"Grand Total: NPR {grand_total}")
    print("--------------")

    # Print Updated Inventory
    print("Updated stock:")
    for item in inventory:
        print(f"{item} = {inventory[item]['stock']}")


# Call the function
process_order(inventory, cart)