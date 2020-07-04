# replace domain
def replace_domain(email, old_domain, new_domain):
    if '@' + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return new_domain


# Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

def first_and_last(message):
    if len(message) == 0:
        return True
    else: return message[0] == message[-1]

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


# Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
print(word.index('x'))

# Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
def initials(phrase):
    words = phrase.split()
    print(words)
    result = ""
    for word in words:
        result += word[:1]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


# Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

def student_grade(name, grade):
    	return f"{name} received {grade}% on the exam"

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))