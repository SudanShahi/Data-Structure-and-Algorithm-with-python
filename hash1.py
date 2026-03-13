students = {
    "Aarav": 85,
    "Sita": 92,
    "Bikram": 78,
    "Priya": 88,
    "Roshan": 95
}

# Main program loop
choice = 1

while choice != 0:
    print("\n" + "=" * 40)
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add/Update student grade")
    print("2. Search student grade")
    print("3. Print all students and grades")
    print("0. Exit")
    print("=" * 40)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = int(input("Enter grade: "))
        students[name] = grade
        print(f"Grade for {name} has been added/updated successfully!")

    elif choice == 2:
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name}'s grade is: {students[name]}")
        else:
            print(f"Student '{name}' not found in the system")

    elif choice == 3:
        if len(students) > 0:
            print("\nAll Students and Grades:")
            print("-" * 30)
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students in the system yet")

    elif choice == 0:
        print("Thank you for using Student Grade Management System!")

    else:
        print("Invalid choice! Please try again.")