import json

def write_data(data, file_path, file_format):
    with open(file_path, "w") as file:
        if file_format == "json":
            json.dump(data, file)
        else:
            raise ValueError("Unsupported file format")
