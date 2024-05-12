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
