# Integer checker - more advanced
def calculate():
    valid = False
    while not valid:
        try:
            num = float(input("Enter participant's time: "))
            if isinstance(num, float):
                valid = True
                return num
        except ValueError:
            print("That is not a number")


time = calculate()
print(f"The test number is {time}")


# Check for valid string input - eg name
def string_checker(question):
    error = "Can't be a number or blank\n"
    while True:
        to_test = input(question)
        if not to_test.isalpha():
            print(error)
            continue
        else:
            return to_test


name = string_checker("Please enter participant name: ")
