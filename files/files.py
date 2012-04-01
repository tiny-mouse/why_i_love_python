def read_this_file():
    with open("files.py") as the_file:
        print the_file.read()

def read_this_file_line_by_line():
    with open("files.py") as the_file:
        for line in the_file.readlines():
            print line

def write_a_new_file():
    with open("new_file_from_python.txt", "w") as new_file:
        new_file.write("I am a new file!")



if __name__ == "__main__":
    read_this_file()
    read_this_file_line_by_line()
    write_a_new_file()
