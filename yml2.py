import yaml

def write_data(data, file_path, file_format):
    with open(file_path, "w") as file:
        if file_format == "yml" or file_format == "yaml":
            yaml.dump(data, file)
        else:
            raise ValueError("Unsupported file format")
