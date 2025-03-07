import random

# Dictionary serves as the database
student_dict = {
    "Neil Sierra": 15900,      # Preset students
    "Lei Bulugagao": 32458     # Preset students
    }

# Generates a unique ID
def generate_id():
    while True:
        temp_id = random.randint(10000, 99999)      # Generates a random 5-digit number
        if temp_id not in student_dict.values():    # Checks if number is unique
            return temp_id

# Function for registering a student
def register_student():
    while True:
        name = input("\nEnter Student Name: ").strip().title()  # Prompt user to enter a name
        if len(name) == 0:                                      # Checks if input is empty
            print("| Invalid input! Please try again!")         # Error handling
            continue
        break
    student_dict[name] = generate_id()                          # Adds name and id to the dictionary
    print(f"| Student '{name}' with an ID of '{student_dict[name]}' has been registered to the database!")  # Feedback

# Searches for the student name
def iterate_dict(id):
    for k, v in student_dict.items():   # Iterates the keys and value of dictionary
            if id == v:                 # Finds the id
                return k

# Function for searching a student
def search_student():
    while True:
        try:
            id = int(input("\nEnter Student ID: "))     # Prompt the user to enter the id
            break
        except ValueError as e:                         # Checks if the user enters integers
            print(f"| Invalid input: {e}")              # Error handling
    if id not in student_dict.values():                 # Checks if input is in the dictionary
        print(f"| Student not found! There is no student with an ID of {id}")   # Feedback
    else:
        print(f"| Student Name: {iterate_dict(id)}")                            # Feedback

# Function for getting user action
def get_action():
    while True:
        action = input("\nEnter Your Action: ").strip()     # Prompt the user to choose an action
        if action == "1":
            print("| Action: Register a Student")           # Feedback
            register_student()                              # Call function
            return True                                     # Return true to continue the main loop
        elif action == "2":
            print("| Action: Search a Student")             # Feedback
            search_student()                                # Call function
            return True                                     # Return true to continue the main loop
        elif action == "3":
            print("| Closing the system...")                # Feedback
            return False                                    # Return false to end the main loop
        else:
            print("| Invalid input! Please try again!")     # Error handling

# Function for repetition
def use_again():
    while True:
        again = input("\nWould you like to use the system again (Yes / No): ").strip()  # Prompt the user to enter yes or no
        if again.lower() in ["y", "yes"]:                   # Checks if y or yes
            print("| Restarting the system...")             # Feedback
            return True                                     # Return true to continue the main loop
        elif again.lower() in ["n", "no"]:                  # Checks if n or no
            print("| Closing the system...")                # Feedback
            return False                                    # Return false to end the main loop
        else:
            print("| Invalid input! Please try again!")     # Error handling

# Main loop
while True:   
    print("\nHello and Welcome to Python Student Management System!" +
        "\n\nPlease select an action to proceed." +
        "\n| (1) Register a Student" +
        "\n| (2) Search a Student" +
        "\n| (3) Exit System")                  # Opening prompt
    
    if not get_action(): break                  # Checks if user want to close the system

    if not use_again(): break                   # Checks if user do not want to use the system again

print("\nThank you for using our system!")      # Closing propmt