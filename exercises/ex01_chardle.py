"""Ex01 - Chardle - A cute step toward Wordle."""

__author__ = "730495205"

chosen_word: str = input("Enter a 5 Character word: ")
if len(chosen_word) != 5:
    print("Error: Word must contain 5 Characters.")
    exit()
else:
    character: str= input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + chosen_word)
x: int = 0
if (character == chosen_word[0]):
    print(str(character) + " found at index 0")
    x = x + 1

if (character == chosen_word[1]):
    print(str(character) + " found at index 1")
    x = x + 1

if (character == chosen_word[2]):
    print(str(character) + " found at index 2")
    x = x + 1

if (character == chosen_word[3]):
    print(str(character) + " found at index 3")
    x = x + 1

if (character == chosen_word[4]):
    print(str(character) + " found at index 4")
    x = x + 1

if x ==1:
    print(str(1) + " instance of " + str(character) + " found in " + chosen_word)

if x>1:
    print(str(x) + " instance of " + str(character) + " found in " + chosen_word)

if x == 0:
    print(str(1) + " instance of " + str(character) + " found in " + chosen_word)
