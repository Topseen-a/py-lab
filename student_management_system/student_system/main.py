from student_system.student_management_system import StudentManagementSystem


def main():
    management_system = StudentManagementSystem()

    while True:
        print("=== Student Management System ===")
        print("1 -> Register Student")
        print("2 -> Add Course")
        print("3 -> Enroll Student in Course")
        print("4 -> Assign Grade")
        print("5 -> View Student Details")
        print("6 -> Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter student name: ")
            student_id = management_system.register_student(name)
            print("Student registered with ID:", student_id)

        elif choice == "2":
            code = input("Enter course code: ")
            title = input("Enter course title: ")
            management_system.add_course(code, title)
            print("Course added successfully.")

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            course_code = input("Enter course code: ")
            management_system.enroll_student(student_id, course_code)
            print("Enrollment successful.")

        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            course_code = input("Enter course code: ")
            grade = float(input("Enter grade (0-100): "))
            management_system.assign_grade(student_id, course_code, grade)
            print("Grade assigned successfully.")

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            student = management_system.get_student(student_id)

            print("Student Name:", student.get_name())
            print("Student ID:", student.get_id())
            print("Enrollments:")

            for enrollment in student.get_enrollments():
                course = enrollment.get_course()
                grade = enrollment.get_grade()
                print(course.get_code(), "-", course.get_title(), "| Grade:", grade)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
