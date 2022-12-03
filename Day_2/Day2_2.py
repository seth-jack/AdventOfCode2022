input_file = open("D:\Code\AdventOfCode2022\AdventOfCode2022\Day_2\Day2_input.txt", "r")
inputs = input_file.readlines()
total_points = 0

for i in inputs:
    if i[0] == 'A':
        match i[2]:
            case 'X':
                points = 3
            case 'Y':
                points = 4
            case 'Z':
                points = 8
    elif i[0] == 'B':
        match i[2]:
            case 'X':
                points = 1
            case 'Y':
                points = 5
            case 'Z':
                points = 9
    else:
        match i[2]:
            case 'X':
                points = 2
            case 'Y':
                points = 6
            case 'Z':
                points = 7
    total_points = total_points + points

print(total_points)