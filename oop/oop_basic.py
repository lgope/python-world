# Class, Object
class Person:
    def __init__(self, person_name: str, birth_year: int, height_inches: int = None):
        self.__name = person_name
        self.__birth_year = birth_year
        self.__height = height_inches

    def get_name(self):
        return self.__name

    def get_birth_year(self):
        return self.__birth_year

    def set_name(self, new_name: str):
        if self.__has_any_number(new_name):
            print('Sorry! Person name can\'t have number.')
            return
        self.__name = new_name

    def __has_any_number(self, str_value: str):
        return "0" in str_value

    def get_summary(self):
        return f'Name: {self.__name}, DOBY: {self.__birth_year}, Height: ' \
               f'{self.__height if self.__height is not None else "N/A"}'


# person_a = Person('Lakshman', 1999, 82)
#
# print(person_a.get_summary())

person_list = [
    Person('Lakshman', 1999, 82),
    Person('Raton', 2000),
    Person('Emon', 1992, 85),
    Person('Bar', 2021, 72),
    Person('Foo', 1990),
    Person('Bob', 1954, 89),
]


# for person in person_list:
#     if person.get_birth_year() >= 1990:
#         print(person.get_summary())

# Class, Inheritance
class Student(Person):
    def __init__(self, person_name: str, birth_year: int, email: str, student_id: str):
        super().__init__(person_name, birth_year)
        self.__email = email
        self.__student_id = student_id

    def get_email(self):
        return self.__email

    def get_student_id(self):
        return self.__student_id

    def get_summary(self):
        return f'Name: {self.get_name()} Email: {self.get_email()}, Birth: {self.get_birth_year()}'

    def __str__(self):
        return self.get_summary()

    def __repr__(self):
        return self.get_summary()


student_a = Student('Lakshman', 1998, 'lakshman@gmail.com', '123456')
print(student_a)
student_a.set_name('Lakshman Gope')
print(student_a)
