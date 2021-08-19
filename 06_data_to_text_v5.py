import re

# To be outputted
result_list = [[3.7, 'Jay'], [4.0, 'Maebh'], [4.3, 'Luna']]


has_error = "yes"
while has_error == "yes":
    global problem
    print()
    filename = input("Please enter a file name: ")
    has_error = "no"

    valid_file = "[A-Za-z0-9]"
    for letter in filename:
        if re.match(valid_file, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"

        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid file name - {}".format(problem))
    else:
        result_list.sort()
        # Add .txt suffix
        filename = filename + ".txt"

        # Creates file to hold data
        f = open(filename, "w+")

        f.write("100m Race\n")
        for element in result_list:
            f.write(f"{(result_list.index(element) + 1)} Name: {element[1]} - Time: {element[0]} seconds\n")

        # Close file
        f.close()
