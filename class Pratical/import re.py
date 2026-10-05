import re

text = "My email is student@gmail.com and my phone number is 9876543210."

# Search for an email pattern
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
email = re.search(email_pattern, text)

# Search for a 10-digit phone number
phone_pattern = r'\b\d{10}\b'
phone = re.search(phone_pattern, text)

if email:
    print("Email:", email.group())

if phone:
    print("Phone Number:", phone.group())