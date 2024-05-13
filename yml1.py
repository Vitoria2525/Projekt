import yaml

def read_data(file_path, file_format):
    with open(file_path, "r") as file:
        if file_format == "yml" or file_format == "yaml":
            try:
                data = yaml.load(file)
                return data
            except yaml.YAMLError as e:
                print(f"Error while parsing YAML file: {e}")
                return None
        else:
            raise ValueError("Unsupported file format")
