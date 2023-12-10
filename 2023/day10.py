
file_path = 'day10.txt'

with open(file_path, 'r') as file:
    content = file.read()

lines = content.split('\n')

pipe_dict = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'L': ['N', 'E'],
    'J': ['N', 'W'],
    '7': ['S', 'W'],
    'F': ['S', 'E'],
    'S': ['N', 'W', 'S', 'E'],
}

connections_dict = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}

def get_pos(pipe):
    for row, line in enumerate(lines):
        col = line.find(pipe)
        if col != -1:
            return row, col


def get_pipe(pos):
    try:
        return lines[pos[0]][pos[1]]
    except:
        return '.'


def are_connected(pipe1, pipe2, pos_pipe2_pipe1):
    conn_pipe1 = pipe_dict.get(pipe1, [])
    conn_pipe2 = pipe_dict.get(pipe2, [])

    opposite_direction = connections_dict.get(pos_pipe2_pipe1)
    return opposite_direction in conn_pipe2 and pos_pipe2_pipe1 in conn_pipe1


def get_main_loop():
    main_loop = [get_pos('S')]
    current_pos = main_loop[0]
    first = True
    while first or current_pos != main_loop[0]:
        north_pos = (current_pos[0] - 1, current_pos[1])
        south_pos = (current_pos[0] + 1, current_pos[1])
        east_pos = (current_pos[0], current_pos[1] + 1)
        west_pos = (current_pos[0], current_pos[1] - 1)

        current = get_pipe(current_pos)
        adjacent_pipes = {north_pos: 'N', south_pos: 'S', east_pos: 'E', west_pos: 'W'}

        connected = []
        for adjacent_pos, direction in adjacent_pipes.items():
            adjacent = get_pipe(adjacent_pos)
            if are_connected(current, adjacent, direction):
                connected.append(adjacent_pos)

        if len(connected) == 2:
            for pos in connected:
                current_pos = pos
                if not current_pos in main_loop:
                    main_loop.append(current_pos)
                    break

        first = False
    return main_loop


def is_inside_polygon(polygon, pos):
    if pos in main_loop:
        return False
    
    # ray-casting algorithm
    row, col = pos
    intersect_count = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        if ((y1 > col) != (y2 > col)) and (row < (x2 - x1) * (col - y1) / (y2 - y1) + x1):
            intersect_count += 1

    return intersect_count % 2 == 1


from shapely.geometry import Polygon, Point
def is_inside_polygon_lib(polygon, pos):
    row, col = pos
    point = Point(row, col)
    return polygon.contains(point)


main_loop = get_main_loop()
print(len(main_loop) / 2) # part 1

polygon = Polygon(main_loop)
ans = 0
for row, line in enumerate(lines):
    is_inside = False
    for col, pipe in enumerate(line):
        pos = (row, col)
        if is_inside_polygon_lib(polygon, pos):
            ans += 1

print(ans) # part 2 lib

ans = 0
for row, line in enumerate(lines):
    is_inside = False
    for col, pipe in enumerate(line):
        pos = (row, col)
        if is_inside_polygon(main_loop, pos):
            ans += 1

print(ans) # part 2 raw