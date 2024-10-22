#   Assignment 1: Temperature Converter

def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def celsius_to_kelvin(c): return c + 273.15

def temperature_converter():
    try:
        temp_value = float(input("Enter temperature value: "))
        temp_unit = input("Current unit (C, F, K): ").strip().upper()
        target_unit = input("Convert to (C, F, K): ").strip().upper()

        if temp_unit == 'C':
            if target_unit == 'F': result = celsius_to_fahrenheit(temp_value)
            elif target_unit == 'K': result = celsius_to_kelvin(temp_value)
            else: result = temp_value
        elif temp_unit == 'F':
            if target_unit == 'C': result = fahrenheit_to_celsius(temp_value)
            elif target_unit == 'K': result = celsius_to_kelvin(fahrenheit_to_celsius(temp_value))
            else: result = temp_value
        elif temp_unit == 'K':
            if target_unit == 'C': result = temp_value - 273.15
            elif target_unit == 'F': result = celsius_to_fahrenheit(temp_value - 273.15)
            else: result = temp_value
        else:
            print("Invalid unit.")
            return

        print(f"Converted: {result:.2f} {target_unit}")

    except ValueError:
        print("Enter a numeric value.")
    else:
        print("Conversion successful.")
    finally:
        print("Thank you!")

temperature_converter()


#  Assignment 2: Handle File Not Found Exception

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    else:
        print("File read successfully.")
    finally:
        print("End of operation.")

    read_file('non_existent_file.txt')
