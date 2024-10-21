# # 1. Basic try-except block
# print("Demo 1: Basic try-except block")
# try:
#      x = int("not_a_number") # This will raise a ValueError
# except ValueError:
#     print("Caught a ValueError: Invalid literal for int()")
#
# print("\n")
#
#
#
# # 2. Multiple except blocks (handling different exceptions separately)
# print("Demo 2: Multiple except blocks")
# try:
#     x = int(input("Enter a number: "))
#     y = x / 0  # This will raise a ZeroDivisionError
#     print(y)
# except ValueError:
#     print("Caught a ValueError")
# except ZeroDivisionError:
#     print("Caught a ZeroDivisionError: Division by zero is not allowed")
#
# print("\n")
# #





#
# # 3. Try-except-finally block (finally block runs no matter what)
# print("Demo 3: Try-except-finally block")
# try:
#     z = 10 / 5  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     print("Caught a ZeroDivisionError: Division by zero is not allowed")
# finally:
#     print("This will always execute, regardless of whether an exception occurred")  # Always runs
#
# print("\n")




#
# # 4. Try-except-else block (else block runs if no exceptions occur)
# print("Demo 4: Try-except-else block")
# try:
#     result = 10 / 0  # No exception here
# except ZeroDivisionError:
#     print("Caught a division by zero error!")
# else:
#     print(f"Division successful, result is {result}")  # This runs because no exceptions occurred
# finally:
#     print("This will always execute, regardless of whether an exception occurred")  # Always runs
#
# print("\n")






# 5. Raising an exception using the raise statement
print("Demo 5: Raising an exception")
try:
    age = -1
    amount = -1000
    if age < 0:
        raise ValueError("Age cannot be negative")  # Raise a ValueError manually

    if amount < 0:
        raise ValueError("Amount cannot be negative")  # Raise a ValueError manually

except ValueError as e:
    print(f"Raised and caught exception: {e}")  # Handle the manually raised exception

