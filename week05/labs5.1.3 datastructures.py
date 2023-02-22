student = {
    "Name" : "Mary",
    "Modules" : [
        {
            "CourseName" : "Programming",
            "Grade" : 45
        },
        {
            "CourseName" : "History",
            "Grade" : 99
        }
    ]
}

#print(f"Student: {student['Name']}")
#for module in student["Modules"]:
#   print(f"\n\t {module['CourseName']} : {module['Grade']}")

x = 1
while x != "":
    x = input("Enter module name: ")
    print(f"{student['Modules'][0]['CourseName']}")
