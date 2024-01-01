import re

def update_colors(color, split_grab, values):
    if color in split_grab:
        index = split_grab.index(color)
        value = int(split_grab[index - 1])
        if values.get(color) < value:
            values[color] = value      
    return values

def get_values(line):
    values = { 'red': 0, 'green': 0, 'blue': 0 }
    game = line.split(":")[1].split(";")
    for grab in game:
        split_grab = re.split(r'[ ,\n]', grab)
        values = update_colors("red", split_grab, values)
        values = update_colors("green", split_grab, values)
        values = update_colors("blue", split_grab, values)
    return values

def check_values(values):
    max_values = { 'red': 12, 'green': 13, 'blue': 14 }
    for k in max_values:
        if max_values.get(k) < values.get(k):
            return False
    return True

def part1(lines):
        sum = 0
        for line in lines:
            game_id = int(line.split(":")[0].split()[1])
            values = get_values(line)

            if check_values(values):
                sum += game_id
        return sum
    
def part2(lines):
    sum = 0
    for line in lines:
        values = get_values(line)
        power = 1
        for i in values.values():
            power *= i
        sum += power
    return sum

if __name__ == "__main__":
    input_data = "data.txt"
    
    with open(input_data) as f:
        lines = f.readlines()
        print(part1(lines))
        print(part2(lines))
