import json

FILE_NAME = "contacts.json"

def load_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_to_file(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
