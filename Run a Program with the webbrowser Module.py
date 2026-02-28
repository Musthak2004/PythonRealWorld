import webbrowser
import sys
import pyperclip
import urllib.parse

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# Encode spaces properly
encoded_address = urllib.parse.quote(address)

webbrowser.open(
    'https://www.openstreetmap.org/search?query=' + encoded_address
)

pyperclip.copy(address)

print("Opening map for:", address)