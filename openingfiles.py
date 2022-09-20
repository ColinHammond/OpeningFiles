my_file = open("requiredCS.txt", 'r')
all_lines = my_file.readlines()
for lines in all_lines:
    print(lines.upper())