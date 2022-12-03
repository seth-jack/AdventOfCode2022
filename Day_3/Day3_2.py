input_file = open("D:\Code\AdventOfCode2022\AdventOfCode2022\Day_3\Day3_input.txt", "r")
inputs = input_file.readlines()
matched_letters = []
priority = 0

i = 0
while i < len(inputs):
    elf_1 = inputs[i]
    elf_2 = inputs[i + 1]
    elf_3 = inputs[i + 2]
    for letter in elf_1:
        if (elf_2.find(letter) != -1) and (elf_3.find(letter) != -1):
            matched_letters.append(letter)
            break
    i = i + 3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for ml in matched_letters:
    value = alphabet.find(ml.lower()) + 1
    if ml != ml.lower():
        value = value + 26
    priority = priority + value

print(priority)