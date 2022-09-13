
from ast import While


__author__: str = "730560818"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "codes"

def contains_char(word:str, char:str) -> bool:
    """This function searches for the single char inside the word string indices."""
    assert len(char) == 1
    count: int = 0
    while count < len(word):
        if char == word[count]:
            return True 
        if char != word[count]:
            count = count + 1
        if count >= len(word):
            return False    

def emojified(guess:str, secret:str) -> str:
    """Tests parameters for matching indices and returns appropriate colored box according to match or not."""
    assert len(guess) == len(secret)
    count: int = 0
    codified: str = ""
    while count < len(secret):
        if guess[count] == secret[count]:
            codified += f"{GREEN_BOX}"
        else:
                if contains_char(secret,guess[count]) == True:
                    codified += f"{YELLOW_BOX}"
                if contains_char(secret,guess[count]) == False:
                    codified += f"{WHITE_BOX}"
        count = count + 1
    return(codified)

def input_guess(expected_length:int) -> str:
    """Controls the expected length of the guess from user."""
    guess: str = str(input(f"Enter a {expected_length} character word: "))
    while len(guess) != expected_length:
        guess: str = str(input(f"That wasn't {expected_length} chars! Try again: "))
    if len(guess) == expected_length:
        return guess
                
def main()-> None:
    """The entrypoint of the program and the main game loop."""
    N: int = 1
    while __name__ == "__main__":
        if N <= 6:
            print(f"=== Turn {N}/6 ===")
            guess: str = input_guess(5) 
            print(emojified(guess,secret))    
            if guess == secret: 
                return(f"You won in {N}/6 turns!")
        if N == 7:
            print("X/6 - Sorry, try again tomorrow!")
            __name__ != "__main__"
            quit()
        N += 1
       

if __name__ == "__main__":
    main()