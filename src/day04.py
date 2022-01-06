import numpy as np

def getFieldFromLineNumber(lineNumber):
    if lineNumber >= 2:
        return (lineNumber - 2) % 5
    return 0


def convert2(fileInfo):
    with open(fileInfo["file"]) as file:
        arrays3d = []
        arrays2d = []
        numbers = []
        isFirst = True
        for line in file:
            line = line.strip()
            if isFirst:
                numbers = [int(part) for part in line.split(",")]
                isFirst = False
            elif line == "":
                if len(arrays2d) > 0:
                    arrays3d.append(arrays2d)
                arrays2d = []
            elif line != "":
                arrays2d.append([int(part) for part in line.replace("  ", " ").strip().split(" ")])
        arrays3d.append(arrays2d) # add last set
        return (numbers, arrays3d)


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


def is_winner(flattened, search=-1, size=5):
    # take chunks of <size> and check if it matches the pattern
    idx = 0
    won = False
    while idx < len(flattened):
        part = flattened[idx:idx+size]
        if len(np.where(part == search)[0]) == size:
            won = True
            break
        idx += size
    return won
    

def findLastBoard(numbers, sets):
    drawn_numbers = []
    winning_order = []

    a = np.array(sets)
    for n in numbers:
        drawn_numbers.append(n)     # keep a list of drawn numbers - maybe we don't need that later
        a = np.where(a == n, -1, a) # "remove" the drawn number

        idx = -1
        for b in a:
            idx += 1
            if idx in winning_order: 
                continue
            elif is_winner(b.flatten('F')) or is_winner(b.flatten()):
                winning_order.append(idx)
                # break

        if len(winning_order) == len(a): # we found the last winner
            # return(n, b)
            return(n, a[winning_order[-1]])
    return (None, None)


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
    leftOvers = []
    for row in item["rows"]:
        for r in row:
            if not r in numbers:
                leftOvers.append(r)

    theSum = sum(list(map(int, leftOvers)))
    theLast = int(numbers[-1])
    return theSum * theLast


def calculateSum2(item, set):
    theSum = 0
    for array in set:
        for i in array:
            if i >= 0:
                theSum += i
    return theSum * item


def solve_part1(fileInfo):
    converted = convert(fileInfo)
    results = findWinningBoard(converted)
    theResult = calculateSum(results[0], results[1])
    return theResult


def solve_part2(fileInfo):
    converted = convert2(fileInfo)
    results = findLastBoard(converted[0], converted[1])
    theResult = calculateSum2(results[0], results[1])
    return theResult

# solve_part2({"file": "test/data/day04.sample.dat"})
# solve_part2({"file": "src/data/day04.input.dat"})
