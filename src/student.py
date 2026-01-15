class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.registered_courses = []

    def register_course(self, course):
        self.registered_courses.append(course)
