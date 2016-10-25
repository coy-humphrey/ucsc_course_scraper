class Student:
    def __init__( self, name ):
        self.name = name
        self.gpa = ''
        self.quarters = []

class Quarter:
    def __init__( self, name ):
        self.name = name
        self.courses = []

class Course:
    def __init__( self, subject, number, name, instructors, grade, units ):
        self.subject = subject
        self.number = number
        self.name = name
        self.instructors = instructors
        self.grade = grade
        self.units = units
