print("Hello welcome to Python Restaurant!" +
      "\nTo select a food please enter its respective number to the 'Input Order Number'" +
      "\n\nFood Menu:")

menu_items = ["Classic Cheeseburger", "Bacon Burger", "Veggie Burger", "Margherita Pizza", "Pepperoni Pizza", "Grilled Chicken Sandwich", "Turkey Club Sandwich", "Veggie Wrap", "Fries (Small)", "Fries (Large)", "Onion Rings", "Soft Drink", "Iced Tea", "Coffee", "Milkshake", "Chicken Tenders", "Fish and Chips", "Caesar Salad", "Mozzarella Sticks", "Garlic Bread"]
prices = [5.99, 6.99, 5.49, 8.99, 9.99, 6.49, 6.99, 5.99, 2.49, 3.49, 3.99, 1.99, 2.49, 1.49, 3.99, 7.49, 8.49, 5.99, 4.99, 2.99]
index = 0

for n in range(len(menu_items)):
  print(f"{str(n + 1) + ".":<4} {menu_items[n]:<30} - ${prices[n]}")

def getOrder():
    while True:
        orderNumber = input("\nInput Order Number: ")
        if orderNumber.isdigit() and 1 <= int(orderNumber) <= len(menu_items):
           index = int(orderNumber)
           return index
        else:
           print("Invalid input! Please choose on the menu!")

def getPayment():
   print(f"\nYou ordered {menu_items[index]} for ${prices[index]}.")
   while True:
        payment = input("\nEnter your payment: $")
        if payment.replace(".", "", 1).isdigit() and float(payment) >= prices[index]:
            change = float(payment) - prices[index]
            print(f"Payment accepted! Change is ${change:.2f}" +
                  "\nEnjoy your order!")
            break
        else:
           print("Invalid amount! Payment shoud be greater or equal to the price!")

getOrder()
getPayment()