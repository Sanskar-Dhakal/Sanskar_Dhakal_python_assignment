def sort_orders(orders):
    orders.sort(key=lambda order: order[1])
    return orders

orders = [
    ("ORD101", 30),
    ("ORD102", 15),
    ("ORD103", 45),
    ("ORD104", 20)
]
sorted_orders = sort_orders(orders)
print("Sorted Orders:")
for order in sorted_orders:
    print(order)