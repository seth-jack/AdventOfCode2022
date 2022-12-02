input_file = open("Day1_input.txt", "r")
inputs = input_file.readlines()
calorie_amounts = []

i = 0
while i < len(inputs):
    if inputs[i] != '\n':
        j = 1
        total_cals = int(inputs[i])
        while i + j < len(inputs) and inputs[i + j] != '\n':
            total_cals = total_cals + int(inputs[i + j])
            j +=1
        calorie_amounts.append(total_cals)
    i += 1

print(max(calorie_amounts))