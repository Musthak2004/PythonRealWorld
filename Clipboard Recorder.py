import pyperclip
import time

print("Recording clipboard... (Ctrl + C to stop)")

previous_content = ''

try:
    while True:

        try:
            content = pyperclip.paste()
        except:
            content = ""

        if content != previous_content:
            print("Copied:", content)
            previous_content = content

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nStopped recording clipboard.")