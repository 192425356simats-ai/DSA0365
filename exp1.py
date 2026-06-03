import re
text = "My phone number is 9876543210"
# Search for a 10-digit number
pattern = r"\d{10}"
match = re.search(pattern, text)
if match:
    print("Phone Number Found:", match.group())
else:
