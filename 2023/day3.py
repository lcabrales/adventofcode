import re

file_path = 'day3.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

# Part 1
symbol_positions = []
engine_numbers = []
for line_index, line in enumerate(lines):
    line = line.strip()
    symbol_positions.append([])
    
    engine_symbols = re.finditer(r'[^0-9.]', line)
    for symbol_match in engine_symbols:
        symbol_positions[line_index].append(symbol_match.start())

for line_index, line in enumerate(lines):
    line = line.strip()

    pos_to_check = []
    if 0 <= line_index - 1 < len(symbol_positions):
        symbol_pos = symbol_positions[line_index - 1]
        if symbol_pos:
            pos_to_check.extend(symbol_pos)

    if 0 <= line_index < len(symbol_positions):
        symbol_pos = symbol_positions[line_index]
        if symbol_pos:
            pos_to_check.extend(symbol_pos)

    if 0 <= line_index + 1 < len(symbol_positions):
        symbol_pos = symbol_positions[line_index + 1]
        if symbol_pos:
            pos_to_check.extend(symbol_pos)

    numbers = re.finditer(r'\d+', line)
    for number_match in numbers:
        start_pos = number_match.start()
        end_pos = number_match.end()

        for symbol_pos in pos_to_check:
            if not symbol_pos:
                continue

            if start_pos - 1 <= symbol_pos <= end_pos:
                engine_numbers.append(int(number_match.group()))

print(sum(engine_numbers)) # answer part 1

# Part 2
gear_ratio = 0
for line_index, line in enumerate(lines):
    line = line.strip()
    symbol_positions.append([])

    for char_index, char in enumerate(line):
        if char != '*':
            continue

        previous_line = ''
        if 0 <= line_index - 1 < len(lines):
            previous_line = lines[line_index - 1].strip()

        next_line = ''
        if 0 <= line_index + 1 < len(lines):
            next_line = lines[line_index + 1].strip()

        parts_count = 0
        parts = []

        numbers = re.finditer(r'\d+', previous_line)
        for number_match in numbers:
            start_pos = number_match.start()
            end_pos = number_match.end()
            
            if start_pos - 1 <= char_index <= end_pos:
                parts_count += 1
                parts.append(int(number_match.group()))

        numbers = re.finditer(r'\d+', line)
        for number_match in numbers:
            start_pos = number_match.start()
            end_pos = number_match.end()
            
            if start_pos - 1 <= char_index <= end_pos:
                parts_count += 1
                parts.append(int(number_match.group()))

        numbers = re.finditer(r'\d+', next_line)
        for number_match in numbers:
            start_pos = number_match.start()
            end_pos = number_match.end()
            
            if start_pos - 1 <= char_index <= end_pos:
                parts_count += 1
                parts.append(int(number_match.group()))
            
        if parts_count == 2:
            gear_ratio += parts[0] * parts[1]


print(gear_ratio) # answer part 2
