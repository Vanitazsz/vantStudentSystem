from tkinter import *
from functools import partial
from add_student import AddStudent
from search_student import searchs_student
from student_info import Student, StudentData

# Initialize backend objects
studdat = StudentData()
add_student_handler = AddStudent(studdat, Student)

# Create main window
win = Tk()
win.title("Student Management System - Roblox Style")
win.configure(bg="#232323")  # Dark background for Roblox-style UI

# Helper Functions
def update_content(frame, content_func):
    for widget in frame.winfo_children():
        widget.destroy()
    content_func(frame)

def content1_func(frame):  # Show logged-in student information
    Label(frame, text="Your Information", font=("Arial", 16), pady=20, bg="#2c2f33", fg="white").pack()

    info_frame = Frame(frame, bg="#99aab5", width=600, height=150)
    info_frame.pack(pady=20, padx=20)
    info_frame.pack_propagate(False)  # Prevent resizing

    info = (f"Name: {user_info[0]}\n"
            f"Age: {user_info[1]}\n"
            f"Student ID: {user_info[2]}\n"
            f"Email: {user_info[3]}\n"
            f"Phone: {user_info[4]}")

    Label(info_frame, text=info, font=("Arial", 14), bg="#99aab5", fg="black", justify="left", anchor="w").pack(fill="both", padx=10, pady=10)


def content2_func(frame):  # Search for a student
    Label(frame, text="Search Student", font=("Arial", 16), pady=20, bg="#2c2f33", fg="white").pack()

    input_frame = Frame(frame, bg="#99aab5", width=600, height=100)
    input_frame.pack(pady=20, padx=20)
    input_frame.pack_propagate(False)  # Prevent resizing

    Label(input_frame, text="Enter Student ID:", font=("Arial", 14), bg="#99aab5", fg="black", anchor="w").pack(pady=5, padx=10, fill="x")
    search_entry = Entry(input_frame, font=("Arial", 14), width=30)
    search_entry.pack(pady=5, padx=10)

    result_frame = Frame(frame, bg="#99aab5", width=600, height=150)
    result_frame.pack(pady=20, padx=20)
    result_frame.pack_propagate(False)

    def perform_search():
        student_id = search_entry.get()
        result = searchs_student(studdat.allstudents, student_id)
        result_label.config(text=result)

    Button(input_frame, text="Search", font=("Arial", 14), bg="#7289da", fg="white", command=perform_search, height="30", width="20").pack(pady=5)
    result_label = Label(result_frame, text="", font=("Arial", 14), bg="#99aab5", fg="black", anchor="w", justify="left")
    result_label.pack(fill="both", padx=10, pady=10)


def content3_func(frame):  # Show all students
    Label(frame, text="All Students", font=("Arial", 16), pady=20, bg="#2c2f33", fg="white").pack()

    # Scrollable Frame
    canvas = Canvas(frame, bg="#2c2f33", highlightthickness=0)
    scroll_y = Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="#2c2f33")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scroll_y.set)

    canvas.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")

    all_students = studdat.allstudents
    if not all_students:
        Label(scrollable_frame, text="No students available.", font=("Arial", 14), bg="#2c2f33", fg="white").pack(pady=10)
    else:
        for student in all_students:
            student_frame = Frame(scrollable_frame, bg="#99aab5", width=600, height=150)
            student_frame.pack(pady=10, padx=20)
            student_frame.pack_propagate(False)

            info = (f"Name: {student.getName()}\n"
                    f"Age: {student.getAge()}\n"
                    f"ID: {student.getIDNum()}\n"
                    f"Email: {student.getEmail()}\n"
                    f"Phone: {student.getPhoneNum()}")

            Label(student_frame, text=info, font=("Arial", 12), bg="#99aab5", fg="black", justify="left", anchor="w").pack(fill="both", padx=10, pady=10)


def content4_func(frame):  # Add a new student
    Label(frame, text="Add Student", font=("Arial", 16), pady=20, bg="#2c2f33", fg="white").pack()
    fields = ["Name", "Age", "Student ID", "Email", "Phone"]
    entries = {}

    for field in fields:
        Label(frame, text=f"{field}:", font=("Arial", 14), bg="#2c2f33", fg="white").pack(pady=5)
        entry = Entry(frame, font=("Arial", 14), width=30)
        entry.pack(pady=5)
        entries[field] = entry

    def add_new_student():
        name = entries["Name"].get()
        age = entries["Age"].get()
        idnum = entries["Student ID"].get()
        email = entries["Email"].get()
        phone = entries["Phone"].get()

        if name and age and idnum and email and phone:
            add_student_handler.add_student(name, age, idnum, email, phone)
            result_label.config(text="Student added successfully!", fg="green")
        else:
            result_label.config(text="Please fill in all fields!", fg="red")

    Button(frame, text="Add Student", font=("Arial", 14), bg="#7289da", fg="white", command=add_new_student).pack(pady=10)
    result_label = Label(frame, text="", font=("Arial", 14), bg="#2c2f33", fg="white")
    result_label.pack()

def login():
    username = username_entry.get()
    global user_info
    if username.lower() == 'admin':
        user_info = ['Admin', 'N/A', 'Admin', 'admin@school.com', 'N/A']
        login_div.pack_forget()
        main_div.pack(side="left", fill="both", expand=True)
        menu_div.pack(side="left", fill="y")
    else:
        user = next((s for s in studdat.allstudents if s.getIDNum() == username), None)
        if user:
            user_info = [user.getName(), user.getAge(), user.getIDNum(), user.getEmail(), user.getPhoneNum()]
            login_div.pack_forget()
            main_div.pack(side="left", fill="both", expand=True)
            menu_div.pack(side="left", fill="y")
        else:
            error_label.config(text="Invalid Login. Try Again!")

def logout():
    main_div.pack_forget()
    login_div.pack(side="left", fill="both", expand=True)

# Create frames
login_div = Frame(win, bg="#2c2f33")  # Login Screen
main_div = Frame(win, bg="#2c2f33")   # Main Menu Frame
menu_div = Frame(main_div, bg="#99aab5")
content_div = Frame(main_div, bg="#23272a")

# Login screen UI
Label(login_div, text="Student Management System", font=("Arial", 28, "bold"), pady=20, bg="#2c2f33", fg="white").pack()
Label(login_div, text="Login", font=("Arial", 24), pady=20, bg="#2c2f33", fg="white").pack()
Label(login_div, text="Username:", font=("Arial", 14), bg="#2c2f33", fg="white").pack(pady=5)
username_entry = Entry(login_div, font=("Arial", 14), width=30)
username_entry.pack(pady=5)

login_btn = Button(login_div, text="Login", font=("Arial", 14), bg="#7289da", fg="white", width=15, command=login)
login_btn.pack(pady=20)
error_label = Label(login_div, text="", font=("Arial", 12), bg="#2c2f33", fg="#e74c3c")
error_label.pack()

# Main menu buttons
menu_options = [
    ("Your Information", content1_func),
    ("Search Student", content2_func),
    ("All Students", content3_func),
    ("Add Student", content4_func),  # New option added
    ("Logout", logout)
]

for idx, (text, command) in enumerate(menu_options):
    if text == "Logout":
        Button(menu_div, text=text, font=("Arial", 14), width=20, bg="#e74c3c", fg="white", command=command).grid(row=idx, column=0, pady=10)
    else:
        Button(menu_div, text=text, font=("Arial", 14), width=20, bg="#7289da", fg="white",
               command=lambda cmd=command: update_content(content_div, cmd)).grid(row=idx, column=0, pady=10)

# Initialize the login screen
login_div.pack(side="left", fill="both", expand=True)

# Layout for main menu
menu_div.pack(side="left", fill="y")
content_div.pack(side="left", fill="both", expand=True)

# Set the window size
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}"), win.mainloop()
