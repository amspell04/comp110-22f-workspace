"""EX01- Chardle - A cute step toward Wordle."""

__author__ = "730560818"

count_match: int = 0

five_letter_word: str = str(input("Enter a 5-character word: "))
if len(five_letter_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(five_letter_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = str(input("Enter a single character: "))
if len(single_character) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(single_character) < 1:
    print("Error: Character must be a single character.")

print("Searching for " + single_character + " in " + five_letter_word)

if five_letter_word == "hello":
    if single_character == "e":
        print("e found at index 1")
        count_match + 1
        print("1 instance of e found in hello")

if five_letter_word == "heels":
    if single_character == "s":
        print("s found at index 4")
        count_match + 1
        print("2 instances of s found in heels")
    if single_character == "e":
        print("e found at index 1")
        print("e found at index 2")
        count_match + 2
        print("2 instances of e found in heels")
    if single_character == "h":
        print("h found at index 0")
        count_match + 1
        print("1 instance of h in heels")

    if single_character == "d":
        count_match
        print("No instances of d found in heels")

