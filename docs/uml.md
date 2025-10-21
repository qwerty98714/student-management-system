# UML-диаграмма для системы управления студентами

Этот документ содержит диаграмму классов UML для системы управления студентами. Диаграмма использует синтаксис Mermaid, поддерживаемый GitHub, для отображения классов и их взаимотношений.

```mermaid
classDiagram
    class Student {
        +id: int
        +name: str
        +enroll(course: Course)
        +drop(course: Course)
        +list_courses()
    }
    class Course {
        +id: int
        +name: str
        +add_student(student: Student)
        +remove_student(student: Student)
        +list_students()
    }
    class Enrollment {
        +enroll(student: Student, course: Course)
        +get_courses(student: Student)
        +get_students(course: Course)
    }
    Student "1" <-- "0..*" Enrollment
    Course "1" <-- "0..*" Enrollment
```
