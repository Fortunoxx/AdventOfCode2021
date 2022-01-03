import sys
sys.path.append('src/puzzle')

day = "04"
file = {"key": "input", "file": f"src/data/day{day}.input.dat"}

import puzzle
puzzle.FetchForDay(day)


def getFieldFromLineNumber(lineNumber):
    if lineNumber >= 2:
        return (lineNumber - 2) % 5
    return 0


def convert(fileInfo, blockSize=6):
    with open(fileInfo["file"]) as file:
        id = 0
        isFirst = True
        lineCounter = 0
        numbers = []
        sets = []
        rows = []
        columns = []

        for line in file:
            line = line.replace("\n", "").replace("  ", " ").strip()

            if isFirst:
                isFirst = False
                numbers = line.split(",")
            elif line != "":
                rows.append(line.split(" "))

            if lineCounter > 0 and lineCounter % blockSize == 0:
                size = len(rows)
                i = 0
                while i < size:
                    col = []
                    for a in rows[len(rows)-(blockSize-1):]:
                        col.append(a[i])
                    columns.append(col)
                    i += 1

                sets.append({"id": id, "rows": rows, "columns": columns})
                id += 1
                rows = []
                columns = []
            lineCounter += 1

    return {"numbers": numbers, "sets": sets}


def findWinningBoard(converted, amount=5):
    drawnNumbers = []
    for number in converted["numbers"]:
        drawnNumbers.append(number)
        if(len(drawnNumbers) < amount):
            continue

        for item in converted["sets"]:
            for row in item["rows"]:
                if findMatches(drawnNumbers, row):
                    return (item, drawnNumbers)
            for col in item["columns"]:
                if findMatches(drawnNumbers, col):
                    return (item, drawnNumbers)
    return (None, None)


def findLastBoard(converted, amount=5):
    drawnNumbers = []
    winningOrder = []

    for number in converted["numbers"]:
        drawnNumbers.append(number)
        if(len(drawnNumbers) < amount):
            continue

        for item in converted["sets"]:
            if item["id"] in winningOrder:
                continue

            for row in item["rows"]:
                if findMatches(drawnNumbers, row):
                    winningOrder.append(item["id"])
                    break
            for col in item["columns"]:
                if findMatches(drawnNumbers, col):
                    winningOrder.append(item["id"])
                    break

            if (len(winningOrder) == len(converted["sets"])):
                return (item, drawnNumbers)

    return None


def findMatches(numbers, arrayToCheck, amount=5):
    matches = 0
    for n in numbers:
        for item in arrayToCheck:
            if n == item:
                matches += 1
                if matches >= amount:
                    return True
    return False


def calculateSum(item, numbers):
    if item is None:
        return -1

    leftOvers = []
    for row in item["rows"]:
        for r in row:
            if not r in numbers:
                leftOvers.append(r)

    theSum = sum(list(map(int, leftOvers)))
    theLast = int(numbers[-1])
    return theSum * theLast


def solve_part1(fileInfo):
    converted = convert(fileInfo)
    results = findWinningBoard(converted)
    theResult = calculateSum(results[0], results[1])
    return theResult


def solve_part2(fileInfo):
    converted = convert(fileInfo)
    results = findLastBoard(converted)
    theResult = calculateSum(results[0], results[1])
    return theResult


print(f"Part 1: {solve_part1(file)}")
print(f"Part 2: {solve_part2(file)}")
