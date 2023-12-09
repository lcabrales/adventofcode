file_path = 'day9.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()


def process_steps(values, ext_values):
    if values:
        ext_values.append(values[-1])

    if all(x == 0 for x in values) or not values:
        ans = 0
        start = ext_values[-1]
        for value in reversed(ext_values):
            ans += start + value
        return ans

    steps = []
    for i, value in enumerate(values):
        if i + 1 >= len(values):
            break

        value = int(value)
        next_value = int(values[i + 1])
        steps.append(next_value - value)
    
    return process_steps(steps, ext_values)


def part1():
    ans = 0
    for line in lines:
        values = line.strip().split()
        ans += process_steps([int(x) for x in values], [])
    return ans


def part2():
    ans = 0
    for line in lines:
        values = reversed(line.strip().split())
        ans += process_steps([int(x) for x in values], [])
    return ans
        

print(part1()) # answer
print(part2()) # answer
