from gradebook.storage import load_data, save_data


class GradebookService:
    """This class handles all operations for the grades system"""

    def __init__(self):
        self.data = load_data()

    def save(self):
        save_data(self.data)

    def add_student(self, name):
        """Add a new student"""
        new_id = len(self.data["students"]) + 1
        self.data["students"][str(new_id)] = {"name": name}
        self.save()
        return new_id

    def add_course(self, code, title):
        """Add a new course by code and title"""
        self.data["courses"][code] = {"title": title}
        self.save()

    def enroll_student(self, student_id, course_code):
        """Enroll a student in a course"""
        self.data["enrollments"].append({
            "student_id": student_id,
            "course_code": course_code,
            "grades": []
        })
        self.save()

    def add_grade(self, student_id, course_code, grade):
        """Add a grade to a student by checking student id and course code"""
        for enrollment in self.data["enrollments"]:
            if enrollment ["student_id"] == student_id and enrollment["course_code"] == course_code:
                enrollment["grades"].append(grade)
                self.save()