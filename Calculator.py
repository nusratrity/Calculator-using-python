import math

def basic_operations():
    print("\nBasic Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Select an operation (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {num1 + num2}")
    elif choice == '2':
        print(f"The result is: {num1 - num2}")
    elif choice == '3':
        print(f"The result is: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid selection!")

def advanced_operations():
    print("\nAdvanced Operations:")
    print("1. Square Root")
    print("2. Power (Exponentiation)")
    print("3. Logarithm")
    print("4. Trigonometric Functions (sin, cos, tan)")

    choice = input("Select an operation (1/2/3/4): ")

    if choice == '1':
        num = float(input("Enter the number: "))
        print(f"The square root of {num} is: {math.sqrt(num)}")
    elif choice == '2':
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        print(f"The result is: {math.pow(base, exponent)}")
    elif choice == '3':
        num = float(input("Enter the number: "))
        base = float(input("Enter the base (default is 10, enter 0 for natural log): "))
        if base == 0:
            print(f"The natural log of {num} is: {math.log(num)}")
        else:
            print(f"The logarithm of {num} to base {base} is: {math.log(num, base)}")
    elif choice == '4':
        angle = float(input("Enter the angle in degrees: "))
        radians = math.radians(angle)
        print(f"sin({angle}°) = {math.sin(radians)}")
        print(f"cos({angle}°) = {math.cos(radians)}")
        print(f"tan({angle}°) = {math.tan(radians)}")
    else:
        print("Invalid selection!")

def calculator():
    print("Welcome to the Amazing Calculator!")
    while True:
        print("\nMain Menu:")
        print("1. Basic Operations")
        print("2. Advanced Operations")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            basic_operations()
        elif choice == '2':
            advanced_operations()
        elif choice == '3':
            print("Thank you for using the Amazing Calculator! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the calculator
calculator()
