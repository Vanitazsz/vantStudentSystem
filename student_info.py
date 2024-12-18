class Student:
    def __init__(self, name, age, idnum, email, phone):
        self.name = name
        self.age = age
        self.idnum = idnum
        self.email = email
        self.phone = phone  # Attribute is correctly named 'phone'

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setIDNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email

    def setPhoneNum(self, phone):
        self.phone = phone

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getIDNum(self):
        return self.idnum

    def getEmail(self):
        return self.email

    def getPhoneNum(self):
        return self.phone  # Corrected this line to return 'self.phone'


class StudentData:
    def __init__(self):
        self.allstudents = []
        self.read_file()

    def add_student(self, student):
        # Add a student to the list
        self.allstudents.append(student)

    def read_file(self):
        try:
            with open("student_data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    student_data = line.strip().split(", ")
                    student = Student(student_data[0], student_data[1], student_data[2], student_data[3], student_data[4])
                    self.allstudents.append(student)
                print("Student list loaded successfully!")
        except FileNotFoundError:
            print("No existing file found. Starting with an empty student list.")
