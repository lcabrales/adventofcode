import re

file_path = 'day2.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

total_part1 = 0
total_part2 = 0

for line in lines:
    line = line.strip()

    is_game_possible = True

    game_id = int(re.search(r'\d+', line).group()) # search for first digit

    max_red = 0
    max_green = 0
    max_blue = 0

    line = line.split(':')[1]
    cube_sets = line.split(';')
    for cube_set in cube_sets:
        cubes = cube_set.split(',')
        
        for cube in cubes:
            cube = cube.strip()
            amount = int(re.search(r'\d+', cube).group())
            
            if 'red' in cube:
                if amount > MAX_RED_CUBES:
                    is_game_possible = False
                max_red = max(amount, max_red)

            if 'green' in cube:
                if amount > MAX_GREEN_CUBES:
                    is_game_possible = False
                max_green = max(amount, max_green)

            if 'blue' in cube:
                if amount > MAX_BLUE_CUBES:
                    is_game_possible = False
                max_blue = max(amount, max_blue)
                
    
    if is_game_possible:
        total_part1 += game_id

    max_power = max_red * max_green * max_blue
    total_part2 += max_power 

print(total_part1) # answer part 1
print(total_part2) # answer part 2