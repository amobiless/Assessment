
result_list = []
to_enter = input("Would you like to enter a new participant? Press 'y' if yes and 'n' if no: ").title()
while to_enter == 'Y':
    if to_enter == 'Y':
        name = input("Please enter a participant name: ")
        time = float(input("Please enter that participant's time: "))
        to_enter = input("Would you like to enter a new participant? Press 'y' if yes and 'n' if no: ").title()
        result_list.append([time, name])
        for result in result_list:
            name = result[1]
            time = result[0]
        print(result_list)
    else:

        break
