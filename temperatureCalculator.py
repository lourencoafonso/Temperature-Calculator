import time

# ────────────────────────────────────────────
# Class to hold ANSI color codes for printing.
# Makes error/warning messages appear colored
# in the terminal for better user experience.
# ────────────────────────────────────────────
class Colors :
    RESET = '\033[0m'     # Resets text color to default
    RED = '\033[31m'      # Red text (used for errors)
    YELLOW = '\033[33m'   # Yellow text (used for warnings)


# ────────────────────────────────────────────
# Function: printMenu
# Prints the main menu of available operations.
# Keeping this as a function avoids duplication
# since we display it multiple times in the loop.
# ────────────────────────────────────────────
def printMenu() :
    print("\nOur provided operations are: "
        "\n 1. Celsius to Fahrenheit "
        "\n 2. Fahrenheit to Celsius "
        "\n 3. Celsius to Kelvin "
        "\n 4. Kelvin to Celsius "
        "\n 5. Fahrenheit to Kelvin "
        "\n 6. Kelvin to Fahrenheit "
        "\n 7. Exit")


# ────────────────────────────────────────────
# Helper conversion functions
# These functions convert temperature between
# units and return a numeric value.
# ────────────────────────────────────────────
def celsiusToFahrenheit(temp) :
    return (temp * 9/5) + 32

def fahrenheitToCelsius(temp) :
    return (temp - 32) * 5/9


print("Welcome to the Temperature Calculator")
printMenu()

# Get initial user selection (menu option)
userOption = input("\nWhich calculation would you like to do? ").strip()

# ────────────────────────────────────────────
# MAIN PROGRAM LOOP
# Continues until user chooses option 7 (Exit)
# ────────────────────────────────────────────
while True:
    # Validate user menu option
    try :
        option = int(userOption)  # Try converting to integer
    except :
        # If conversion fails, notify user and restart input
        print(Colors.RED + "\nInvalid Input. Please enter a whole number (1-7)." + Colors.RESET)
        time.sleep(2)
        printMenu()
        userOption = input("\nWhich calculation would you like to do? ").strip()
        continue

    # Check numeric range 1–7
    if option < 1 or option > 7 :
        print(Colors.YELLOW + "\nInvalid Number. Please choose a digit between 1 and 7." + Colors.RESET)
        time.sleep(2)
        printMenu()
        userOption = input("\nWhich calculation would you like to do? ").strip()
        continue

    # If user chooses Exit (option 7)
    if option == 7 :
        print("\nThank you for using this Calculator.\n")
        break

    # ────────────────────────────────────────────
    # GET TEMPERATURE INPUT
    # Allows decimals (ex: 98.6)
    # Will reprompt until valid float
    # ────────────────────────────────────────────
    while True :
        stringTemp = input("Please input your original temperature: ").strip()
        try :
            temp = float(stringTemp)  # Allows decimal temperatures
            break
        except :
            print(Colors.RED + "\nInvalid Temperature. Please try again.\n" + Colors.RESET)
            time.sleep(1)

    # ────────────────────────────────────────────
    # Perform temperature conversion based on choice
    # ────────────────────────────────────────────
    if option == 1 :
        unit = "Fahrenheit"
        temp = celsiusToFahrenheit(temp)

    elif option == 2 :
        unit = "Celsius"
        temp = fahrenheitToCelsius(temp)

    elif option == 3 :
        unit = "Kelvin"
        temp = temp + 273.15

    elif option == 4 :
        unit = "Celsius"
        temp = temp - 273.15

    elif option == 5 :
        unit = "Kelvin"
        temp = fahrenheitToCelsius(temp) + 273.15

    else :
        unit = "Fahrenheit"
        temp = celsiusToFahrenheit(temp - 273.15)

    # Format output: remove trailing '.0' for integers
    if float(temp).is_integer():
        result = int(temp)
    else:
        result = round(temp, 4)  # rounded to 4 decimals for clean output

    print(f"Your temperature is {result} degrees {unit}")
    time.sleep(1.5)

    print("\n")
    printMenu()

    # Ask user for the next conversion
    userOption = input("\nWhich calculation would you like to do next? ").strip()
