import json

def read_data(file_path, file_format):
    with open(file_path, "r") as file:
        if file_format == "json":
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Invalid JSON format or file does not exist.")
                return None
        else:
            print("Unsupported file format.")
            return None
