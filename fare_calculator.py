# Travel Fare Calculator
FARE_RATE = 14

# Validate passenger name
while True:
    name = input("Enter passenger name: ")
    if name.strip() != "":
        break
    else:
        print("Invalid name. Name cannot be empty. Please try again.")

# Validate distance
while True:
    distance_str = input("Enter distance (km): ")
    if distance_str.isdigit():
        distance = float(distance_str)
        if distance > 0:
            break
    print("Invalid distance. Please enter a number greater than 0.")

# Validate number of passengers
while True:
    passengers_str = input("Enter number of passengers: ")
    if passengers_str.isdigit():
        passengers = int(passengers_str)
        if passengers > 0:
            break
    print("Invalid input. Please enter a positive whole number.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
