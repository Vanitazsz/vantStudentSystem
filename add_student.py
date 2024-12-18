class AddStudent:
    def __init__(self, student_database, student_info_class):
        self.student_data = student_database
        self.StudentInfo = student_info_class 

    def add_student(self, name, age, idnum, email, phone):
        student = self.StudentInfo(name, age, idnum, email, phone)
        self.write_to_file(student)
        self.student_data.add_student(student)
        print(f"Added Student {name} to the list.")

    def input_add_student(self):
        print("-" * 10, "Add New Student", "-" * 10)
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        idnumber = input("Enter Student ID: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        print("-" * 10, "Nothing follows", "-" * 10)
        self.add_student(name, age, idnumber, email, phone)

    def write_to_file(self, student):
        with open("student_data.txt", "a") as file:
            file.write(f"{student.getName()}, {student.getAge()}, {student.getIDNum()}, {student.getEmail()}, {student.getPhoneNum()}\n")
        print("Student data saved successfully!")
