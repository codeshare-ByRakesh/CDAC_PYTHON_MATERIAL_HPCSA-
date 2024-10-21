import csv
# List Data to write
# data = [
#     ['Name', 'Age', 'Grade'],
#     ['Eve', 14, 'B'],
#     ['Frank', 16, 'A'],
#     ['Grace', 15, 'B']
# ]
# # Open a new CSV file for writing
# with open('new_students.csv', mode='w', newline='', encoding='utf-8') as file:
#     csv_writer = csv.writer(file)
#     # Write the data
#     csv_writer.writerows(data)
# print("Data written to new_students.csv")
#
# # Open the CSV file for reading
# with open('new_students.csv', mode='r', encoding='utf-8') as file:
#     csv_reader = csv.reader(file)
#     # Read the header (first row)
#     header = next(csv_reader)
#     print(f"Header: {header}")
#     # Read the remaining rows
#     for row in csv_reader:
#         print(row)
#

# Sample dictionary data (single record)
data = {'Name': 'Alice', 'Age': 30, 'City': 'New York'}
# Specify the file name
filename = 'students.csv'
# Writing to a CSV file
with open(filename, mode='w', newline='') as file:
    # Get the keys of the dictionary as fieldnames for the header
    fieldnames = data.keys()
    # Create a DictWriter object, passing the fieldnames as headers
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Write the header
    writer.writeheader()
    # Write the single row of data
    writer.writerow(data)
print(f'Data has been written to {filename}')
#
#
students = [
    {'ID': 'S001', 'Name': 'Alice Smith', 'Age': 20, 'Grade': 'A'},
    {'ID': 'S002', 'Name': 'Bob Brown', 'Age': 22, 'Grade': 'B'},
    {'ID': 'S003', 'Name': 'Charlie Johnson', 'Age': 19, 'Grade': 'A'},
]

with open(filename, 'w', newline='') as file:
    # Get the keys from the first dictionary as the header
    fieldnames = students[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

