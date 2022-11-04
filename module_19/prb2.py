
def center_align(file_name):
    lines = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        print(lines)
    file.close()

    with open(file_name, "w") as file:
        for line in lines:
            file.write(line.center(len(line)+30))
    file.close()


fileName = "file.txt"
center_align(fileName)
