""" Second version of storing the participant entries. This version prints the entries in order
Created by Ashlee Barrell
02/08/2021
"""


# Check for valid string
def string_checker(test):
    while True:
        to_test = test
        if to_test.isdigit():
            return True
        else:
            return False


error = "Invalid entry. Must be a name followed by time greater than 0"
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

        elif result[1][0].isdigit():
            time = float(result[1])
            if time < 1:
                print(error)

            elif result[0].isdigit():
                print(error)
                continue

            else:
                name = result[0]
                result_list.append([time, name])

        else:
            print(error)
            continue

# Checks the number of appended items in the list and gives error if 0
if len(result_list) == 0:
    print("The list of participants is empty. Please enter participants.")

# Sorts the list into the fastest to slowest times and prints the fastest 5 times
else:
    result_list.sort()
    if len(result_list) > 4:
        for num in range(0, 5):
            print(f"{(result_list.index(result_list[num]) + 1)} Name: {result_list[num][1]} - Time: {result_list[num][0]} seconds\n")
    else:
        for num in range(0, len(result_list)):
            print(f"{(result_list.index(result_list[num]) + 1)} Name: {result_list[num][1]} - Time: {result_list[num][0]} seconds\n")
