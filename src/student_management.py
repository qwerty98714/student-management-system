# student_management.py

class Student:
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    def enroll(self, course):
        """Enroll the student in a course and update both student and course lists."""
        self.courses.append(course)
        course.add_student(self)

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"


class Course:
    def __init__(self, course_id: int, title: str):
        self.course_id = course_id
        self.title = title
        self.students = []

    def add_student(self, student):
        """Add a student to the course if not already enrolled."""
        if student not in self.students:
            self.students.append(student)

    def __repr__(self):
        return f"Course({self.course_id}, {self.title})"


class Enrollment:
    """Manages collections of students and courses and their enrollment relationships."""

    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student_id: int, name: str, email: str) -> Student:
        """Create a new Student and add to the list."""
        student = Student(student_id, name, email)
        self.students.append(student)
        return student

    def add_course(self, course_id: int, title: str) -> Course:
        """Create a new Course and add to the list."""
        course = Course(course_id, title)
        self.courses.append(course)
        return course

    def enroll(self, student: Student, course: Course):
        """Enroll a student in a course using their respective objects."""
        student.enroll(course)

    def get_student_courses(self, student: Student):
        """Return a list of courses a student is enrolled in."""
        return student.courses

    def get_course_students(self, course: Course):
        """Return a list of students enrolled in a course."""
        return course.students

if __name__ == "__main__":
    enrollment = Enrollment()
    s1 = enrollment.add_student(1, "Alice", "alice@example.com")
    s2 = enrollment.add_student(2, "Bob", "bob@example.com")
    c1 = enrollment.add_course(101, "Mathematics")
    c2 = enrollment.add_course(102, "Physics")

    enrollment.enroll(s1, c1)
    enrollment.enroll(s1, c2)
    enrollment.enroll(s2, c1)

    print(f"{s1.name} is enrolled in {[c.title for c in enrollment.get_student_courses(s1)]}")
    print(f"{c1.title} has students {[s.name for s in enrollment.get_course_students(c1)]}")
