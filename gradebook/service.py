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