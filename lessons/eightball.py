from random import randint 

question: str = input("What is your yes/no question?")
response: int = randint(0, 4) 

if response == 0:
    print("Yes, def")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("yes ofc")
elif response == 3:
    print("no way jose")
else:
    print("My sources say no")