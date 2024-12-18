class PrintStudent:
    def __init__(self, student_database):
        self.student_data = student_database

    def print_all_students(self):
        print("\n", "-"*15, "All Students", "-"*15, "\n")
        # Replace `get_all_students` with `allstudents`
        for student in self.student_data.allstudents:
            print(f"Name: {student.getName()}\n"
                  f"Age: {student.getAge()}\n"
                  f"Student ID: {student.getIDNum()}\n"
                  f"Email: {student.getEmail()}\n"
                  f"Phone: {student.getPhoneNum()}\n")
        print("\n", "-"*15, "Nothing Follows", "-"*15, "\n")
