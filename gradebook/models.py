"""This is a Student Class """
class student:
    def __init__(self, student_id, name):
        """ Unique Student ID and Student name non-empty"""
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a string and non-empty")
        self.id = student_id
        self.name = name

    def __str__(self):
        return f"Student(id={self.id}, name={self.name})"
