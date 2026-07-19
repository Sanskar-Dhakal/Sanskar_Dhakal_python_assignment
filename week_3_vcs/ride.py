BASE_RATES = {
    "bike": 5,
    "auto": 8,
    "car": 12,
    "premium": 20,
}

def estimate_fare(distance_km, vehicle_type, surge=1.0):
    base_rate = BASE_RATES.get(vehicle_type)
    if base_rate is None:
        return f"Invalid vehicle type: {vehicle_type}"

    fare = base_rate * distance_km * surge
    return round(fare, 2)  
print(estimate_fare(10, "bike"))
print(estimate_fare(10, "auto"))
print(estimate_fare(10, "car"))
print(estimate_fare(10, "premium"))  
print(estimate_fare(10, "bike", 2))   
print(estimate_fare(10, "auto", 2))    
print(estimate_fare(10, "car", 2))     
print(estimate_fare(10, "premium", 2))   