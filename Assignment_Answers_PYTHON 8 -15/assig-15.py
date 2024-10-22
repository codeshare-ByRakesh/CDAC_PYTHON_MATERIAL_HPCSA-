# Assig-1     Extracting phone number

import re

def extract_phone_numbers(text):
    pattern = r'\(\d{3}\) \d{3}-\d{4}'
    return re.findall(pattern, text)

# Example usage
text_with_numbers = "You can reach me at (123) 456-7890 or (987) 654-3210."
phone_numbers = extract_phone_numbers(text_with_numbers)
print("Extracted Phone Numbers:", phone_numbers)


# Assig-2     Extracting Hashtag


import re

def extract_hashtags(text):
    pattern = r'#[A-Za-z]{4,}'
    hashtags = re.findall(pattern, text)

    unique_hashtags = set(tag.lower() for tag in hashtags)
    return unique_hashtags

# Example usage
social_media_post = "Loving #Python, #coding, and #AI! Also enjoying #python and #DataScience."
hashtags = extract_hashtags(social_media_post)
print("Extracted Hashtags:", hashtags)

