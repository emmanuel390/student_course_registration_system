from student import Student
from course import Course

class RegistrationSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)

    def add_course(self, course_code, course_title):
        course = Course(course_code, course_title)
        self.courses.append(course)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course
        return None

    def register_student_for_course(self, student_id, course_code):
        student = self.find_student(student_id)
        course = self.find_course(course_code)

        if student and course:
            student.register_course(course)
            return True
        return False

    def display_students(self):
        for student in self.students:
            print(f"\nStudent ID: {student.student_id}")
            print(f"Name: {student.name}")
            print("Registered Courses:")
            for course in student.registered_courses:
                print(f"- {course.course_code}: {course.course_title}")
