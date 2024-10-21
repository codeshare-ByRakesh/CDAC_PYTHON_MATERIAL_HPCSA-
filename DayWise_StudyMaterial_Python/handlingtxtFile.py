
# Demonstrates text file handling: creating, writing, reading, and appending

# Function to write data to a text file
def write_to_file(filename, data):
    with open(filename, 'w') as file:  # 'w' mode opens the file for writing (creates if not exists)
        file.write(data)
    print(f"Data written to {filename} successfully.")

# Function to read data from a text file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:  # 'r' mode opens the file for reading
            content = file.read()
        print(f"Contents of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Function to append data to a text file
def append_to_file(filename, data):
    with open(filename, 'a') as file:  # 'a' mode opens the file for appending
        file.write(data)
    print(f"Data appended to {filename} successfully.")




def write_list_to_file(filename: str, my_list: list):
    """Writes a list to a text file, each item on a new line."""
    with open(filename, 'a') as file:
        for item in my_list:
            file.write(f"{item}\n")

my_list = ['apple', 'banana', 'cherry']
write_list_to_file('example.txt', my_list)





#
#
def write_dict_to_file(filename: str, my_dict: dict):
    """Writes a dictionary to a text file in a key=value format."""
    with open(filename, 'a') as file:
        for key, value in my_dict.items():
            file.write(f"{key}={value}\n")

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
write_dict_to_file('example.txt', my_dict)







# Example usage
# filename = 'example.txt'

# # # Writing to the file
# write_to_file(filename, "Hello, World!\nThis is the first line of the file.\n")
# Appending to the file
# append_to_file(filename, "Appending a new line to the file.\n")
# Reading from the file
# read_from_file(filename)
#
# # Reading again to see the appended content
# read_from_file(filename)
#
