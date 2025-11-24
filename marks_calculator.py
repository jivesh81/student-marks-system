students = {}

def add_marks():
    while True:
        print("\n==ADD STUDENT MARKS==")
        name = input("Enter student name (enter EXIT to exit): ")
        name = name.lower()
        if name == "exit":
            break
        else:
            marks = input("Enter marks: ")
            if marks.isdigit() and 0 <= int(marks) <= 100:
                students[name] = int(marks)
                print("Marks added ")
            else:
                print("Invalid input! Enter 0-100 only")

def view_marks():
    print("\n==ALL STUDENTS MARKS==")
    if len(students) == 0:
        print("No data available")
        return
    else:
        for name, marks in students.items():
            print(f"{name.capitalize()}: {marks}")

def find_topper():
    print("\n==TOPPER FINDER==")
    if len(students) == 0:
        print("No data available")
        return
    else:
        topper_name = max(students, key=students.get)
        topper_marks = students[topper_name]
        print(f"Topper student: {topper_name.capitalize()}")
        print(f"Topper marks: {topper_marks}")

def update_marks():
    print("\n==UPDATE STUDENT MARKS==")
    if len(students) == 0:
        print("No data available")
        return
    name = input("Enter student name to update: ").lower()
    if name in students:
        marks = input("Enter new marks: ")
        if marks.isdigit() and 0 <= int(marks) <= 100:
            students[name] = int(marks)
            print("Marks updated successfully!")
        else:
            print("Invalid input! Enter 0-100 only")
    else:
        print("Student not found!")

def delete_student():
    print("\n==DELETE STUDENT==")
    if len(students) == 0:
        print("No data available")
        return
    name = input("Enter student name to delete: ").lower()
    if name in students:
        del students[name]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def calculate_average():
    print("\n==CLASS AVERAGE==")
    if len(students) == 0:
        print("No data available")
        return
    total = sum(students.values())
    average = total / len(students)
    print(f"Total students: {len(students)}")
    print(f"Class average: {average:.2f}")

def search_student():
    print("\n==SEARCH STUDENT==")
    if len(students) == 0:
        print("No data available")
        return
    name = input("Enter student name to search: ").lower()
    if name in students:
        print(f"Student: {name.capitalize()}")
        print(f"Marks: {students[name]}")
    else:
        print("Student not found!")

def main():
    while True:
        print("\n" + "="*40)
        print("  STUDENT MARKS MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add student marks")
        print("2. View all marks")
        print("3. Find topper")
        print("4. Update marks")
        print("5. Delete student")
        print("6. Calculate class average")
        print("7. Search student")
        print("8. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            add_marks()
        elif choice == "2":
            view_marks()
        elif choice == "3":
            find_topper()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            search_student()
        elif choice == "8":
            print("\n" + "="*40)
            print("Thanks for using Student Marks Calculator!")
            print("="*40)
            break
        else:
            print("\nInvalid input! Please enter a number between 1-8")

main()