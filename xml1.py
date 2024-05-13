from xml.etree import ElementTree as ET 

def read_data(file_path, file_format):
    with open(file_path, "r") as file:
        if file_format == "xml":
            data = ET.parse(file).getroot()
        else:
            raise ValueError("Unsupported file format")
    return data
