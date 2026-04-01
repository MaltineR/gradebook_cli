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

    def list_students(self):
        """List all students by name"""
        return sorted(self.data["students"].items(), key=lambda x: x[1]["name"])

    def list_courses(self):
        """List all courses by title"""
        return sorted(self.data["courses"].items(), key=lambda x: x[1]["title"])

    def list_enrollments(self):
        """List all enrollments by course code"""
        return sorted(self.data["enrollments"], key=lambda x: x["course_code"])
    
    def compute_average(self, student_id, course_code):
        """Calculate average grade for a student in a course"""
        for enrollment in self.data["enrollments"]:
            if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
                grades = enrollment["grades"]
                if not grades:
                    return 0
                return sum(grades) / len(grades)

    def compute_gpa(self, student_id):
        """Calculate GPA for a student"""
        averages = []
        for enrollment in self.data["enrollments"]:
            if enrollment["student_id"] == student_id:
                averages.append(self.compute_average(student_id, enrollment["course_code"]))
        if not averages:
            return 0
        return sum(averages) / len(averages)