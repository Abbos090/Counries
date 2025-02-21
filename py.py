import json
from abc import ABC, abstractmethod

# 1. Abstract Class (Abstraction & Encapsulation)
class User(ABC):
    def __init__(self, user_id, name, email):
        self._user_id = user_id  # Encapsulation (private-like attribute)
        self._name = name
        self._email = email

    @abstractmethod
    def get_role(self):
        pass

    def get_info(self):
        return {
            "user_id": self._user_id,
            "name": self._name,
            "email": self._email,
            "role": self.get_role()
        }

# 2. Student Class (Inheritance)
class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self._courses = []

    def enroll_course(self, course):
        self._courses.append(course)
        course.add_student(self)

    def get_role(self):
        return "Student"

    def get_courses(self):
        return [course.get_info() for course in self._courses]

# 3. Instructor Class (Inheritance & Polymorphism)
class Instructor(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self._courses = []

    def create_course(self, course_name, course_id):
        course = Course(course_id, course_name, self)
        self._courses.append(course)
        return course

    def get_role(self):
        return "Instructor"

    def get_courses(self):
        return [course.get_info() for course in self._courses]

# 4. Course Class
class Course:
    def __init__(self, course_id, name, instructor):
        self._course_id = course_id
        self._name = name
        self._instructor = instructor
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def get_info(self):
        return {
            "course_id": self._course_id,
            "name": self._name,
            "instructor": self._instructor.get_info(),
            "students": [student.get_info() for student in self._students]
        }

# 5. Admin Class (Encapsulation & Management)
class Admin(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def get_role(self):
        return "Admin"

    def delete_course(self, lms, course_id):
        lms.remove_course(course_id)

# 6. LMS Class (Management & JSON File Handling)
class LMS:
    def __init__(self):
        self._users = []
        self._courses = []

    def add_user(self, user):
        self._users.append(user)

    def add_course(self, course):
        self._courses.append(course)

    def remove_course(self, course_id):
        self._courses = [course for course in self._courses if course._course_id != course_id]

    def save_to_json(self, filename="lms_data.json"):
        data = {
            "users": [user.get_info() for user in self._users],
            "courses": [course.get_info() for course in self._courses]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filename="lms_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                print("Loaded data:", data)  # Foydalanuvchi uchun chiqadi
        except FileNotFoundError:
            print("No previous data found.")
