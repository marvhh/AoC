def p1_get_digits(line):
    numbers = [ch for ch in line if ch.isdigit()]
    return numbers[0] + numbers[-1]

def p2_get_digits(line):
    numbers = { "zero": "0o", "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e" }
    
    for number in numbers.keys():
        if number in line:
            line = line.replace(number, str(numbers.get(number)))
    r = [d for d in line if d.isdigit()]
    return r[0] + r[-1]


def part1(lines):
    total = 0
    for line in lines:
        total += int(p1_get_digits(line))
    return total

def part2(line):
    total = 0
    for line in lines:
        total += int(p2_get_digits(line))
    return total
    
if __name__ == "__main__":
    with open("data.txt") as f:
        lines = f.read().splitlines()
        print(part1(lines))
        print(part2(lines))
