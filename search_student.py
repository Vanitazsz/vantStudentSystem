def searchs_student(studentlist, keyword):
    result = ""
    # Loop through each student object in the list
    for student in studentlist:
        # Compare the student ID using the getIDNum() method
        if student.getIDNum() == keyword:
            result = (f"Name: {student.getName()}\n"
                      f"Age: {student.getAge()}\n"
                      f"Student Number: {student.getIDNum()}\n"
                      f"Email: {student.getEmail()}\n"
                      f"Contact Number: {student.getPhoneNum()}")
            break
    if not result:
        result = "Student not found!"
    return result


# Assuming this function is in your search_student.py
def verify_login(student_list, idnum):
    for student in student_list:
        if student.getIDNum() == idnum:  # Accessing ID using getter method
            return student  # Return the StudentInfo object
    return None  # Return None if not found
