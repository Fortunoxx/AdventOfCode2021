import sys
sys.path.append('src/puzzle')
import puzzle

day = "02"
file = {"key": "input", "file": f"src/data/day{day}.input.dat"}
puzzle.FetchForDay(day)


def solve_part1(fileInfo):
    horiz = 0
    depth = 0

    with open(fileInfo["file"]) as file:
        for line in file:
            parts = line.split(' ')
            cmd = parts[0]
            num = int(parts[1])
            if cmd == "forward":
                horiz += num
            elif cmd == "down":
                depth += num
            elif cmd == "up":
                depth -= num

    return horiz*depth


def solve_part2(fileInfo):
    horiz = 0
    depth = 0
    aim = 0

    with open(fileInfo["file"]) as file:
        for line in file:
            parts = line.split(' ')
            cmd = parts[0]
            num = int(parts[1])
            if cmd == "forward":
                horiz += num
                depth += (aim * num)
            elif cmd == "down":
                aim += num
            elif cmd == "up":
                aim -= num

    return horiz*depth