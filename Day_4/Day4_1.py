input_file = open("D:\Code\AdventOfCode2022\AdventOfCode2022\Day_4\Day4_input.txt", "r")
inputs = input_file.readlines()
fully_contained_ranges = 0


i = 0
while i < len(inputs):
    formatted_input = str(inputs[i]).replace('\n','')
    one,two = formatted_input.split(',')
    a,b = one.split('-')
    c,d = two.split('-')
    a,b,c,d = [int(x) for x in [a,b,c,d]]
    if a >= c and b <= d or a <= c and b >= d:
        fully_contained_ranges += 1
    i += 1

print(fully_contained_ranges)