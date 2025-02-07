print("---DIWALI OFFERS---")
def display_menu():
    print("\n--- fashion Store ---")
    print("1. Accessories")
    print("2. Footwear")
    print( "3. jewellary")
    print("4. Checkout") 
    

def calculate_offer(category, total):
    if category == "Accessories" and total > 5000:
        return total * 0.9  # 10% off
    elif category == "Footwear" and total > 7000:
        return total * 0.85  # 15% off
    elif category == "jewellary" and total > 60000:
        return total * 1.4  # 15% off
    return total

def get_price(item, quantity):
    prices = {  'watches':2500,'sunglasses':1000,'belts':500, 'nike':8000, 'addidas':6000,'puma':4000, 'chain':50000,'ring':45000,'bracetets':74000}
    return prices.get(item.lower(), 0) * quantity

def process_category(category):
    total_price = 0
    while True:
        item = input(f"Enter item for {category} (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for {item}: "))
        total_price += get_price(item, quantity)
    return calculate_offer(category, total_price)

def main():
    total_bill = 0
    while True:
        display_menu()
        choice = input("Choose a category (1-4): ")
        if choice == '1':
            total_bill += process_category("Accessories")
        elif choice == '2':
            total_bill += process_category("Footwear")
        elif choice == '3':
            total_bill += process_category("jewellary")
        elif choice == '4':
            print(f"\nTotal Bill: {total_bill:.2f}")
            print("Thanks for shopping!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
