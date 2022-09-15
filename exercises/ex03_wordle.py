"""Creating a wordle system using functions."""

__author__: str = "730560818"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "codes"


def contains_char(word: str, char: str) -> bool: 
    """This function searches for the single char inside the word string indices."""
    # This function runs through the indices of a string checking for the matching char. 
    # If character matches string results will be True, if not the program returns False. 
    assert len(char) == 1
    count: int = 0
    while count < len(word):
        if char == word[count]:
            return True 
        if char != word[count]:
            count = count + 1
        if count >= len(word):
            return False    
    return False


def emojified(guess: str, secret: str) -> str:
    """Tests parameters for matching indices and returns appropriate colored box according to match or not."""
    # This function goes through each index of the string and tests for matching indices.
    # Function makes use of contain_char function which automatically runs through variable indexes.
    assert len(guess) == len(secret)
    count: int = 0
    codified: str = ""
    while count < len(secret):
        if guess[count] == secret[count]:
            codified += f"{GREEN_BOX}"
        else:
            if contains_char(secret, guess[count]) is True:
                codified += f"{YELLOW_BOX}"
            if contains_char(secret, guess[count]) is False:
                codified += WHITE_BOX
        count = count + 1
    return codified


def input_guess(expected_length: int) -> str:
    """Controls the expected length of the guess from user."""
    guess: str = str(input(f"Enter a {expected_length} character word: "))
    # This function makes sure that the input guess is the appropriate length. 
    # If guess is not appropriate length, guess is prompted again. 
    while len(guess) != expected_length:
        guess = str(input(f"That wasn't {expected_length} chars! Try again: "))
    return guess


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    N: int = 1
    main_move: bool = True
    while main_move is True:
        if N <= 6:
            # Loop enters here if N less or equal to 6 
            # Uses f string to count turns and uses input_huess and emojified to print emoji string
            print(f"=== Turn {N}/6 ===")
            guess: str = input_guess(5) 
            print(emojified(guess, secret))    
        if guess == secret: 
            # Loop enters here only if the guess from input_guess == our secret "codes". Program ends.
            print(f"You won in {N}/6 turns!")
            main_move = False  
        if N > 6:
            # Loop enters here only when N is greater than 6. The turns for the user are over. Program ends.
            print("X/6 - Sorry, try again tomorrow!")
            main_move = False 
        N += 1


if __name__ == "__main__":
    main()