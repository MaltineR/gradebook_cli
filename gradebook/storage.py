import json

F_PATH = "data/gradebook.json"


def load_data():
    """Loads data from the JSON file. Returns empty data if file not found or invalid"""
    try:
        with open(F_PATH, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File not found")

    except json.JSONDecodeError:
        print("Error: JSON file is corrupted or empty")

    return {
        "students": {},
        "courses": {},
        "enrollments": []
    }
def save_data(data):
    """Saves all data to the JSON file"""
    with open(F_PATH, "w") as file:
        json.dump(data, file, indent=2)
    