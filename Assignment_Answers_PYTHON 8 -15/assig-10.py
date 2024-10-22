#  Replace a Keyword in a Text File


filename = 'sample.txt'

with open(filename, 'r') as file:
    content = file.read()

modified_content = content.replace('after', 'before')

with open(filename, 'w') as file:
    file.write(modified_content)

print("All occurrences of 'after' have been replaced with 'before' Keyword.")
