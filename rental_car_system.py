#Rental car system

print("Rental car system")

# List of cars
cars = {
    "C101": {"name": "Maruti Suzuki Swift", "status": "Available", "price": 800},
    "C102": {"name": "Hyundai Aura",  "status": "Available", "price": 900},
    "C103": {"name": "Honda City",   "status": "Available", "price": 1200},
    "C104": {"name": "Maruti Suzuki Ertiga","status": "Available", "price": 1500}
}

# car details
rented = {}  


# function for available cars
def show_cars():
    print("\n Available Cars")
    for code, car in cars.items():
        if car["status"] == "Available":
            print(f"{code} - {car['name']} (₹{car['price']} per day)")



# function for renting car
def rent_car():
    show_cars()
    print("Rent car")
    car_code = input("Car code:").upper()

    if car_code not in cars:
        print("Error")
       return

    if cars[car_code]["status"] == "Rented":
        print("Sorry:( This car is already rented")
        return

    name = input("Customer name: ")
    days = int(input("Number of days to rent for: "))

    # Calculate bill
    rate = cars[car_code]["price"]
    bill = rate * days

    rented[car_code] = {"customer": name, "days": days, "bill": bill}
    cars[car_code]["status"] = "Rented"

    print(f"\nCar {car_code} successfully rented :)")
    print(f"Customer: {name}")
    print(f"Total Rental Cost: ₹{bill}")



# function to return car

def return_car():
    print("\n Return car")
    car_code = input("Enter car code: ").upper()

    if car_code not in rented:
        print("Error")
        return

    info = rented[car_code]

    print("\n Summary")
    print(f"Customer: {info['customer']}")
    print(f"Days Rented: {info['days']}")
print(f"Total Bill: ₹{info['bill']}")

    # Mark car as available again
    cars[car_code]["status"] = "Available"
    del rented[car_code]

    print("\nCar has been returned successfully:)")



# function to show all rented cars

def show_rented():
    print("\n Rented cars")
    if not rented:
        print("Error")
        return

    for code, info in rented.items():
        print(f"{code} - {info['customer']} (₹{info['bill']})")



# Main Menu

while True:
    print(" Main menu")
    print("1. Show Available Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Show Rented Cars")
    print("5. Exit")

    choice = input("your choice: ")

    if choice == "1":
        show_cars()
        elif choice == "2":
        rent_car()
    elif choice == "3":
        return_car()
    elif choice == "4":
        show_rented()
    elif choice == "5":
        print("Thank you for using the Car Rental System!")
        break
    else:
        print("Error")
