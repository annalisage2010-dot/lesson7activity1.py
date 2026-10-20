classmates = ["Sam", "Mary", "jessica", "George", "Hailye"]
print("Class Title:", classmates)

print("Total students:", len(classmates))
print("First student:",classmates[0])
print("Last student:", classmates[-1])
print("First three:", classmates[:3])

classmates.append("Rose")
print("\nAfter adding Rose:", classmates)
classmates.remove("Sam")
print("After removing Sam:", classmates)
classmates.sort()
print("Sort Alphabetically:", classmates)
classmates.reverse(),
print("Reverse:", classmates)

teacher = {"name": "Samuel", "subject": "python", "experience": 5}
print("\nTeacher's profile:", teacher)

print("Subject:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not found"))
teacher["experience"] = 6
teacher["email"]="samuel.1995@school.com"
teacher.pop("experience")
print("Updated teacher's profile:", teacher)

roll_numbers=[1, 2, 3, 4, 5]
names=["Sam", "Mary", "Jessica", "George", "Hailye"]
students_directory = dict(zip(roll_numbers, names))
print("\nStudents Directory:", students_directory)
print("Student with Roll 3:", students_directory[3])