# Data to be outputted
result_list = [['Jay', 3.7], ['Maebh', 4.0], ['Luna', 4.3]]
result_list.sort()
for element in result_list:
    print(f"{(result_list.index(element)+1)}. Name: {element[0]}\t Time: {element[1]}")

# Get file name which can't be blank or invalid
# Assume valid data
filename = input("Please enter a file name: ")

# Add .txt suffix
filename = filename + ".txt"

# Creates file to hold data
f = open(filename, "w+")

for element in result_list:
    f.write("100m Race")
    f.write(f"{(result_list.index(element))} Name: {element[0]} - Time:{element[1]}\n")

# Close file
f.close()
