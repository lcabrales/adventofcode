file_path = 'day4.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

sum = 0
scratchcards_total = 0
duplicates = {}
for index, line in enumerate(lines):
    line = line.split(':')
    line = line[1].split('|')
    
    winning_numbers = line[0].strip().replace('  ', ' ').split(' ')
    my_numbers = line[1].strip().replace('  ', ' ').split(' ')

    matches = set(my_numbers) & set(winning_numbers)

    # part 1
    points = 2 ** (len(matches) - 1) if matches else 0
    sum += points

    # part 2
    scratchcards = 1
    copies = duplicates.get(index)
    if copies:
        scratchcards += copies
    scratchcards_total += scratchcards
    
    for i in range(0, scratchcards):
        for match_index in range(0, len(matches)):
            key = index + match_index + 1
            value = duplicates.get(key)
            if value:
                duplicates[key] += 1
            else:
                duplicates[key] = 1

print(sum) # answer part 1
print(scratchcards_total) # answer part 2
