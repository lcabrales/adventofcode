file_path = 'day6.txt'

with open(file_path, 'r') as file:
    lines = file.read()


def part1():
    times, distances = lines.split('\n')

    times = times.split(':')[1].split()
    distances = distances.split(':')[1].split()

    ans = 1
    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])

        count = 0
        for speed in range(0, time):
            if speed * (time - speed) > distance:
                count += 1
        ans *= count
    print(ans)

def part2():
    times, distances = lines.split('\n')

    time = int(times.split(':')[1].replace(' ', ''))
    distance = int(distances.split(':')[1].replace(' ', ''))

    ans = 0
    for speed in range(0, time):
        if speed * (time - speed) > distance:
            ans += 1
    print(ans)

part1()
part2()