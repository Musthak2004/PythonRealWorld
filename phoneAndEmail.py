"""What is this project?

Imagine a big webpage with thousands of words…

You want only:

✔ Phone numbers
✔ Email addresses

Instead of searching manually 😩
👉 This program finds them automatically 💪"""

import pyperclip, re

# Phone number regex
phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # Area code
    (\s|-|\.)?                      # Separator
    (\d{3})                         # First 3 digits
    (\s|-|\.)                       # Separator
    (\d{4})                         # Last 4 digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # Extension
)''', re.VERBOSE)

# Email regex
email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # Username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # Domain name
    (\.[a-zA-Z]{2,4})   # Dot something
)''', re.VERBOSE)

# Get text from clipboard
text = str(pyperclip.paste())

# Store matches
matches = []

# Find phone numbers
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])

    if groups[6] != '':
        phone_num += ' x' + groups[7]

    matches.append(phone_num)

# Find email addresses
for groups in email_re.findall(text):
    matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")
