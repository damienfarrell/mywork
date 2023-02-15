# Write a program (guess1.py) that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right on

number = 5
guess = int(input(f"Please guess the number: "))

while guess != number:
    print("Wrong")
    guess = int(input("Please guess again: "))
    
print(f"Well done! Yes the number was {number}")