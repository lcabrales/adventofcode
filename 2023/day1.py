file_path = 'day1.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

uses_words = True # part 1 or part 2

total = 0
for line in lines:
    line = line.strip()
    first_digit = None
    last_digit = None
    
    first_index = -1
    last_index = -1
    for key, value in word_to_digit.items():
        key_index = line.find(key)
        digit_index = line.find(value) if uses_words else -1
        
        if key_index < 0 and digit_index < 0:
            continue

        index = -1
        if key_index < 0:
            index = digit_index
        elif digit_index < 0:
            index = key_index
        else:
            index = min(key_index, digit_index)

        if first_index < 0 or index < first_index:
            first_digit = value
            first_index = index

        key_index = line.rfind(key)
        digit_index = line.rfind(value)
        
        if key_index < 0 and digit_index < 0:
            continue

        index = -1
        if key_index < 0:
            index = digit_index
        elif digit_index < 0:
            index = key_index
        else:
            index = max(key_index, digit_index)

        if last_index < 0 or index > last_index:
            last_digit = value
            last_index = index

    total += int(first_digit + last_digit)

print(total) # answer