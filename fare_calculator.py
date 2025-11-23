# --- MODULE 1: INPUT MODULE ---
def get_details():
    print("--- TRAIN FARE CALCULATOR ---")

    distance = float(input("Enter how many km you want to travel: "))

    print("Select Coach Type:")
    print("1 General (₹0.5 per km)")
    print("2 Sleeper (₹1.5 per km)")
    print("3 3AC     (₹3.0 per km)")
    print("4 2AC     (₹4.0 per km)")
    print("5 1AC     (₹5.0 per km)")

    option = input("Enter your option (1-5): ")

    return distance, option


# --- MODULE 2: FARE CALCULATION MODULE ---
def basic_fare(distance, option):
    price = 0

    if option == "1":
        price = 0.5
    elif option == "2":
        price = 1.5
    elif option == "3":
        price = 3.0
    elif option == "4":
        price = 4.0
    elif option == "5":
        price = 5.0
    else:
        print("Wrong option selected!")

    amount = distance * price
    return amount


# --- MODULE 3: OUTPUT MODULE ---
def show_total(total_fare):
    print("Your Total Fare is: ₹", total_fare)


# --- MODULE 4: DISCOUNT MODULE ---
def apply_offer(amount):
    print("Choose Discount Category:")
    print("1 Student (10% off)")
    print("2 Senior Citizen (40% off)")
    print("3 Military (20% off)")
    print("4 No Discount")

    disc = input("Enter your choice (1-4): ")

    cut = 0

    if disc == "1":
        cut = amount * 0.10
    elif disc == "2":
        cut = amount * 0.40
    elif disc == "3":
        cut = amount * 0.20
    else:
        cut = 0

    amount_after_cut = amount - cut
    return amount_after_cut


# --- MODULE 5: GST MODULE ---
def add_tax(amount):
    tax = amount * 0.05
    total_fare = amount + tax
    return total_fare


# --- MAIN PROGRAM ---
distance, option = get_details()
fare = basic_fare(distance, option)
fare_after_discount = apply_offer(fare)
total_fare = add_tax(fare_after_discount)
show_total(total_fare)