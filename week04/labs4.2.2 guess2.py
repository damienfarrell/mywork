# How would you modify the program in 3 (guess2.py) above, so that the
# program tells the user if there guess is too high or too low, each time they
# guess. HINT: put an if statement inside the while loop

import random

number = random.randint(0, 100)
guess = int(input(f"Please guess the number: "))

while guess != number:
    print("Wrong")
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    guess = int(input("Please guess again: "))
    
print(f"Well done! Yes the number was {number}")