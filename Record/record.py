students = [] 
def add_student(): 
    name = input("Enter student name: ") 
    roll = input("Enter roll number: ") 
    students.append({"name": name, "roll": roll}) 
    print("Student added!\n") 
def view_students(): 
    if not students: 
        print("No students found.\n") 
        return 
    for s in students: 
        print(f"Name: {s['name']}, Roll: {s['roll']}") 
    print() 
def search_student(): 
    roll = input("Enter roll number to search: ") 
    for s in students: 
        if s["roll"] == roll: 
            print(f"Found: {s['name']}") 
            return 
    print("Student not found.\n") 
while True: 
    print("1. Add Student\n2. View All\n3. Search\n4. Exit") 
    choice = input("Enter your choice: ") 
     
    if choice == "1": 
        add_student() 
    elif choice == "2": 
        view_students() 
    elif choice == "3": 
        search_student() 
    elif choice == "4": 
        break 
    else: 
        print("Invalid choice\n") 