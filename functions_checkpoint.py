# Simple Calculator App

def calculator(num1, num2):
    # Prompt the user for an operator
    operator = input("Enter the operator (+, -, *, /): ")

    # Perform the calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Invalid operator. Please use +, -, *, or /."

    return result


# Main program loop
while True:
    print("\nWelcome to the Simple Calculator!")
    
    # Get user input and convert to float
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        continue

    # Call the calculator function
    output = calculator(num1, num2)
    print("The result is:", output)

    # Ask user if they want to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break
