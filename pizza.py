#name: CARDINALE
#program purpose: to calculate a rercipt for a pizza purchase



import datetime

## Global values
PIZZA_SIZES = {'S': 9.99, 'M': 12.99, 'L': 14.99, 'X': 17.99}
SALES_TAX_RATE = 0.055

## Define main function
def main():
    while True:
        size, quantity = get_order()
        pizza_cost, sales_tax, total = calculate_cost(size, quantity)
        print_receipt(size, quantity, pizza_cost, sales_tax, total)
        if not order_again():
            break

# Function to get pizza order from user
def get_order():
    while True:
        size = input("Enter pizza size (S/M/L/X): ").upper()
        if size in PIZZA_SIZES:
            break
        print("Invalid input.")
    quantity = int(input("Enter quantity: "))
    return size, quantity

# Function to calculate pizza cost, sales tax, and total
def calculate_cost(size, quantity):
    pizza_cost = quantity * PIZZA_SIZES[size]
    sales_tax = pizza_cost * SALES_TAX_RATE
    total = pizza_cost + sales_tax
    return pizza_cost, sales_tax, total

# Function to print receipt
def print_receipt(size, quantity, pizza_cost, sales_tax, total):
    print("\nPalermo Pizza")
    print(datetime.datetime.now())
    print(f"Number of pizzas ordered: {quantity}")
    print(f"Pizza cost:      ${pizza_cost:>6.2f}")
    print(f"Sales tax:       ${sales_tax:>6.2f}")
    print(f"Total:           ${total:>6.2f}")

# Function to ask user if they want to order another pizza
def order_again():
    while True:
        another_order = input("Do you want to order another pizza (Y/N)? ").upper()
        if another_order == 'Y':
            return True
        elif another_order == 'N':
            return False
        print("Invalid input.")

## Run main function
main()
