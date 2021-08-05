result_list = [
    "jay 4.30",
    "harry 4:30"
]

for participant in result_list:
    participant = participant.split()
    name = participant[0].title()
    time = participant[1]
    if name.isspace() or name.isdigit():
        print("Please enter a valid name")
    if time.isdigit():
        participant.remove(participant[1])
    product = " ".join([str(word) for word in participant])

    print(f"Name: = {name}, Time = {time} seconds")
