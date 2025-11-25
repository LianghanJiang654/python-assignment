def get_student_info():
    """Collect and validate single student's info (name, ID, grade)"""
    student = {}
    student["name"] = input("Enter student name: ").strip()
    student["id"] = input("Enter student ID: ").strip()

    while True:
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                student["status"] = "Pass" if grade >= 60 else "Fail"
                student["grade"] = grade
                return student
            print("Grade must be 0-100!")
        except ValueError:
            print("Enter a number!")


def save_to_file(students):
    """Save list of students to text file (file handling)"""
    with open("grades.txt", "w") as f:
        for s in students:
            f.write(f"Name: {s['name']}, ID: {s['id']}, Grade: {s['grade']}, Status: {s['status']}\n")
    print("\nData saved to grades.txt!")


def main():
    """Main function: Core program flow"""
    students = []
    print("=== Simple Grade Manager ===")

    while input("\nAdd a student? (y/n): ").lower() == "y":
        students.append(get_student_info())

    if students:
        print("\n=== Student List ===")
        for idx, s in enumerate(students, 1):
            print(f"{idx}. {s['name']} (ID: {s['id']}) - Grade: {s['grade']}, Status: {s['status']}")
        save_to_file(students)
    else:
        print("No students added!")

if __name__ == "__main__":
    main()