# imports
import random
from pyinputplus import inputInt

to_guess = random.randint(1, 100)

for attempt in range(10):
    print(f'Remaining attempts: {10 - attempt}')
    guess = inputInt("Guess the number (1-100): ", min=1, max=100)

    if guess > to_guess:
        print("Too high")

    elif guess < to_guess:
        print("Too low")

    else:
        print("BINGO!! A winner is you")
        break

else:
    print("Ohno!! You lose :'()")