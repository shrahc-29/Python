#Python code for Student Directory:

students =[]   #list to store student information

def add_stud(name, age, marks):    #Function to add student info
  student = {'name': name, 'age': age, 'marks': grade(marks) }
  students.append(student)


def update(name, new_mrks):     #Function to update student info via name
  for student in students:
    if student['name']==name:
      student['marks']=new_mrks
      student['grade']=grade(new_mrks)

      print("Marks successfully updated")
      return
  print("Student not found.")


def grade(marks):   #Function for grades based on marks
  if marks>=90:
   return "A"
  elif marks>=80:
   return "B"
  elif marks>=70:
   return "C"
  elif marks>=60:
    return "D"
  else:
    return "F"


def display():       #Function for displaying student info
  print("Student Information: ")
  for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")


#Menu driven code:

while True:
    print("\n--- Student Directory Menu ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = int(input("Enter student marks: "))
        add_stud(name, age, marks)

    elif choice == '2':
        name = input("Enter the name of the student to update: ")
        new_marks = int(input("Enter new marks: "))
        update(name, new_marks)

    elif choice == '3':
        print("   ")
        display()

    elif choice == '4':
        print("Exiting student info directory.")
        break

    else:
        print("Invalid choice.")
