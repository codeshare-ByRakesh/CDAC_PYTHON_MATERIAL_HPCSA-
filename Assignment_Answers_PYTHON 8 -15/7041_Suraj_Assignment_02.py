# Assignment 1: Conversion Program
while True:
    inches = float(input("Enter inches: "))

    print("Convert to:")
    print("1. Feet")
    print("2. Meters")
    print("3. Centimeters")

    choice = input("Select an option (1, 2, 3): ")

    if choice == "1":
        result = inches / 12
        target_unit = "feet"
    elif choice == "2":
        result = inches * 0.0254
        target_unit = "meters"
    elif choice == "3":
        result = inches * 2.54
        target_unit = "centimeters"
    else:
        print("Invalid option.")
        continue

    print(inches, "inches =", round(result, 2), target_unit)

    if input("Convert again? (Yes/No): ").lower() == 'no':
        break

# Assignment 2: Simple Calculator
while True:
    print("Select operation:")
    print("1: Add")
    print("2: Sub")
    print("3: Mul")
    print("4: Div")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            result = num1 / num2

        print("Result:", result)  # Changed to a simpler print statement
    else:
        print("Invalid choice.")

    if input("Another calculation? (Yes/No): ").lower() == 'no':
        break

# Assignment 3: Fibonacci
a, b = 0, 1
print("Fibonacci series from 2 to 100:")
while a <= 100:
    if a >= 2:
        print(a, end=" ")
    a, b = b, a + b
