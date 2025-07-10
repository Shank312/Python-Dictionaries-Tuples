
# 📌 Task: Store info about students using nested dictionaries.

students = {
    "1001" : {"name": "Amit", "age": 18, "grade": "A"},
    "1002" : {"name": "Bhavna", "age": 19, "grade": "B"},
    "1003" : {"name": "Chirag", "age": 17, "grade": "A+"}
}

# Access student 1002's name
print("Student 1002 Name:", students["1002"]["name"])

# print all students 
print("\nAll Students: ")
for student_id, details in students.items():
    print(f"ID: {student_id}")
    for key, value in details.items():
        print(f"  {key}: {value}")
