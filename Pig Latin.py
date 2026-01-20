# English to pig latin
print("Enter the English message to translate into pig latin: ")
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # Stores translated words

for word in message.split():

    # 1. Remove non-letters at the start
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # 2. Remove non-letters at the end
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    # 3. Remember capitalization
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    # 4. Remove consonants from the start
    prefixConsonants = ''
    while len(word) > 0 and word[0] not in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # 5. Add Pig Latin ending
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # 6. Restore capitalization
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # 7. Reattach punctuation
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# 8. Join and print
print(' '.join(pigLatin))