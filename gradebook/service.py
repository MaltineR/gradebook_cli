from gradebook.storage import load_data, save_data


class GradebookService:
    """This class handles all operations for the grades system"""

    def __init__(self):
        self.data = load_data()

    def save(self):
        save_data(self.data)