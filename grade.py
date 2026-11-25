def calculate_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")
department = input("Enter department: ")
semester = input("Enter semester: ")

mark1 = float(input("Enter Subject 1 marks: "))
mark2 = float(input("Enter Subject 2 marks: "))
mark3 = float(input("Enter Subject 3 marks: "))

total = mark1 + mark2 + mark3
average = total / 3
grade = calculate_grade(average)

print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("Department:", department)
print("Semester:", semester)
print("Subject 1 Marks:", mark1)
print("Subject 2 Marks:", mark2)
print("Subject 3 Marks:", mark3)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)