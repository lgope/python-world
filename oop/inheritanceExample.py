class Person:
    def __init__(self, fname, lname, graduationYear):
        self.firstname = fname
        self.lastname = lname
        self.graduationYear = graduationYear

    def printInfo(self):
        print(f"My name is {self.firstname} {self.lastname}. And my graduation year is {self.graduationYear}")


class Student(Person):
    def __init__(self, fname, lname, graduationYear):
        super().__init__(fname, lname, graduationYear)


student1 = Student("Lakshman", "Gope", "2021")
student1.printInfo()

student2 = Student("Raton", "Biswas", "2021")
student2.printInfo()