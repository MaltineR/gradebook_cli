import unittest
from gradebook.service import add_student, add_grade, compute_average


class Test(unittest.TestCase):

    def test_add_student(self):
        data = {"students": {}, "courses": {}, "enrollments": []}
        data, student_id = add_student(data, "Maltine")
        self.assertIn(str(student_id), data["students"])

    def test_add_grade(self):
        data = {
            "students": {"1": {"name": "Maltine"}},
            "courses": {"TECH1": {"title": "Python"}},
            "enrollments": [
                {"student_id": 1, "course_code": "TECH1", "grades": []}
            ]
        }
        data = add_grade(data, 1, "TECH1", 90)
        self.assertIn(90, data["enrollments"][0]["grades"])

    def test_compute_average(self):
        data = {
            "students": {"1": {"name": "Maltine"}},
            "courses": {"TECH2": {"title": "OOP"}},
            "enrollments": [
                {"student_id": 1, "course_code": "TECH2", "grades": [80, 100]}
            ]
        }
        avg = compute_average(data, 1, "TECH2")
        self.assertEqual(avg, 90)

    def test_compute_average_wrong_course(self):
        """ Failing case: returns 0 for non existent course"""
        data = {
            "students": {"1": {"name": "Maltine"}},
            "courses": {"TECH1": {"title": "Python"}},
            "enrollments": [
                {"student_id": 1, "course_code": "TECH1", "grades": [80, 90]}
            ]
        }
        avg = compute_average(data, 1, "JAVA")
        self.assertEqual(avg, 0)


if __name__ == "__main__":
    unittest.main()