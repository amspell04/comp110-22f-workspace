"""Create your own adventure."""

from tkinter.messagebox import YES


__author__: str = "730560818"

player: str = ""
points: int == 0
point_tracker: str = ""

def main() -> None:
    player: str = greet()
    challenge_one(1)
    global points

def greet() -> None:
    welcome: str = str(input(f"Welcome to Chances of Survival An interactive game where your choices will effect your players life. Please name your character: "))
    player = welcome

def challenge_one(chance: int) -> None:
    print(f"You have {chance} chances to complete this challenge.")
    challenge_prompt: str = str(input("There is a fire in the dorm, 5 doors down from your room. What do you do?\nEnter A to: Run down the hall screaming\nEnter B to: Call your mom\nEnter: "))
    response: str = ""
    a: str = "A"
    b: str = "B"
    while chance > 0:
            if challenge_prompt[0] == a[0]:
                response = f"WRONG! Your mom is sleeping, {player}. She doesn't answer you."
                points = 0
                point_tracker = (f"You have {points} points. :(")

            if challenge_prompt[0] == b[0]:
                response = f"CORRECT! A good start to a great independent college life. Nice going {player}."
                points = 3
                point_tracker = (f"You have {points} points! :)")

            chance = 0
    print(response)
    print(point_tracker)


def challenge_two(chance: int) -> None:


def fun_challenge() -> None:
     
