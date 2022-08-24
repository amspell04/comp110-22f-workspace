"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess?"))

if guess == SECRET:
    print("You guess correctly!")
    print("have a wonderful day :)")
    
else: 
    print("Sorry, wrong answer.")
    if guess > SECRET:
        print("you guessed too high.")
    else:
        print("you guessed too low")


print("Game over.")