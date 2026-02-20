def welcome_message():
    print("\n************* Welcome to the SoftwareBox SuperStore ***************\n")

def get_quantity():
    while True:
        quantity = input("Please enter a quantity (whole number only) of software package(s) to order: ")
        if quantity.isdigit():
            return int(quantity)
        print("Invalid input. Please enter a whole number for quantity only.")

def calculate_discount_rate(quantity):
    if quantity < 10:
        return 0.0
    elif quantity < 20:
        return 0.10
    elif quantity < 50:
        return 0.20
    elif quantity < 100:
        return 0.30
    else:
        return 0.40

def print_discount_message(quantity, discount_rate):
    if discount_rate == 0.0:
        print("**You are ordering less than 10 units. Sorry, no discount applied.")
    else:
        print(f"**You are ordering {quantity} units. Congratulations, you get a {int(discount_rate * 100)}% discount!")

def calculate_total_price(quantity, unit_price, discount_rate):
    return unit_price * quantity * (1 - discount_rate)

def display_summary(quantity, unit_price, total_price):
    print(f"\n**You are ordering quantity: {quantity}")
    print(f"**The retail price for the software package is: ${unit_price}")
    print(f"**Your total price is: ${total_price:,.2f}")

def main():
    unit_price = 99
    welcome_message()
    quantity = get_quantity()
    discount_rate = calculate_discount_rate(quantity)
    print_discount_message(quantity, discount_rate)
    total_price = calculate_total_price(quantity, unit_price, discount_rate)
    display_summary(quantity, unit_price, total_price)

if __name__ == "__main__":
    main()
