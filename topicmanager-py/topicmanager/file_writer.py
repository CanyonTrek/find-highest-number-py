def write_line_to_file(line, file_path="output.txt"):
    with open(file_path, "a") as f:
        f.write(line + "\n")
