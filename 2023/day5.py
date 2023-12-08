from timeit import default_timer as timer

file_path = 'day5.txt'

with open(file_path, 'r') as file:
    lines = file.read()

sections = lines.split('\n\n')
seeds = [int(x) for x in sections[0].split('seeds:')[1].strip().split()]
others = sections[1:]
map_lines_list = []
for map_str in others:
    map_lines_list.append([[int(y) for y in x.split()] for x in map_str.split(':')[1].strip().split('\n')])


def process_seed(seed, current_ans):
    current = seed
    for map_lines in map_lines_list:
        for map_line in map_lines:
            destination_s, source_s, len = map_line
            if source_s <= current <= source_s + len:
                current = current - source_s + destination_s
                break
    return min(current_ans, current)


def part1(seeds):
    ans = max(seeds)
    for seed in seeds:
        ans = process_seed(seed, ans)
    return ans


def part2():
    seeds_pairs = sorted(list(zip(seeds[::2], seeds[1::2])), key=lambda x: x[1])
    ans = float('inf')
    for seed_s, seed_l in seeds_pairs:
        seed_s = int(seed_s)
        seed_l = int(seed_l)

        r = range(seed_s, seed_s + seed_l)
        for seed in r:
            ans = process_seed(seed, ans)
    return ans


print(part1(seeds))
print(part2())