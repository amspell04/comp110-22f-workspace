"""Create your own adventure."""

from random import randint


__author__: str = "730560818"

player: str = ""
points: int = 0
HAPPY_FACE: str = "\U0001F92A"
SAD_FACE: str = "\U0001F972"
game_on: int = 1


def main() -> None:
    """This runs the whole game and allows the player to return and choose another step."""
    greet()
    global game_on
    global points
    global player
    is_playing: bool = True

    while game_on == 1 and is_playing:
        if points > 3:
            print(f"You currently have {points} points! {HAPPY_FACE}")
        if points < 3:
            print(f"You currently have {points} points. {SAD_FACE}")

        print("Which challenge would you like to complete?")
        print("Easy(1), Medium(2), Hard(3), or Super(4)? Enter QUIT to quit the game.")
        where_to: str = input("Please enter 1, 2, 3, or 4 to begin (or QUIT to leave): ")

        if where_to == "QUIT":
            print("Game Over. Goodbye.")
            is_playing = False
        if where_to == "1":
            points = easy_challenge(1, points)
        if where_to == "2":
            medium_challenge(2)
        if where_to == "3":
            hard_challenge(3, "731")
        if where_to == "4":
            super_challenge(3)


def greet() -> None:
    """This function greets the player, describes the game, and asks the player for their name."""
    global player
    print("Welcome to Chances of Survival.")
    print("An interactive game where your choices will effect your players life.")
    welcome: str = input("Please name your character: ")
    print("To begin the game, you will be given three challenges to choose to complete.\nYou may also choose to not play the game at all....making you an automatic loser.")
    player = welcome


def easy_challenge(chance: int, points: int) -> int:
    """This function asks the player to guess the correct choice between A and B."""
    print(f"For this first challenge you will have {chance} chance(s) to earn points")
    challenge_prompt: str = input("Enter A to: Call your mom\nEnter B to: Run down the hall screaming\nEnter: ")
    response: str = ""
    global player
    a: str = "A"
    b: str = "B"
    i: int = 0
    while i < chance:
        if challenge_prompt[0] == a[0]:
            response = f"WRONG! Your mom is sleeping, {player}. She doesn't answer you."
            points += 0
            print(f"You have {points} points. {SAD_FACE}")

        if challenge_prompt[0] == b[0]:
            response = f"CORRECT! A good start to a great independent college life. Nice going {player}."
            points += 3
            print(f"You have {points} points! {HAPPY_FACE}")
        i += 1
    print(response)
    return points


def medium_challenge(chance: int) -> str:
    """This function is similar to the easy_challenge. It gives three options and prompts the player to try and guess the correct answer."""
    print(f"For this second challenge, you will have {chance} chance(s) to earn points.")
    print("You are hungry, but have run out of meal swipes. What will you do?")
    print("Enter 1 to: Dumpster dive outside your dorm, there ought to be something to eat in there.\nEnter 2 to: Ask a friend for a free swipe into Lenoir\nEnter 3 to: Use your debit card to buy food on Franklin street")
    challenge_prompt: str = input("Enter: ")
    global points
    global player
    one: str = "1"
    two: str = "2"
    three: str = "3"
    point_tracker: str = ""
    i: int = 0
    while i < chance:
        if challenge_prompt[0] == one[0]:
            points += 3
            return (f"CORRECT! You found an orange and leftover chipotle. Yum! Enjoy your meal {player}\nYou have {points} points! {HAPPY_FACE} ")
        if challenge_prompt[0] == two[0]:
            print(f"WRONG! Lenoir food is gross and your friend is selfish. Better luck next time {player}")
            points += 0
            point_tracker = (f"You have {points} points. {SAD_FACE}")
        if challenge_prompt[0] == three[0]: 
            print(f"WRONG! Your card denies at checkout. Seems like your'e broke, {player}")
            points += 0
            point_tracker = (f"You have {points} points. {SAD_FACE}")
        challenge_prompt = input("Try again: ")
        i += 1
    return point_tracker


def hard_challenge(chance: int, correct_guess: str) -> str:
    """This function asks the player to guess a 3 digit integer that matches the correct_guess integer."""
    global player 
    global points
    print(f"Have you survived or thrived so far, {player}? Now it is time for a real challenge.")
    print("You have locked your booksack in a locker at Student Rec Center, but have forgotten your three digit code.")
    print(f"You will get {chance} tries to guess the three digit code before you look like a complete idiot")
    print("What is your 3 number guess? (Enter numbers in this format: 911)")
    guess: str = str(input("Enter guess:"))
    if len(guess) > len(correct_guess):
        guess = input("Too many numbers, try just three numbers: ")
    if len(guess) < len(correct_guess):
        guess = input("Too few numbers, try again with three numbers: ")
    
    idx: int = 1
    while idx < chance:
        if guess == correct_guess:
            points += 6
            return (f"CORRECT! Super point bonus! You now have {points} points!")
        else:
            guess = input("WRONG! Try again: ")
            points += 0
            idx += 1
    return "Your stuff seems to be locked away forever. Maybe next time, but probably not."


def super_challenge(question: int) -> str:
    """This function asks the player to guesss a random generated integer."""
    global points
    print("You are playing Club Penguin in class and your professor just called on you.")
    print("Your professor asks which question of the 100 question review packet the class is on.")
    print("Quick!! Guess which random question the class is discussing!")
    guess: int = int(input("Make a guess 1-100: "))
    question = randint(30, 50)

    if guess == question:
        print(f"CONGRATULATIONS!! You are a certified UNC genius, {player}. Your professor is astonished.")
        points += 8
    if guess != question: 
        print(f"Dang {player}! Your professor really caught you lacking. He is generous and gives you a hint.")
        guess_2: int = int(input("Make a guess 30-50: "))
    if guess_2 == question:
        print(f"CONGRATULATIONS!! You are (almost) a certified UNC genius, {player}. Your professor is somewhat astonished.")
        points += 5
    if guess_2 != question:
        print(f"WRONG! Sorry {player}. Looks like you should pay better attention next time.")
        return f"{question} was the correct answer"
    return "default return statement"


if __name__ == "__main__":
    main()