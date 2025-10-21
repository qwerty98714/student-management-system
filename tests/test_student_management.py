import unittest
from src.student_management import Student, Course, Enrollment

class TestStudentManagement(unittest.TestCase):
    def test_student_creation(self):
        student = Student(1, "Alice")
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, "Alice")

    def test_course_creation(self):
        course = Course(101, "Mathematics")
        self.assertEqual(course.id, 101)
        self.assertEqual(course.name, "Mathematics")

    def test_enrollment(self):
        student = Student(1, "Alice")
        course = Course(101, "Mathematics")
        enrollment = Enrollment()
        enrollment.enroll(student, course)
        self.assertIn(course, student.list_courses())
        self.assertIn(student, course.list_students())

    def test_double_enrollment(self):
        student = Student(1, "Alice")
        course = Course(101, "Mathematics")
        enrollment = Enrollment()
        enrollment.enroll(student, course)
        enrollment.enroll(student, course)
        self.assertEqual(len(student.list_courses()), 1)
        self.assertEqual(len(course.list_students()), 1)

if __name__ == "__main__":
    unittest.main()
