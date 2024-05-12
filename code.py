
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: program.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_file(input_file, output_file)
