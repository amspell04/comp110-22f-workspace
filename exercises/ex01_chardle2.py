"""EX01 chardle resubmission"""

__author__ = "730560818"
from operator import indexOf

match_indices: int = 0 

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
    exit()

print("Searching for " + single_character + " in " + five_letter_word)


if single_character == five_letter_word[0]:
    print(single_character + " found at index 0")
    match_indices += 1

if single_character == five_letter_word[1]:
    print(single_character + " found at index 1")
    match_indices += 1

if single_character == five_letter_word[2]:
    print(single_character + " found at index 2")
    match_indices += 1

if single_character == five_letter_word[3]:
    print(single_character + " found at index 3")
    match_indices += 1

if single_character == five_letter_word[4]:
    print(single_character + " found at index 4")
    match_indices += 1


if match_indices == 0:
    print("No instances of " + single_character + " in " + five_letter_word)

if match_indices == 1:
    print("1 instance of " + single_character + " found in " + five_letter_word)

if match_indices == 2:
    print("2 instances of " + single_character + " found in " + five_letter_word)

if match_indices == 3:
    print("3 instances of " + single_character + " found in " + five_letter_word)

if match_indices == 4:
    print("4 instances of " + single_character + " found in " + five_letter_word)

if match_indices == 5:
    print("5 instances of " + single_character + " found in " + five_letter_word)