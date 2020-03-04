# Implement Python Switch Case Statement using Dictionary


def monday():
    return "monday"


def tuesday():
    return "tuesday"


def wednesday():
    return "wednesday"


def thursday():
    return "thursday"


def friday():
    return "friday"


def saturday():
    return "saturday"


def sunday():
    return "sunday"


def default():
    return "Incorrect day"


switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
}


def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()


print(switch(1))
print(switch(6))


# Implement Python Switch Case Statement using Class

class PythonSwitch:

    def switch(self, dayOfWeek):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "Monday"

    def case_2(self):
        return "Tuesday"

    def case_3(self):
        return "Wednesday"


s = PythonSwitch()

print(s.switch(1))
print(s.switch(0))
