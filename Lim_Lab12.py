def display_menu():
    print("\nWelcome! Here is our menu:")
    print("1) Burger - PHP50.00")
    print("2) Pizza - PHP100.00")
    print("3) Pasta - PHP80.00")
    print("4) Fries - PHP40.00")

def get_order():
    choice = input("Select an item (1-4): ")
    if choice == "1":
        return "Burger", 50.00
    elif choice == "2":
        return "Pizza", 100.00
    elif choice == "3":
        return "Pasta", 80.00
    elif choice == "4":
        return "Fries", 40.00
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
        return None, 0.00

def process_payment(total_cost):
    while True:
        cash = input(f"The total is PHP{total_cost}. Enter payment: PHP")
        if cash.replace('.', '', 1).isdigit():
            cash = float(cash)
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment successful! Your change is PHP{change}.")
                break
            else:
                print("Insufficient payment. Please try again.")
        else:
            print("Invalid input. Please enter a valid amount.")

def main():
    print("Welcome to the Food Ordering System!")
    display_menu()
    item, price = get_order()
    if price > 0:
        print(f"You ordered: {item} - PHP{price}")
        process_payment(price)

if __name__ == "__main__":
    main()