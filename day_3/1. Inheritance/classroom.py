


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    def printName(self):
        return f"{self.firstname} {self.lastname}"


class Student:
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        return f"{self.firstname} {self.lastname}, {self.subject}"


class Teacher:
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course

    def printNameCourse(self):
        return f"{self.firstname} {self.lastname}, {self.course}"

    
    
        