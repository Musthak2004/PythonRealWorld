import pyperclip

# Step 1: Get text from clipboard
text = pyperclip.paste()

# Step 2: Split text into lines
lines = text.split('\n')

# Step 3: Add bullet star to each line
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Step 4: Join lines back into a single string
text = '\n'.join(lines)

# Step 5: Copy modified text back to clipboard
pyperclip.copy(text)