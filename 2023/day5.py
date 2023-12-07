from timeit import default_timer as timer
from datetime import timedelta

file_path = 'day5.txt'

with open(file_path, 'r') as file:
    lines = file.read()

sections = lines.split('\n\n')
seeds = [int(x) for x in sections[0].split('seeds:')[1].strip().split()]
others = sections[1:]

def process_seed(seed, current_ans):
    current = seed
    for map_str in others:
        map_lines = [[int(y) for y in x.split()] for x in map_str.split(':')[1].strip().split('\n')]
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
    seeds_pairs = list(zip(seeds[::2], seeds[1::2]))
    ans = float('inf')
    for seed_s, seed_l in seeds_pairs:
        seed_s = int(seed_s)
        seed_l = int(seed_l)
        
        # improve performance?
        div_by = 100
        ranges = []
        for div in range(div_by):
            f1 = seed_l // div_by * div
            if div == div_by - 1:
                f2 = seed_l
            else:
                f2 = seed_l // div_by * (div + 1)
            ranges.append(range(f1, f2))

        print(ranges)
        for range_val in ranges:
            start = timer()
            for val in range_val:
                seed = val + seed_s

                if val % 1_000_000 == 0:
                    end = timer()
                    print(f"trying seed: {seed} - {timedelta(seconds=end-start)}")
                    start = timer()

                ans = process_seed(seed, ans)
    return ans

print(part1(seeds))
print(part2())