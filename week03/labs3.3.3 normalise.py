#Please enter a string: Some StRiNg
#That String normalised is :some string
#we reduced the input string from 57 to 11 characters

astring = input("Please enter a string:")
new_string = astring.lower().strip()

astring_length = len(astring)
new_string_length = len(new_string)

print(f"That normalised string is: {new_string}")
print(f"We reduced the input string from {astring_length} to {new_string_length} characters")