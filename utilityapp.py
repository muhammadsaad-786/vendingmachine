def main():  
   # Define a dictionary to store menu items, categorized by type  
   menu_items = {  
      "Drinks": {  
        "1": {"name": "Kinza-Cola", "price": 2.75, "code": "KC", "stock": 10},  
        "2": {"name": "Pepsi", "price": 3.00, "code": "PE", "stock": 10},  
        "3": {"name": "Water Bottle", "price": 2.00, "code": "WB", "stock": 10},  
        "4": {"name": "Iced Tea", "price": 5.25, "code": "IT", "stock": 10},  
        "5": {"name": "Fresh Lemonade", "price": 8.50, "code": "FL", "stock": 10},  
      },  
      "Snacks": {  
        "1": {"name": "Dairy Milk", "price": 4.75, "code": "DM", "stock": 10},  
        "2": {"name": "Lays Chips", "price": 2.50, "code": "LC", "stock": 10},  
        "3": {"name": "Chocolate-Chip Cookies", "price": 5.50, "code": "CCC", "stock": 10},  
        "4": {"name": "Popcorn", "price": 6.75, "code": "PC", "stock": 10},  
        "5": {"name": "Candy", "price": 3.75, "code": "CD", "stock": 10},  
      },  
      "Hot Drinks": {  
        "1": {"name": "Black Coffee", "price": 14.00, "code": "BC", "stock": 10},  
        "2": {"name": "Karak Tea", "price": 4.00, "code": "TE", "stock": 10},  
        "3": {"name": "Hot Chocolate", "price": 16.00, "code": "HC", "stock": 10},  
        "4": {"name": "Cappuccino", "price": 15.00, "code": "CP", "stock": 10},  
        "5": {"name": "Latte", "price": 15.50, "code": "LT", "stock": 10},  
      },  
      "Food": {  
        "1": {"name": "Burger", "price": 8.00, "code": "BG", "stock": 10},  
        "2": {"name": "Salad", "price": 12.50, "code": "SL", "stock": 10},  
        "3": {"name": "Pizza", "price": 25.00, "code": "PZ", "stock": 10},  
        "4": {"name": "Fries", "price": 5.50, "code": "FR", "stock": 10},  
        "5": {"name": "Chicken Nuggets", "price": 10.50, "code": "CN", "stock": 10},  
      },  
      "Sandwiches": {  
        "1": {"name": "Grilled Chicken Sandwich", "price": 13.50, "code": "GCS", "stock": 10},  
        "2": {"name": "BLT Sandwich", "price": 10.50, "code": "BLT", "stock": 10},  
        "3": {"name": "Chicken Tikka Wrap", "price": 7.50, "code": "CTW", "stock": 10},  
        "4": {"name": "Turkey Sandwich", "price": 17.50, "code": "TS", "stock": 10},  
        "5": {"name": "Veggie Sandwich", "price": 6.50, "code": "VS", "stock": 10},  
      },  
   }  
  
   # Print the welcome message  
   print("\n************************************")  
   print("*       WELCOME TO THE      *")  
   print("*      VENDING MACHINE      *")  
   print("************************************")  
   print()  
  
   # Print the available categories to the user  
   print("-------------------------------")  
   print("      CATEGORIES       ")  
   print("-------------------------------")  
   for category in menu_items.keys():  
      print(f"* {category}")  
   print("-------------------------------")  
   print()  
  
   # Initialize the user's balance to $0.00  
   balance = 0.0  
  
   # Initialize the user's purchase history  
   purchase_history = []  
  
   # Main Loop to prompt the user for input until they choose to quit  
   while True:  
      # Prompt the user to select a category or deposit money  
      user_input = input("\n-------------------------------\n"  
                  "      SELECT AN OPTION    \n"  
                  "-------------------------------\n"  
                  "1. Select a category\n"  
                  "2. Deposit money\n"  
                  "3. View purchase history\n"  
                  "4. Quit\n"  
                  "-------------------------------\n"  
                  "Enter your choice: ")  
  
      # If the user chooses to quit, print a goodbye message and exit the program  
      if user_input == "4":  
        print("\n************************************")  
        print("*      THANK YOU FOR USING    *")  
        print("*      THE VENDING MACHINE    *")  
        print("************************************")  
        break  
  
      # If the user chooses to deposit money, ask  them to enter the amount  
      elif user_input == "2":  
        try:  
           # Attempt to convert the user's input to a float  
           deposit_amount = float(input("Enter the amount to deposit: $"))  
  
           # Check if the deposit amount is negative  
           if deposit_amount < 0:  
              print("Invalid deposit amount. Please enter a positive number.")  
           else:  
              # Add the deposit amount to the user's balance  
              balance += deposit_amount  
              print(f"\nYour new balance is: ${balance:.2f}")  
        except ValueError:  
           # If the user's input can't be converted to a float, print an error message  
           print("Invalid input. Please enter a valid number.")  
  
      # If the user selects to view their purchase history, print the list of previous purchases  
      elif user_input == "3":  
        if len(purchase_history) == 0:  
           print("\nYou have not made any purchases yet :/")  
        else:  
           print("\n-------------------------------")  
           print("      PURCHASE HISTORY    ")  
           print("-------------------------------")  
           total_amount = 0.0  
           for i, purchase in enumerate(purchase_history):  
              print(f"{i+1}. {purchase['name']} - ${purchase['price']}")  
              total_amount += purchase['price']  
           print(f"\nTotal Amount: ${total_amount:.2f}")  
           print("-------------------------------")  
  
      # If the user selects a category, print the menu items in that category  
      elif user_input == "1":  
        print("\n-------------------------------")  
        print("      SELECT A CATEGORY    ")  
        print("-------------------------------")  
        for i, category in enumerate(menu_items.keys()):  
           print(f"{i+1}. {category}")  
        print("-------------------------------")  
        category_input = input("Enter the number of your chosen category: ")  
        if category_input.isdigit() and 1 <= int(category_input) <= len(menu_items):  
           selected_category = list(menu_items.keys())[int(category_input) - 1]  
           print(f"\n-------------------------------")  
           print(f"      {selected_category.upper()} MENU    ")  
           print("-------------------------------")  
           for key, value in menu_items[selected_category].items():  
              print(f"{key}. {value['name']} - ${value['price']}")  
           print("-------------------------------")  
  
           # Prompt the user to select an item from the category  
           while True:  
              item_input = input("\n-------------------------------\n"  
                          "      SELECT AN ITEM    \n"  
                          "-------------------------------\n"  
                          "Enter the number of your chosen item, or 'b' to go back: ")  
  
              # If the user chooses to go back, break out of the inner loop  
              if item_input.lower() == 'b':  
                break  
  
              # If the user selects an item, check if they have sufficient funds  
              elif item_input in menu_items[selected_category].keys():  
                selected_item = menu_items[selected_category][item_input]  
                if balance >= selected_item['price']:  
                   # If the user has sufficient funds, check if the item is in stock  
                   if selected_item['stock'] > 0:  
                      # Subtract the item's price from the user's balance  
                      balance -= selected_item['price']  
                      # Decrement the item's stock level  
                      selected_item['stock'] -= 1  
                      # Print a message to confirm the purchase  
                      print(f"\nYou have purchased {selected_item['name']}. Your new balance is: ${balance:.2f}")  
                      # Print a message to confirm the item has been dispensed  
                      print(f"{selected_item['name']} has been dispensed. Please collect your item from the dispenser.")  
                      # Print the remaining stock level  
                      print(f"Remaining stock: {selected_item['stock']}")  
                      # Add the purchased item to the user's purchase history  
                      purchase_history.append(selected_item)  
  
                      # If the user's balance is greater than $0.00, prompt them to receive their change  
                      if balance > 0:  
                        print("\n-------------------------------")  
                        print("      RECEIVE CHANGE    ")  
                        print("-------------------------------")  
                        print("Would you like to receive your change? (y/n)")  
                        change_input = input().lower()  
                        if change_input == 'y':  
                           # If the user chooses to receive their change, print the amount and reset their balance to $0.00  
                           print(f"\nHere is your change: ${balance:.2f}")  
                           balance = 0.0  
                   else:  
                      # If the item is out of stock, print an error message  
                      print("\n-------------------------------")  
                      print("      OUT OF STOCK      ")  
                      print("-------------------------------")  
                      print("Sorry, this item is out of stock.")  
                else:  
                   # If the user does not have sufficient funds, print an error message  
                   print("\n-------------------------------")  
                   print("      INSUFFICIENT FUNDS   ")  
                   print("-------------------------------")  
                   print("Insufficient funds. Please deposit more money.")  
              else:  
                # If the user's input is invalid, print an error message  
                print("\n-------------------------------")  
                print("      INVALID INPUT      ")  
                print("-------------------------------")  
                print("Invalid input. Please try again.")  
        else:  
           print("\n-------------------------------")  
           print("      INVALID CATEGORY    ")  
           print("-------------------------------")  
           print("Invalid category. Please try again.")  
  
      else:  
        # If the user's input is invalid, print an error message  
        print("\n-------------------------------")  
        print("      INVALID INPUT      ")  
        print("-------------------------------")  
        print("Invalid input. Please try again.")  
  
if __name__ == "__main__":  
   main()
