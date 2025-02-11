import math
import itertools

green = 4
blue = 5
red = 6

elements = ['G'] * green + ['B'] * blue + ['R'] * red

unique_combinations = set(itertools.permutations(elements))

for combination in unique_combinations:
    formatted_combination = []
    for item in combination:
        if item == 'G':
            formatted_combination.append(1)
        elif item == 'B':
            formatted_combination.append(4)
        elif item == 'R':
            formatted_combination.append(6)
    print(tuple(formatted_combination))

print(f"Общее количество уникальных комбинаций: {total_combinations}")
total_combinations = math.factorial(green + blue + red) // (math.factorial(green) * math.factorial(blue) * math.factorial(red))
