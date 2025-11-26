# import time
#
# try:
#     a= int(input("Enter any number:"))
#     b = int(input("Enter any number:"))
#
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as v:
#     print(v)
# else:
#     c=a/b
#     print(c)
# finally:
#     print(f'{time.strftime("%H:%M:%S", time.localtime())}')
#
#
#
import csv

filename = "students_data.csv"
students = []

while True:
    name = input("Enter the name of student: ")
    roll_no = int(input("Enter the roll no of student: "))
    marks = int(input("Enter the marks of student: "))
    grade = input("Enter the grade of student: ")

    # Store data in list
    students.append({
        "Name": name,
        "Roll_No": roll_no,
        "Marks": marks,
        "Grade": grade
    })

    # Ask user if they want to continue
    choice = input("Would you like to add another record? (yes/no): ").lower()
    if choice != 'y':
        break

# Write data to CSV after loop ends
with open(filename, "w", newline="") as csvfile:
    fieldnames = ["Name", "Roll_No", "Marks", "Grade"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print(f"\n✅ All data successfully saved in '{filename}'")
