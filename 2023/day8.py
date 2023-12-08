import math

file_path = 'day8.txt'

with open(file_path, 'r') as file:
    lines = file.read()

inst, nodes_str = lines.split('\n\n')
inst = list(inst)

nodes = {}
for node_str in nodes_str.split('\n'):
    root, pointers = node_str.split('=')
    left, right = pointers.split(',')
    root = root.strip()
    left = left.replace('(', '').strip()
    right = right.replace(')', '').strip()
    nodes[root] = (left, right)


def solve_key(key, is_part1 = False):
    current = nodes[key]
    ans = 0
    while True:
        dir = inst[ans % len(inst)] # overflow
        ans += 1

        dest = current[0 if dir == 'L' else 1]
        if is_part1:
            if dest == 'ZZZ':
                return ans
        else:
            if dest.endswith('Z'):
                return ans
        current = nodes[dest]


def part1():
    print(solve_key('AAA', True)) # answer


def part2():
    current_keys = [key for key in nodes if key.endswith('A')]
    ans_l = []
    for key in current_keys:
        ans_l.append(solve_key(key))
    print(math.lcm(*ans_l)) # answer


part1()
part2()