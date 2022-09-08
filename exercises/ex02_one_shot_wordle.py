"""One shot wordle exercise with emoji function"""

__author__: str = "730560818"

secret_word: str = "python"
guess: str = str(input("What is your 6-letter guess?"))
match: int = 0
result: str = ""
character_exist: bool = False
alt: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret_word):
    guess: str = str (input("That was not 6 letters! Try again: "))  
while match < len(secret_word):
    while match < len(secret_word):
        if guess[match] == secret_word[match] and secret_word[alt]:
            result += f"{GREEN_BOX}"
            """if index of guess is equal to index of secret word or alternate index of secret word green box prints"""
        else: 
            while character_exist is not True and alt < len(secret_word):
                if guess[match] == secret_word[alt]:
                    result += f"{YELLOW_BOX}"
                    alt = 0
                    character_exist = True
                    """if guess index matches the alternate index of secret word but not orginal index yellow box prints"""
                if guess[match] != secret_word[alt]:
                    alt = alt + 1
                    """if guess index does not match alternate index of secret word test again using + 1 alternate index"""
                if alt >= len(secret_word):
                    result += f"{WHITE_BOX}"
                    character_exist = True
                    """if guess index does not match any alternate or regular index of secret word white box prints"""
     
        match = match + 1
        alt = 0
        character_exist = False

print(result)

if guess != secret_word:
    print("Not quite. Play again soon!")
if guess == secret_word:
    print("Woo! You got it!")
