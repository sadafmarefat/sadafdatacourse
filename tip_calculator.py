# Define tax rates
QST_RATE = 0.09975 # Quebec sales tax
GST_RATE = 0.05 # Federal sales tax

# Function to get user input for number of diners
def get_num_diners():
    while True:
        try:
            num_diners = int(input("How many people are in your group? "))
            if num_diners > 0:
                return num_diners
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to get user input for meal price before tax
def get_meal_price():
    while True:
        try:
            meal_price = float(input("What is the total price of the meal before tax? $"))
            if meal_price >= 0:
                return meal_price
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to get user input for tip percentage
def get_tip_percent():
    while True:
        tip_choice = input("How was the service?\n1) Exceptional (20% tip)\n2) Good (15% tip)\n3) Basic (10% tip)\n4) Horrible (0% tip)\nPlease choose a number (1-4): ")
        if tip_choice == "1":
            return 0.2
        elif tip_choice == "2":
            return 0.15
        elif tip_choice == "3":
            return 0.1
        elif tip_choice == "4":
            return 0
        else:
            print("Please choose a number from 1 to 4.")

# Calculate tax amount
def calculate_tax(meal_price):
    qst_amount = meal_price * QST_RATE
    gst_amount = meal_price * GST_RATE
    return qst_amount, gst_amount

# Calculate total cost
def calculate_total(meal_price, qst_amount, gst_amount):
    total = meal_price + qst_amount + gst_amount
    return total

# Calculate tip amount
def calculate_tip(meal_price, tip_percent):
    tip_amount = meal_price * tip_percent
    return tip_amount

# Main function
def main():
    print("Welcome to the tip calculator program!\n")
    num_diners = get_num_diners()
    meal_price = get_meal_price()
    tip_percent = get_tip_percent()

    qst_amount, gst_amount = calculate_tax(meal_price)
    total = calculate_total(meal_price, qst_amount, gst_amount)
    tip_amount = calculate_tip(meal_price, tip_percent)
    grand_total = total + tip_amount
    owed_per_person = grand_total / num_diners

    print(f"\nNumber of diners: {num_diners}")
    print(f"Meal price before tax: ${meal_price:.2f}")
    print(f"Quebec tax (QST) added: ${qst_amount:.2f}")
    print(f"Federal tax (GST) added: ${gst_amount:.2f}")
    print(f"Total including tax: ${total:.2f}")
    print(f"Tip amount (based on meal price before tax): ${tip_amount:.2f}")
    print(f"Grand total including tax and tip: ${grand_total:.2f}")
    print(f"Amount owed per person: ${owed_per_person:.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
    
