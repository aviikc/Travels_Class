class Student():
    def __init__(self, fname, lname, age, semester):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.semester = semester

    def returnStudent(self):
        return {"First Name": self.first_name,
                "Last Name": self.last_name,
                "Age": self.age,
                "Semester": self.semester
                }

class ClassRoom():
    def __init__(self):
        self.class_room = []
        
    def addStudent(self):
        self.f_name = input("Input First Name: ")
        self.l_name = input("Input Last Name: ")
        self.age = int(input("Age: "))
        self.semester = int(input("Enter Semester: "))
        student = Student(self.f_name, self.l_name, self.age, self.semester)
        self.class_room.append(student.returnStudent())

    def returnStudents(self):
        return self.class_room

if __name__ == "__main__":
    animation = ClassRoom()
    animation.addStudent()
    print(animation.returnStudents())
