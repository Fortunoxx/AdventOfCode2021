import sys
sys.path.append('src/puzzle')

day = "07"
file = {"key": "input", "file": f"src/data/day{day}.input.dat"}

import puzzle
puzzle.FetchForDay(day)


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        lines = file.read()
        first = lines.split('\n', 1)[0]
        parts = list(map(int, first.split(",")))
        return parts


def align(positions):
    # sort array, determine max horizontal position - this will be the max (min will always be 0)
    sort = sorted(positions)
    max = sort[-1]
    diff = None
    for i in range(max):
        totalDifference = 0
        for pos in sort:
            totalDifference += abs(pos-i)
        if diff is None or totalDifference < diff: 
            diff = totalDifference
    return diff


def align2(positions):
    # sort array, determine max horizontal position - this will be the max (min will always be 0)
    sort = sorted(positions)
    max = sort[-1]
    diff = None

    # create a dictionary with enumerate to simply lookup fuel costs by index, this will be a dictionary from 0 to <max>
    fuelCosts = {}
    aggregated = 0
    for idx, value in (enumerate(range(max+1))):
        aggregated += value
        fuelCosts[idx] = aggregated

    for i in range(max):
        totalDifference = 0
        for pos in sort:
            totalDifference += fuelCosts[abs(pos-i)]
        if diff is None or totalDifference < diff: 
            diff = totalDifference
    return diff 
    

def solve_part1(fileInfo):
    converted = convert(fileInfo)
    result = align(converted)
    return result


def solve_part2(fileInfo):
    converted = convert(fileInfo)
    result = align2(converted)
    return result


print(f"Part 1: {solve_part1(file)}")
print(f"Part 2: {solve_part2(file)}")
