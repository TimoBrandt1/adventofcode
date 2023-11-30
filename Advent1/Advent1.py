

deptIncreasePerStep = 0
increasedDept = 0
decreasedDept = 0

# Input file name
input_file = "Advent1/input.txt"

input_file_array = []
with open(input_file) as my_file:
    for line in my_file:
        input_file_array.append(line)

print (input_file_array[3])

for line in input_file_array:
    if line[1] > line[0]:
        increasedDept+=1