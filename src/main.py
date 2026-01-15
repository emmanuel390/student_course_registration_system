from registration_system import RegistrationSystem

def main():
    system = RegistrationSystem()

    while True:
        print("\nStudent Course Registration System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Display Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            system.add_student(student_id, name)
            print("Student added successfully.")

        elif choice == "2":
            course_code = input("Enter course code: ")
            course_title = input("Enter course title: ")
            system.add_course(course_code, course_title)
            print("Course added successfully.")

        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            if system.register_student_for_course(student_id, course_code):
                print("Student registered for course successfully.")
            else:
                print("Registration failed.")

        elif choice == "4":
            system.display_students()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
