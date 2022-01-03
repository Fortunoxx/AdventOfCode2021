import sys
sys.path.append('src/puzzle')

day = "20"

import puzzle
puzzle.FetchForDay(day)


file = {"key": "input", "file": f"src/data/day{day}.input.dat"}


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        bins = []
        for line in file:
            line = line.replace("\n", "")
            binary = ''
            num_of_bits = 4
            for char in line:
                binary += bin(int(char, 16))[2:].zfill(num_of_bits)
            bins.append((binary, line))
        return bins


def solve_part1(fileInfo):
    converted = convert(fileInfo)

    result = {"file": fileInfo['key'], "converted": converted }
    print(f"Part I: {result}")


def solve_part2(fileInfo):
    converted = convert(fileInfo)
    converted = convert(fileInfo)

    result = {"file": fileInfo['key'], "converted": converted }
    print(f"Part II: {result}")


print(f"Part 1: {solve_part1(file)}")
print(f"Part 2: {solve_part2(file)}")
