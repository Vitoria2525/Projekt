import json
import yaml
from xml.etree import ElementTree as ET

def read_data(file_path, file_format):
    with open(file_path, "r") as file:
        if file_format == "json":
            data = json.load(file)
        elif file_format == "yml" or file_format == "yaml":
            data = yaml.load(file)
        elif file_format == "xml":
            data = ET.parse(file).getroot()
        else:
            raise ValueError("Unsupported file format")
    return data

def write_data(data, file_path, file_format):
    with open(file_path, "w") as file:
        if file_format == "json":
            json.dump(data, file)
        elif file_format == "yml" or file_format == "yaml":
            yaml.dump(data, file)
        elif file_format == "xml":
            xml = ET.tostring(data).decode('utf-8')
            file.write(xml)
        else:
            raise ValueError("Unsupported file format")

def convert_file(input_file, output_file):
    input_format = input_file.split('.')[-1]
    output_format = output_file.split('.')[-1]
    input_data = read_data(input_file,input_format)
    write_data(input_data, output_file, output_format)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: program.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_file(input_file, output_file)
