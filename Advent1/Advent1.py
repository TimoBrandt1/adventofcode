

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

for i in range(1,len(input_file_array)):
    if input_file_array[i] > input_file_array[i-1]:
        increasedDept+=1
        print(increasedDept)

print(increasedDept + 1)