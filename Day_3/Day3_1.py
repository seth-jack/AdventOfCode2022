input_file = open("D:\Code\AdventOfCode2022\AdventOfCode2022\Day_3\Day3_input.txt", "r")
inputs = input_file.readlines()
matched_letters = []
priority = 0

for i in inputs:
    i = i.replace('\n', '')
    first_half = i[0:int(len(i) / 2)]
    second_half = i[int(len(i) / 2):int(len(i))]
    for letter in first_half:
        comparison = second_half.find(letter)
        if comparison != -1:
            matched_letters.append(letter)
            break

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for ml in matched_letters:
    value = alphabet.find(ml.lower()) + 1
    if ml != ml.lower():
        value = value + 26
    priority = priority + value

print(priority)