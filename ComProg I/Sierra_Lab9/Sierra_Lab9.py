row_count = int(input('Enter the number of rows: ')) # Ask user for the row count

num = 1  # Starting number
triangle_row = '' # Initial value

if row_count > 0: # Checks if user input is valid

  for row in range(1, row_count + 1): # Loop for rows

    for column in range(row): # Loop for columns

      triangle_row += str(num) + ' ' # Adds columns

      num += 1 # Adds value to next number

    print(triangle_row) # Displays a row

    triangle_row = '' # Resets the row

else: # Runs if user input is invalid

  print("Invalid number of rows. Should be greater than 0") # Display error
