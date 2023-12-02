import re

# open the file
with open('Day1.txt', 'r') as f:
	input_string = f.read().splitlines()


def Part1(input_string : str):
    first_digit_match = re.search(r'^\D*(\d)', input_string)
    last_digit_match = re.search(r'(\d)\D*$', input_string)
    return int(f"{first_digit_match.group(1)}{last_digit_match.group(1)}")

def Part2(input_string : str):
    search = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    ]
    str_to_int_mapping = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine':9,
        '1': 1, '2': 2, '3': 3, '4': 4, '5':5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    indices = []

    for item in search:
        if item in input_string:
            indices.append([input_string.index(item), str_to_int_mapping[item]])
            indices.append([input_string.rfind(item), str_to_int_mapping[item]])
    s = sorted(indices, key=lambda x: x[0])

    return int( f"{s[0][1]}{s[-1][1]}" )

sum1 = sum([Part1(item) for item in input_string])
sum2 = sum([Part2(item) for item in input_string])
print("Part 1:", sum1)
print("Part 2:", sum2)