def calculator(operator, *args):
    """Performs the chosen arithmetic operation on multiple numbers."""
    if not args:
        return"❌Error! No numbers provided."

    if operator == '+':
        return sum(args)  # Addition

    elif operator == '-':
        return args[0] - sum(args[1:])  # Subtraction

    elif operator == '*':
        product = args[0]
        for num in args[1:]:
            product *= num  # Multiplication
        return product

    elif operator == '/':
        quotient = args[0]
        for num in args[1:]:
            if num == 0:
                return"❌ Error! Division by zero."
            quotient /= num  # Division
        return quotient

    elif operator == '%':
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "❌ Error! Modulus by zero."
            result %= num  # Modulus
        return result

    elif operator == '**':
        result = args[0]
        for num in args[1:]:
            result **= num  # Exponentiation
        return result

    else:
        return "❌ Invalid operation! Use +, -, *, /, %, or **."


# ✅ Calculator Execution
while True:
    print("🧮 Calculator with Multiple Inputs")

    # Validate operator first
    operation = input("Choose from the following operations (+, -, *, /, %, **): ").strip()
    if operation not in ('+', '-', '*', '/', '%', '**'):
        print("❌Invalid operation! Please enter a valid one.")
        continue  # Restart loop

    # Get numbers from the user, handling empty input safely
    try:
        numbers = list(map(float, input("Enter as many numbers as you want separated by space 🔢: ").split()))

    except ValueError:
        print("❌Invalid input! Please enter valid numbers.")
        continue  # Restart loop

    # Perform and display the calculation
    print("✅Result:", calculator(operation, *numbers))

    # Ask user if they want to continue
    again = input("Would you like to continue using the calculator again? (y/n): ").strip().lower()
    if again != 'y':
        print("👋 Thank you for using the calculator! Have a great day! 😁")
        break  # Exit loop
