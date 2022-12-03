input_file = open("D:\Code\AdventOfCode2022\AdventOfCode2022\Day_2\Day2_input.txt", "r")
inputs = input_file.readlines()
total_points = 0

for i in inputs:
    if i[0] == 'A':
        match i[2]:
            case 'X':
                points = 4
            case 'Y':
                points = 8
            case 'Z':
                points = 3
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
                points = 7
            case 'Y':
                points = 2
            case 'Z':
                points = 6
    total_points = total_points + points

print(total_points)