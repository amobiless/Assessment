""" First version of a name and number checker to ensure valid input
Created by Ashlee Barrell
02/08/2021
"""


# Check for valid string
def string_checker(test):
    while True:
        to_test = test
        if to_test.isalpha():
            return True
        else:
            return False


error = "Invalid entry. Must be a name followed by time"
result = ""
result_list = []
while result != "X":
    result = input("Please enter the name followed by the time or press 'x' to exit: ").title()
    if result == "X":
        break
    else:
        result = result.strip()
        result = result.split()

        if len(result) < 2:
            print(error)
            continue

        elif result[-1][0].isdigit():
            time = result[-1]

            if result[0].isdigit():
                print(error)
                continue

            else:
                name = result[0]

            print(f"Name: = {name} Time = {time} seconds")
            result_list.append(name + ' ' + time)
            print(result_list)
        else:
            print(error)
            continue

