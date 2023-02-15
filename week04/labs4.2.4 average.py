# Write a program (average.py) that keeps reading numbers until the user
# enters a 0. (the program should append each of them into a list)
# The program should then print out each of the numbers entered and the
# average of them. (Use a list)

numbers = []
number = int(input("Enter number (0 to quit): "))

while number != 0:
    number = int(input("enter anouther (0 to quit): "))
    numbers.append(number)

print("Numbers entered: ", numbers)
print(f"The average is {sum(numbers)/len(numbers)}")