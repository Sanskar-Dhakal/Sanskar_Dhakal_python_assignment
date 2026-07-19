def ticket_price(seat_type, count):
    if seat_type.lower() == "regular":
        return 300 * count
    elif seat_type.lower() == "recliner":
        return 500 * count
    else:
        return "Invalid seat type"

print(ticket_price("regular", 3))    
print(ticket_price("recliner", 2))  