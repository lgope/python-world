class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def showInfoFunc(self):
        print(f"Name: {self.name}\nEmail: {self.email}")


personObj = Person("Lakshman", "email@example.com")
personObj.showInfoFunc()
