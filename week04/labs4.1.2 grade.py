import math

grade = math.ceil((float(input("Enter the percentage "))))

if grade <= 40:
    print(f"{grade} = Fail")
elif grade >= 40 and grade <= 49:
    print(f"{grade} = Pass")
elif grade >= 50 and grade <= 59:
    print(f"{grade} = Merit 2")
elif grade >= 60 and grade <= 69:
    print(f"{grade} = Merit 1")
elif grade >= 70:
    print(f"{grade} = Distinction")