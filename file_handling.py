# file=open("shubham.txt",'r')
# data=file.read()
# print(data)
# file.close()

# file=(open("shubham.txt",'a'))
# data=file.append()
# print(data)
# file.close()

# file=open("kc.txt",'w+')
# file.write("shubham6")
# print(file)
# file.close()
#



# file=open("shubham.txt",'r')
# print(file.read())
# file.close()
# file=open("shubham.txt","w+")
#
# file.write("123")
# print(file)

# file=open("shubham6.txt","r+")
# file.write("123")
#
# file.close()
 # reader = csv.reader(csvfile)

# d=["shubham",45,"new delhi"]
# file = open("data.csv","w+")
# file.write(str(d))
# file.close()




# with open()
import csv
filename="students_result.csv"
students = []
while True:

 Name=str(input("Enter the name of student:"))
 Roll_no=int(input("Enter the roll no of student:"))
 Marks=int(input("Enter the marks of student:"))
 Grade=str(input("Enter the grade of student:"))
 students.append({
     "Name": Name,
     "Roll_no": Roll_no,
     "Marks": Marks,
     "Grade": Grade,})

 choice = input("Would you like to add another record? (yes/no): ").lower()
 if choice != 'yes':
         break
 with open(filename, "w", newline="") as csvfile:
    fieldnames = ["Name", "Roll_no", "Marks", "Grade"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print(f"\n✅ All data successfully saved in '{filename}'")
# showing in terminal
print(f"\n All data successfully saved in '{filename}'")

print("\n=== Student Records ===")

with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['Name']:^15} {row['Roll_no']:^10} {row['Marks']:^10} {row['Grade']:^10}")


