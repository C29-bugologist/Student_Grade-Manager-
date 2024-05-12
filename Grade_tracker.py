# Function to enter grades for assignments
def enter_grades(student_info):
    # Ask for input: student ID, assignment name, and grade
    student_id = input("Enter student ID: ")
    assignment_name = input("Enter assignment name: ")
    grade = float(input("Enter grade: "))

    # Check if student ID exists in student_info
    if student_id in student_info:
        # If the student ID exists, add/update grade for the assignment
        if 'grades' in student_info[student_id]:
            student_info[student_id]['grades'][assignment_name] = grade
        else:
            student_info[student_id]['grades'] = {assignment_name: grade}
        print("Grade added successfully!")
    else:
        print("Student ID not found.")

# Function to calculate average grade for a student
def calculate_average_grade(student_info, student_id):
    if student_id in student_info:
        grades = student_info[student_id].get('grades', {})
        if grades:
            average_grade = sum(grades.values()) / len(grades)
            return average_grade
        else:
            return "No grades available for this student."
    else:
        return "Student ID not found."

# Function to view all students' data
# Function to view all students' data
def view_all_students_data(student_info):
    if not student_info:
        print("No student data available.")
        return
    print("\nAll Students' Data:")
    for student_id, info in student_info.items():
        print("\nStudent ID:", student_id)
        for key, value in info.items():
            if key != 'grades':
                print(key.capitalize() + ":", value)
            else:
                print("Grades:")
                for assignment, grade in value.items():
                    print("- {}: {}".format(assignment, grade))

if __name__ == "__main__":
    student_info = {}

    while True:
        print("\nOptions:")
        print("1. Enter grades for assignments")
        print("2. Calculate average grade for a student")
        print("3. View all students' data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            enter_grades(student_info)

        elif choice == '2':
            student_id = input("Enter student ID: ")
            average_grade = calculate_average_grade(student_info, student_id)
            print("Average grade for student {}: {}".format(student_id, average_grade))

        elif choice == '3':
            view_all_students_data(student_info)

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

