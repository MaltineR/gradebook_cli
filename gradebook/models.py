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
    
""" This is a Course Class """

class course :
    def __init__(self, code, title) :
        """ It takes Course Code and Course Title """
        if not code or not title :
            raise ValueError ("Code and title must be non-empty")
        self.code=code
        self.title=title
    def __str__ (self):
        return f"Course (code={self.code}, title={self.title})"

