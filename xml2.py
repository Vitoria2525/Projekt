from xml.etree import ElementTree as ET

def write_data(data, file_path, file_format):
    with open(file_path, "w") as file:
        if file_format == "xml":
            xml = ET.tostring(data).decode('utf-8')
            file.write(xml)
        else:
            raise ValueError("Unsupported file format")
