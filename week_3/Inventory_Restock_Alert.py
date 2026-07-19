inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

restock_count = 0

print("=== Inventory Restock Report ===")

# Loop through the inventory
for product in inventory:
    if product["stock"] < product["threshold"]:
        print(f"Restock Alert: {product['item']} "
              f"(Stock: {product['stock']}, Threshold: {product['threshold']})")
        restock_count += 1

print("\nTotal items that need restocking:", restock_count)