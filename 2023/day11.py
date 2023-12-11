file_path = 'day11.txt'

with open(file_path, 'r') as file:
    content = file.read()

lines = content.split('\n')

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_sum(lines, exp_val):
    x_exp_indices = []
    for xi in range(len(lines[0])):
        column = [line[xi] for line in lines]
        if all(char == '.' for char in column):
            x_exp_indices.append(xi)
            
    y_exp_indices = []
    for yi, line in enumerate(lines):
        if all(char == '.' for char in line):
            y_exp_indices.append(yi)

    galaxies = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '#':
                continue
            nx = x
            for exp_x in x_exp_indices:
                if x > exp_x:
                    nx += exp_val - 1
            ny = y
            for exp_y in y_exp_indices:
                if y > exp_y:
                    ny += exp_val - 1
            galaxies.append((nx, ny))

    ans = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            x1, y1 = galaxy1
            x2, y2 = galaxy2
            ans += distance(x1, y1, x2, y2)

    return ans // 2

print(find_sum(lines, 2)) # part 1
print(find_sum(lines, 1_000_000)) # part 2