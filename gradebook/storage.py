import json
import logging

F_PATH = "fake/gradebook.json"


logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data():
    """Loads data from the JSON file. Returns empty data if file not found or invalid"""
    try:
        with open(F_PATH, "r") as file:
            data = json.load(file)
            logging.info("Data loaded successfully")
            return data

    except FileNotFoundError:
        logging.error("File not found")
        print("File not found")

    except json.JSONDecodeError:
        logging.error("Error:Json file is corrupted or empty")
        print("Error: JSON file is corrupted or empty")

    return {
        "students": {},
        "courses": {},
        "enrollments": []
    }
def save_data(data):
    try:
        """Saves all data to the JSON file"""
        with open(F_PATH, "w") as file:
            json.dump(data, file, indent=2)
            logging.info("Data saved successfully")
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        print("Error saving data")
    