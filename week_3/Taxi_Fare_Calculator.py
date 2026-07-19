# Taxi Fare Calculator

trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

trip_number = 1

for trip in trips:
    distance = trip["distance"]
    hour = trip["hour"]

    # Base fare
    fare = 150

    # Next 8 km (3–10 km)
    if distance > 2:
        if distance <= 10:
            fare += (distance - 2) * 35
        else:
            fare += 8 * 35
            # Beyond 10 km
            fare += (distance - 10) * 28

    # Night surcharge (10 PM – 5 AM)
    if hour >= 22 or hour < 5:
        fare = fare * 1.10

    print("Trip", trip_number)
    print("Distance:", distance, "km")
    print("Hour:", hour)
    print("Total Fare: NPR", round(fare, 2))
    print("--------------------------")

    trip_number += 1