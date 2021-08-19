import re

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
        print("Valid file name")
