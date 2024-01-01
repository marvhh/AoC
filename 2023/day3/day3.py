def get_partnumbers(grid):
    # find symbols in grid and check for digits in 3x3 dimension arrount it
    # save start locations of digits in a set.
    cs = set()
    gs = []
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            # skip char when not symbol
            if char.isdigit() or char == ".":
                continue
            if char == "*":
                gears = set()
                for cr in [r - 1, r, r + 1]:
                    for cc in [c - 1, c, c + 1]:
                        if cr < 0 or cr > len(grid) or cc < 0 or cc > len(grid[cr]) or not grid[cr][cc].isdigit():
                            continue
                        
                        while cc > 0 and grid[cr][cc - 1].isdigit():
                            cc -= 1
                        gears.add((cr,cc))
                if len(gears) == 2:
                    gs.append(gears)

            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    # skip if not digit
                    if cr < 0 or cr > len(grid) or cc < 0 or cc > len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    # find start location of digit in current row
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))
    return (cs, gs)

def calc_gear_ratio(gears):
    total = 0
    for gear in gears:
        gr = []
        for r,c in gear:
            l = []
            while c < len(grid[r]) and grid[r][c].isdigit():
                l.append(grid[r][c])
                c += 1
            gr.append(int("".join(l)))
        total += gr[0] * gr[1]
    return total

def sum_partnumbers(partnumbers):
    total = 0
    for r,c in partnumbers:
        l = []
        while c < len(grid[r]) and grid[r][c].isdigit():
            l.append(grid[r][c])
            c += 1
        total += int("".join(l))
    return total

def part1(grid):
    return sum_partnumbers(get_partnumbers(grid)[0])

def part2(grid):
    return calc_gear_ratio(get_partnumbers(grid)[1])

if __name__ == "__main__":
    input_data = "data.txt"
    with open(input_data) as f:
        grid = f.read().splitlines()
        print(part1(grid))
        print(part2(grid))
