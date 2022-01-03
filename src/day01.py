import sys
sys.path.append('src/puzzle')
import puzzle

day = "01"
file = {"key": "input", "file": f"src/data/day{day}.input.dat"}
puzzle.FetchForDay(day)


def solve_part1(fileInfo):
    counter = 0
    last = None

    with open(fileInfo["file"]) as file:
        for line in file:
            number = int(line)
            if last is not None and last < number:
                counter += 1
            last = number

    return counter


def solve_part2(fileInfo):
    cnt = 3
    counter = 0
    last = None
    arrays = []
    results = []

    with open(fileInfo["file"]) as file:
        for line in file:
            number = int(line)
            arrays.append([])

            for array in arrays:
                if (len(array) < cnt):
                    array.append(number)

        file.close()

        l = len(arrays) - 1

        # remove last 2 arrays - incomplete
        arrays.pop(l)
        arrays.pop(l - 1)

        for a in arrays:
            s = 0
            for i in a:
                s += i
            results.append(s)

        for number in results:
            if last is not None and last < number:
                counter += 1
            last = number

    return counter


print(f"Part 1: {solve_part1(file)}")
print(f"Part 2: {solve_part2(file)}")