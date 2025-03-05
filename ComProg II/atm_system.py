account = "Neil Sierra"
passkey = "0211NEIL"
balance = 29000.00

# Function for logging in
def loginAccount():
    attempts = 3 # Count of attempts in password

    while True:
        password = input("\nEnter Password: ").strip()

        if attempts == 0:
            print(f"| No attempts left! Closing the system...")
            return True # To activate the break in main loop
        elif password.upper() == passkey:
            print("| Account logged in successfully!")
            return False # To pass the break in main loop
        else:
            print(f"| Incorrect password! {attempts} attempts left!")
            attempts -= 1 # Decrements the attempts

# Function for withdrawing
def withdraw():
    global balance # Allows to edit the balance
    while True:
        try:
            amount = float(input("\nEnter Withdrawal Amount: ₱"))
            if amount <= balance: # Checks if amount is higher than balance
                balance -= amount
                print(f"| ₱{amount:.02f} has been withdrawed from your account!" +
                      f"\n| Balance has been updated to ₱{balance:.02f}" +
                      "\n| Select another action to proceed!")
                break
            else:
                print("| Insufficient amount! Please try again! ")
        except ValueError as e:
            print(f"| Invalid Input: {e}") # Prints error input

# Function to get what action the user wants
def getAction():
    print("\nSelect an action to proceed:" +
          "\n1. Balance Inquiry" +
          "\n2. Withdraw" +
          "\n3. Exit")
    
    while True:
        action = input("\nEnter Action (1-3): ").strip()

        if action == "1": # User wants to see the balance
            print(f"| Your account has a balance of ₱{balance:.02f}" +
                  "\n| Select another action to proceed!")
        elif action == "2": # User want to withdraw
            print("| Opening withdraw menu...")
            withdraw() # Run function
        elif action == "3": # User want to exit
            print("| Closing the system...")
            return True # To activate the break in main loop
        else:
            print("| Invalid action! Please try again!") # Error handling

# Main function -- Loop for the system
def atmSystem():
    while True:
        print(f"\nWelcome to Python Bank {account}!")

        if loginAccount(): break # End if the user used all attempts
        if getAction(): break # End if the user chose exit

    print("\nThank you for using Python Bank!")

atmSystem() # Run the main function