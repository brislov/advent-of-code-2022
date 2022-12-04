import re

with open("Day 1\input.txt") as input:
    elf = 1
    calories = 0

    current_elf = 1
    current_calories = 0

    for line in input:
        line = re.sub("\s", "", line)

        if line.isdigit():
            current_calories += int(line)
        else:
            if current_calories > calories:
                elf = current_elf
                calories = current_calories

            current_elf += 1
            current_calories = 0

    print(f"Elf {elf} has {calories} calories")
    