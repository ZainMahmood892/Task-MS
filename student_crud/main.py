import sys
from crud import (
    create_student,
    get_all_students,
    search_students,
    get_student_by_id,
    update_student,
    delete_student,
)
from validation import (
    validate_name,
    validate_email,
    validate_phone,
    validate_age,
    validate_course,
)


def input_student_data(existing_data=None):
    """
    Collect student data from user input with validation.
    If existing_data is provided, allow empty input to keep current values.
    """
    while True:
        name_prompt = "Name"
        email_prompt = "Email"
        phone_prompt = "Phone"
        course_prompt = "Course"
        age_prompt = "Age"

        if existing_data:
            name_prompt += f" [{existing_data['name']}]"
            email_prompt += f" [{existing_data['email']}]"
            phone_prompt += f" [{existing_data['phone']}]"
            course_prompt += f" [{existing_data['course']}]"
            age_prompt += f" [{existing_data['age']}]"

        name = input(f"{name_prompt}: ").strip()
        if existing_data and name == "":
            name = existing_data["name"]
        if not validate_name(name):
            print("Invalid name. Please enter at least 2 characters.")
            continue

        email = input(f"{email_prompt}: ").strip()
        if existing_data and email == "":
            email = existing_data["email"]
        if not validate_email(email):
            print("Invalid email. Please enter a valid email address.")
            continue

        phone = input(f"{phone_prompt}: ").strip()
        if existing_data and phone == "":
            phone = existing_data["phone"]
        if not validate_phone(phone):
            print("Invalid phone. Please enter digits, spaces, +, - only.")
            continue

        course = input(f"{course_prompt}: ").strip()
        if existing_data and course == "":
            course = existing_data["course"]
        if not validate_course(course):
            print("Invalid course. Please enter at least 2 characters.")
            continue

        age = input(f"{age_prompt}: ").strip()
        if existing_data and age == "":
            age = str(existing_data["age"])
        if not validate_age(age):
            print("Invalid age. Please enter a valid positive integer.")
            continue

        return {
            "name": name,
            "email": email,
            "phone": phone,
            "course": course,
            "age": int(age),
        }


def add_student():
    print("\n========== ADD STUDENT ==========")
    student_data = input_student_data()
    success, message = create_student(student_data)
    if success:
        print(f"Success: {message}")
    else:
        print(f"Error: {message}")


def view_all_students():
    print("\n========== ALL STUDENTS ==========")
    students = get_all_students()
    if not students:
        print("No students found.")
        return
    print(
        f"{'ID':<5} | {'Name':<20} | {'Email':<30} | {'Phone':<15} | {'Course':<20} | {'Age':<3}"
    )
    print("-" * 105)
    for s in students:
        print(
            f"{s['id']:<5} | {s['name']:<20} | {s['email']:<30} | {s['phone']:<15} | {s['course']:<20} | {s['age']:<3}"
        )


def search_student():
    print("\n========== SEARCH STUDENT ==========")
    print("Search by:\n1. ID\n2. Name\n3. Email")
    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        sid = input("Enter Student ID: ").strip()
        if not sid.isdigit():
            print("Invalid ID. It must be numeric.")
            return
        student = get_student_by_id(int(sid))
        if student:
            print_student_details(student)
        else:
            print(f"No student found with ID {sid}")
    elif choice == "2":
        name = input("Enter Name to search: ").strip()
        results = search_students("name", name)
        if results:
            for s in results:
                print_student_details(s, separator=True)
        else:
            print("No student found with that name.")
    elif choice == "3":
        email = input("Enter Email to search: ").strip()
        results = search_students("email", email)
        if results:
            for s in results:
                print_student_details(s, separator=True)
        else:
            print("No student found with that email.")
    else:
        print("Invalid choice.")


def print_student_details(student, separator=False):
    if separator:
        print("-" * 40)
    print(f"ID    : {student['id']}")
    print(f"Name  : {student['name']}")
    print(f"Email : {student['email']}")
    print(f"Phone : {student['phone']}")
    print(f"Course: {student['course']}")
    print(f"Age   : {student['age']}")


def update_student_menu():
    print("\n========== UPDATE STUDENT ==========")
    sid = input("Enter Student ID to update: ").strip()
    if not sid.isdigit():
        print("Invalid ID. It must be numeric.")
        return
    student = get_student_by_id(int(sid))
    if not student:
        print(f"No student found with ID {sid}")
        return
    print("Current student information:")
    print_student_details(student)
    print("\nEnter new details (leave blank to keep current value):")
    new_data = input_student_data(existing_data=student)
    success, message = update_student(int(sid), new_data)
    if success:
        print(f"Success: {message}")
    else:
        print(f"Error: {message}")


def delete_student_menu():
    print("\n========== DELETE STUDENT ==========")
    sid = input("Enter Student ID to delete: ").strip()
    if not sid.isdigit():
        print("Invalid ID. It must be numeric.")
        return
    student = get_student_by_id(int(sid))
    if not student:
        print(f"No student found with ID {sid}")
        return
    print("Student details:")
    print_student_details(student)
    confirm = input(
        "Are you sure you want to delete this student? (yes/no): "
    ).strip().lower()
    if confirm == "yes":
        success, message = delete_student(int(sid))
        if success:
            print(f"Success: {message}")
        else:
            print(f"Error: {message}")
    else:
        print("Delete operation cancelled.")


def main():
    while True:
        print("\n====================================")
        print("STUDENT MANAGEMENT SYSTEM")
        print("=========================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student_menu()
        elif choice == "5":
            delete_student_menu()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()