# Dictionary for the Aircrafts Models
aircrafts = {
  1: [200, "Boeing 777", 1],
  2: [175, "Airbus A350 XWB", 2],
  3: [150, "Boeing 787 Dreamliner", 3],
  4: [125, "Airbus A320 Family", 4]
}
# Dictionary for the Airport Names, Location, Routes and Schedules
airports = {
  1: {
    "name": "UAE - Dubai International Airport",
    "location": "Dubai, United Arab Emirates",
    # Routes Available
    2: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 600, 169, aircrafts[1]],
      2: ["12/12/24", "12:00 PM", 600, 130, aircrafts[2]],
      3: ["12/17/24", "04:00 PM", 600, 113, aircrafts[3]],
      4: ["12/22/24", "08:00 PM", 600, 104, aircrafts[4]],
      5: ["12/27/24", "12:00 AM", 600, 174, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/02/24", "04:00 AM", 700, 173, aircrafts[1]],
      2: ["12/07/24", "08:00 AM", 700, 147, aircrafts[2]],
      3: ["12/18/24", "04:00 PM", 700, 109, aircrafts[3]],
      4: ["12/23/24", "08:00 PM", 700, 82, aircrafts[4]],
      5: ["12/28/24", "12:00 AM", 700, 175, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/03/24", "04:00 AM", 1200, 155, aircrafts[1]],
      2: ["12/08/24", "08:00 AM", 1200, 134, aircrafts[2]],
      3: ["12/13/24", "12:00 PM", 1200, 116, aircrafts[3]],
      4: ["12/24/24", "08:00 PM", 1200, 102, aircrafts[4]],
      5: ["12/29/24", "12:00 AM", 1200, 170, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/04/24", "04:00 AM", 500, 172, aircrafts[1]],
      2: ["12/09/24", "08:00 AM", 500, 152, aircrafts[2]],
      3: ["12/14/24", "12:00 PM", 500, 106, aircrafts[3]],
      4: ["12/19/24", "04:00 PM", 500, 76, aircrafts[4]],
      5: ["12/30/24", "12:00 AM", 500, 173, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/05/24", "04:00 AM", 800, 157, aircrafts[1]],
      2: ["12/10/24", "08:00 AM", 800, 137, aircrafts[2]],
      3: ["12/15/24", "12:00 PM", 800, 125, aircrafts[3]],
      4: ["12/20/24", "04:00 PM", 800, 92, aircrafts[4]],
      5: ["12/25/24", "08:00 PM", 800, 160, aircrafts[1]]
    }
  },
  2: {
    "name": "CHN - Guangzhou Baiyun International Airport",
    "location": "Guangdong Province, China",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/06/24", "08:00 AM", 600, 155, aircrafts[1]],
      2: ["12/11/24", "12:00 PM", 600, 137, aircrafts[2]],
      3: ["12/16/24", "04:00 PM", 600, 122, aircrafts[3]],
      4: ["12/21/24", "08:00 PM", 600, 79, aircrafts[4]],
      5: ["12/26/24", "12:00 AM", 600, 166, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/02/24", "04:00 AM", 650, 177, aircrafts[1]],
      2: ["12/07/24", "08:00 AM", 650, 155, aircrafts[2]],
      3: ["12/18/24", "04:00 PM", 650, 114, aircrafts[3]],
      4: ["12/23/24", "08:00 PM", 650, 81, aircrafts[4]],
      5: ["12/28/24", "12:00 AM", 650, 174, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/03/24", "04:00 AM", 1100, 173, aircrafts[1]],
      2: ["12/08/24", "08:00 AM", 1100, 148, aircrafts[2]],
      3: ["12/13/24", "12:00 PM", 1100, 112, aircrafts[3]],
      4: ["12/24/24", "08:00 PM", 1100, 91, aircrafts[4]],
      5: ["12/29/24", "12:00 AM", 1100, 177, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/04/24", "04:00 AM", 450, 169, aircrafts[1]],
      2: ["12/09/24", "08:00 AM", 450, 130, aircrafts[2]],
      3: ["12/14/24", "12:00 PM", 450, 113, aircrafts[3]],
      4: ["12/19/24", "04:00 PM", 450, 104, aircrafts[4]],
      5: ["12/30/24", "12:00 AM", 450, 174, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/05/24", "04:00 AM", 750, 176, aircrafts[1]],
      2: ["12/10/24", "08:00 AM", 750, 153, aircrafts[2]],
      3: ["12/15/24", "12:00 PM", 750, 104, aircrafts[3]],
      4: ["12/20/24", "04:00 PM", 750, 99, aircrafts[4]],
      5: ["12/25/24", "08:00 PM", 750, 160, aircrafts[1]]
    }
  },
  3: {
    "name": "GBR - London Heathrow Airport",
    "location": "London, United Kingdom",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/06/24", "08:00 AM", 700, 167, aircrafts[1]],
      2: ["12/11/24", "12:00 PM", 700, 154, aircrafts[2]],
      3: ["12/16/24", "04:00 PM", 700, 113, aircrafts[3]],
      4: ["12/21/24", "08:00 PM", 700, 102, aircrafts[4]],
      5: ["12/26/24", "12:00 AM", 700, 172, aircrafts[1]]
    },
    2: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 650, 150, aircrafts[1]],
      2: ["12/12/24", "12:00 PM", 650, 130, aircrafts[2]],
      3: ["12/17/24", "04:00 PM", 650, 122, aircrafts[3]],
      4: ["12/22/24", "08:00 PM", 650, 88, aircrafts[4]],
      5: ["12/27/24", "12:00 AM", 650, 173, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/03/24", "04:00 AM", 900, 179, aircrafts[1]],
      2: ["12/08/24", "08:00 AM", 900, 128, aircrafts[2]],
      3: ["12/13/24", "12:00 PM", 900, 100, aircrafts[3]],
      4: ["12/24/24", "08:00 PM", 900, 87, aircrafts[4]],
      5: ["12/29/24", "12:00 AM", 900, 156, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/04/24", "04:00 AM", 550, 150, aircrafts[1]],
      2: ["12/09/24", "08:00 AM", 550, 141, aircrafts[2]],
      3: ["12/14/24", "12:00 PM", 550, 124, aircrafts[3]],
      4: ["12/19/24", "04:00 PM", 550, 82, aircrafts[4]],
      5: ["12/30/24", "12:00 AM", 550, 150, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/05/24", "04:00 AM", 850, 153, aircrafts[1]],
      2: ["12/10/24", "08:00 AM", 850, 155, aircrafts[2]],
      3: ["12/15/24", "12:00 PM", 850, 112, aircrafts[3]],
      4: ["12/20/24", "04:00 PM", 850, 80, aircrafts[4]],
      5: ["12/25/24", "08:00 PM", 850, 152, aircrafts[1]]
    }
  },
  4: {
    "name": "USA - Los Angeles International Airport",
    "location": "California, USA",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/06/24", "08:00 AM", 1200, 154, aircrafts[1]],
      2: ["12/11/24", "12:00 PM", 1200, 140, aircrafts[2]],
      3: ["12/16/24", "04:00 PM", 1200, 126, aircrafts[3]],
      4: ["12/21/24", "08:00 PM", 1200, 97, aircrafts[4]],
      5: ["12/26/24", "12:00 AM", 1200, 153, aircrafts[1]]
    },
    2: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 1100, 175, aircrafts[1]],
      2: ["12/12/24", "12:00 PM", 1100, 134, aircrafts[2]],
      3: ["12/17/24", "04:00 PM", 1100, 103, aircrafts[3]],
      4: ["12/22/24", "08:00 PM", 1100, 89, aircrafts[4]],
      5: ["12/27/24", "12:00 AM", 1100, 171, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/02/24", "04:00 AM", 900, 153, aircrafts[1]],
      2: ["12/07/24", "08:00 AM", 900, 125, aircrafts[2]],
      3: ["12/18/24", "04:00 PM", 900, 101, aircrafts[3]],
      4: ["12/23/24", "08:00 PM", 900, 101, aircrafts[4]],
      5: ["12/28/24", "12:00 AM", 900, 161, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/04/24", "04:00 AM", 600, 171, aircrafts[1]],
      2: ["12/09/24", "08:00 AM", 600, 138, aircrafts[2]],
      3: ["12/14/24", "12:00 PM", 600, 128, aircrafts[3]],
      4: ["12/19/24", "04:00 PM", 600, 87, aircrafts[4]],
      5: ["12/30/24", "12:00 AM", 600, 157, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/05/24", "04:00 AM", 1100, 174, aircrafts[1]],
      2: ["12/10/24", "08:00 AM", 1100, 132, aircrafts[2]],
      3: ["12/15/24", "12:00 PM", 1100, 125, aircrafts[3]],
      4: ["12/20/24", "04:00 PM", 1100, 90, aircrafts[4]],
      5: ["12/25/24", "08:00 PM", 1100, 153, aircrafts[1]]
    }
  },
  5: {
    "name": "PHL - Ninoy Aquino International Airport",
    "location": "Manila, Philippines",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/06/24", "08:00 AM", 500, 175, aircrafts[1]],
      2: ["12/11/24", "12:00 PM", 500, 153, aircrafts[2]],
      3: ["12/16/24", "04:00 PM", 500, 116, aircrafts[3]],
      4: ["12/21/24", "08:00 PM", 500, 92, aircrafts[4]],
      5: ["12/26/24", "12:00 AM", 500, 153, aircrafts[1]]
    },
    2: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 450, 154, aircrafts[1]],
      2: ["12/12/24", "12:00 PM", 450, 154, aircrafts[2]],
      3: ["12/17/24", "04:00 PM", 450, 125, aircrafts[3]],
      4: ["12/22/24", "08:00 PM", 450, 78, aircrafts[4]],
      5: ["12/27/24", "12:00 AM", 450, 156, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/02/24", "04:00 AM", 550, 166, aircrafts[1]],
      2: ["12/07/24", "08:00 AM", 550, 134, aircrafts[2]],
      3: ["12/18/24", "04:00 PM", 550, 112, aircrafts[3]],
      4: ["12/23/24", "08:00 PM", 550, 86, aircrafts[4]],
      5: ["12/28/24", "12:00 AM", 550, 174, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/03/24", "04:00 AM", 600, 175, aircrafts[1]],
      2: ["12/08/24", "08:00 AM", 600, 144, aircrafts[2]],
      3: ["12/13/24", "12:00 PM", 600, 101, aircrafts[3]],
      4: ["12/24/24", "08:00 PM", 600, 95, aircrafts[4]],
      5: ["12/29/24", "12:00 AM", 600, 164, aircrafts[1]]
    },
    6: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/05/24", "04:00 AM", 700, 154, aircrafts[1]],
      2: ["12/10/24", "08:00 AM", 700, 146, aircrafts[2]],
      3: ["12/15/24", "12:00 PM", 700, 101, aircrafts[3]],
      4: ["12/20/24", "04:00 PM", 700, 76, aircrafts[4]],
      5: ["12/25/24", "08:00 PM", 700, 166, aircrafts[1]]
    }
  },
  6: {
    "name": "JPN - Tokyo Haneda Airport",
    "location": "Tokyo, Japan",
    # Routes Available
    1: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/06/24", "08:00 AM", 800, 155, aircrafts[1]],
      2: ["12/11/24", "12:00 PM", 800, 131, aircrafts[2]],
      3: ["12/16/24", "04:00 PM", 800, 126, aircrafts[3]],
      4: ["12/21/24", "08:00 PM", 800, 88, aircrafts[4]],
      5: ["12/26/24", "12:00 AM", 800, 180, aircrafts[1]]
    },
    2: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/01/24", "04:00 AM", 750, 166, aircrafts[1]],
      2: ["12/12/24", "12:00 PM", 750, 139, aircrafts[2]],
      3: ["12/17/24", "04:00 PM", 750, 127, aircrafts[3]],
      4: ["12/22/24", "08:00 PM", 750, 101, aircrafts[4]],
      5: ["12/27/24", "12:00 AM", 750, 156, aircrafts[1]]
    },
    3: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/02/24", "04:00 AM", 850, 152, aircrafts[1]],
      2: ["12/07/24", "08:00 AM", 850, 145, aircrafts[2]],
      3: ["12/18/24", "04:00 PM", 850, 125, aircrafts[3]],
      4: ["12/23/24", "08:00 PM", 850, 76, aircrafts[4]],
      5: ["12/28/24", "12:00 AM", 850, 172, aircrafts[1]]
    },
    4: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/03/24", "04:00 AM", 1000, 160, aircrafts[1]],
      2: ["12/08/24", "08:00 AM", 1000, 148, aircrafts[2]],
      3: ["12/13/24", "12:00 PM", 1000, 118, aircrafts[3]],
      4: ["12/24/24", "08:00 PM", 1000, 104, aircrafts[4]],
      5: ["12/29/24", "12:00 AM", 1000, 150, aircrafts[1]]
    },
    5: {
      #   Date        Take-off    $$   PAX  Aircraft
      1: ["12/04/24", "04:00 AM", 700, 176, aircrafts[1]],
      2: ["12/09/24", "08:00 AM", 700, 151, aircrafts[2]],
      3: ["12/14/24", "12:00 PM", 700, 129, aircrafts[3]],
      4: ["12/19/24", "04:00 PM", 700, 86, aircrafts[4]],
      5: ["12/30/24", "12:00 AM", 700, 153, aircrafts[1]]
    }
  }
}
# Dictionary for the Ticket Classes
ticketClasses = {
  1: [1, "Economy Class"],
  2: [1.2, "Business Class"],
  3: [1.5, "First Class"]
}
# Function to get Origin and Destination
def getRoute():
  global origin, destination
  print("\nHello and Welcome to Python Airlines!")
  print("\nAirports List:")
  for n in range(len(airports)):
    n += 1
    print(f"{n}. {airports[n]["name"]}")
  print("Enter 'X' to restart the system.")
  while True:
    org = input("\nChoose an Origin: ")
    if org.isdigit() and 1 <= int(org) <= len(airports):
      origin = int(org)
      print(f"Chosen {airports[origin]["name"]} as the origin airport.")
      break
    elif org.lower() == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")
  while True:
    dtn = input("\nChoose an Destination: ")
    if dtn == org:
      print("Invalid input! Cannot choose origin as destination.")
    elif dtn.isdigit() and 1 <= int(dtn) <= len(airports):
      destination = int(dtn)
      print(f"Chosen {airports[destination]["name"]} as the origin airport.")
      break
    elif dtn.lower() == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")
# Function to format and get the Seats Availability
def calcSeats(x, y):
  if x == y:
    return "FULL"
  return f"{x:03d}/{y:03d}"
# Function to get the Flight and FlightNum
def getFlight():
  global flight, flightNum
  print("\nFlight Schedule:")
  print(f"+{"-"*11}+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*9}+{"-"*23}+")
  print(f"| {"Flt #":^9} | {"Date":^8} | Take-off | {"Cost":^8} | {"Seats":^7} | {"Aircraft":^21} |")
  print(f"+{"-"*11}+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*9}+{"-"*23}+")
  for n in range(len(airports[origin][destination])):
    n += 1
    x = airports[origin][destination][n]
    y = f"{x[2]:.2f}"
    print(f"| Flight #{n} | {x[0]} | {x[1]} | ${y:^7} | {calcSeats(x[3], x[4][0]):^7} | {x[4][1]:^21} |")
  print(f"+{"-"*11}+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*9}+{"-"*23}+")
  print("Enter 'X' to restart the system.")
  while True:
    flt = input("\nChoose a Flight Schedule: ")
    if flt.isdigit() and 1 <= int(flt) <= len(airports[origin][destination][n]):
      flightNum = int(flt)
      flight = airports[origin][destination][int(flt)]
      print(f"Chosen flight schedule #{int(flt)}.")
      break
    elif flt.lower() == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")
# Function to get the Ticket Amount, Class and Cost
def getTicket():
  global ticketAmount, ticketClass, totalCost
  seatsLeft = flight[4][0] - flight[3]
  while True:
    tktAmt = input(f"\nEnter Ticket Amount ({seatsLeft} left): ")
    if tktAmt.isdigit() and 1 <= int(tktAmt) <= seatsLeft:
      ticketAmount = int(tktAmt)
      break
    elif tktAmt.lower() == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid amount! Please try again.")
  print("\nChoose ticket class:")
  print(f"+---+{"-"*27}+{"-"*18}+{"-"*27}+")
  print(f"| # | {"Aircraft":^25} | {"Multiplier":^16} | {"Total Cost":^25} |")
  print(f"+---+{"-"*27}+{"-"*18}+{"-"*27}+")
  for n in range(len(ticketClasses)):
    n += 1
    total = f"${ticketAmount * ticketClasses[n][0] * flight[2]:.2f}"
    print(f"| {n} | {ticketClasses[n][1]:^25} | {str(ticketClasses[n][0]) + " x":^16} | {total:^25} |")
  print(f"+---+{"-"*27}+{"-"*18}+{"-"*27}+")
  print("Enter 'X' to restart the system.")
  while True:
    tktCls = input("\nChoose a Ticket Class: ")
    if tktCls.isdigit() and 1 <= int(tktCls) <= len(ticketClasses):
      ticketClass = ticketClasses[int(tktCls)]
      totalCost = ticketAmount * ticketClass[0] * flight[2]
      print(f"Chosen {ticketClass[1]} as ticket class.")
      print(f"Total cost of the tickets is ${totalCost:.2f}")
      break
    elif tktCls.lower() == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")
# Function to get the Payment
def getPayment():
  while True:
    payment = input("\nEnter payment amount: $")
    if payment.replace(".", "", 1).isdigit() and float(payment) >= totalCost:
      print(f"Payment accepted! Change is ${float(payment) - totalCost:.2f}")
      break
    elif payment == "x":
      print("Restarting...\n\n\n\n\n")
      return True
    else:
      print("Invalid input! Please try again.")
# Function for printing and formating the Ticket IDs
def printTicketIDs():
  print("\nPrinting ticket IDs...\n")
  for n in range(ticketAmount):
    seatNum = flight[3] + n + 1
    date = f"M{flight[0][0:2]}D{flight[0][3:5]}Y{flight[0][6:8]}"
    ticketID = f"PAL-OR{origin:02d}-DT{destination:02d}-{date}-FLT{flightNum:03d}-MDL{flight[4][2]:02d}-P{seatNum:03d}"
    print(f"{ticketID:^80}")
  flight[3] += ticketAmount
  print("\nAdditional Information:")
  print("Seat number can be found for the last four digits of the ticket ID.")
# Function to Restart the System
def restartSystem():
  while True:
    restart = input("\nWould you like to order again? (Yes/No): ")
    if restart.lower() == "yes":
      print("Running the system again...\n\n\n\n\n")
      return True
    elif restart.lower() == "no":
      print("Closing the system...")
      print("Thank you for using Python Airlines!\n")
      return False
    else:
      print("Invalid input! Please try again.")
# Main Loop of the system
while True:
  # Runs the functions and if true is returned then the system restarts
  if getRoute(): continue 
  if getFlight(): continue
  if getTicket(): continue
  if getPayment(): continue
  printTicketIDs()
  if restartSystem(): continue 
  break # Break for the system end