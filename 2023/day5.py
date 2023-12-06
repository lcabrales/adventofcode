file_path = 'day5.txt'

with open(file_path, 'r') as file:
    lines = file.read()

sections = lines.split('\n\n')
seeds = [int(x) for x in sections[0].split('seeds:')[1].strip().split()]
others = sections[1:]

def part1():
    ans = max(seeds)
    for seed in seeds:
        current = seed
        for map_str in others:
            map_lines = [[int(y) for y in x.split()] for x in map_str.split(':')[1].strip().split('\n')]
            for map_line in map_lines:
                destination_s, source_s, len = map_line
                if source_s <= current <= source_s + len:
                    current = current - source_s + destination_s
                    break
                    
        ans = min(ans, current)

    print(ans) # part 1


def part2():
    seeds_pairs = list(zip(seeds[::2], seeds[1::2]))
    seeds_dict = {}
    for seed_s, seed_l in seeds_pairs:
        seeds_dict[seed_s] = seed_l

    ans = max(seeds_dict, key=lambda k: seeds_dict[k])
    for seed_s in seeds_dict.keys():
        len = seeds_dict[seed_s]
        for seed in range(seed_s, seed_s + len):
            current = seed
            for map_str in others:
                map_parts = map_str.split(':')
                map_lines = [[int(y) for y in x.split()] for x in map_parts[1].strip().split('\n')]
                
                for destination_s, source_s, length in map_lines:
                    if source_s <= current <= source_s + length:
                        current = current - source_s + destination_s
                        break
                        
            ans = min(ans, current)
    print(ans) # part 2

#part1()
part2()