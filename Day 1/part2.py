import re

with open("Day 1\input.txt") as input:
    calories_sums = list()
    current_calories = 0

    for line in input:
        line = re.sub("\s", "", line)

        if line.isdigit():
            current_calories += int(line)
        else:
            calories_sums.append(current_calories)
            current_calories = 0

    calories_sums.sort(reverse=True)

    print(f"Total calories from the top three Elves is {sum(calories_sums[0:3])}")
    