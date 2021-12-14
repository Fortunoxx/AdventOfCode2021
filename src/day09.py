import sys
sys.path.append('src/puzzle')

day = "09"

import puzzle
puzzle.FetchForDay(day)


files = [
    { "key": "input", "file": f"test/day{day}.input.dat" },
    { "key": "sample", "file": f"test/day{day}.sample.dat" }
]


def findNeighbours(arrays, x, y, maxX = 9, maxY = 4):
    neighbours = []
    if x > 0:
        neighbours.append(arrays[y][x-1])
    if x < maxX:
        neighbours.append(arrays[y][x+1])
    if y > 0:
        neighbours.append(arrays[y-1][x])
    if y < maxY:
        neighbours.append(arrays[y+1][x])
    return neighbours


def findLowPoints(arrays):
    results = []
    y = 0
    for array in arrays:
        x = 0
        for a in array:
            neighbours = findNeighbours(arrays, x, y, len(array)-1, len(arrays)-1)
            x += 1
            isLowest = True
            for n in neighbours:
                if n <= a:
                    isLowest = False
                    break
            if isLowest == True:
                results.append(a)
        y += 1
    return results


def addNeighbours(coordinates, values, processed, results, maxX = 9, maxY = 4):
    x = coordinates[0]
    y = coordinates[1]

    tempCoordinates = (x - 1, y)
    if x > 0 and tempCoordinates not in processed:
        processed.append(tempCoordinates)
        tempValue = values[tempCoordinates]
        if tempValue != 9:
            results.append(tempCoordinates)
            addNeighbours(tempCoordinates, values, processed, results, maxX, maxY)
    tempCoordinates = (x + 1, y)
    if x < maxX and tempCoordinates not in processed:
        processed.append(tempCoordinates)
        tempValue = values[tempCoordinates]
        if tempValue != 9:
            results.append(tempCoordinates)
            addNeighbours(tempCoordinates, values, processed, results, maxX, maxY)
    tempCoordinates = (x, y - 1)
    if y > 0 and tempCoordinates not in processed:
        processed.append(tempCoordinates)
        tempValue = values[tempCoordinates]
        if tempValue != 9:
            results.append(tempCoordinates)
            addNeighbours(tempCoordinates, values, processed, results, maxX, maxY)
    tempCoordinates = (x, y + 1)
    if y < maxY and tempCoordinates not in processed:
        processed.append(tempCoordinates)
        tempValue = values[tempCoordinates]
        if tempValue != 9:
            results.append(tempCoordinates)
            addNeighbours(tempCoordinates, values, processed, results, maxX, maxY)
    return results

def findBasins(arrays):
    # store all processed coordinates (x,y)
    values = {}
    y = 0
    maxX = 0
    maxY = 0
    for array in arrays:
        x = 0
        for a in array:
            coordinates = (x,y)
            values[coordinates] = a
            x += 1
            if maxX < x:
                maxX = x
        y += 1
        if maxY < y:
            maxY = y

    processed = []
    results = []
    for c in values:
        if c not in processed:
            results.append(addNeighbours(c, values, processed, [], maxX - 1, maxY - 1))
    return results


def findGreatesByCount(arrays, counter = 3):
    counters = []
    for a in arrays:
        counters.append(len(a))
    return sorted(counters)[-1*counter:]


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        arrays = []
        for line in file:
            array = []
            line = line.replace("\n", "")
            for char in line:
                array.append(int(char))
            arrays.append(array)
        return arrays


def process(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        low = findLowPoints(converted)
        summe = 0
        for l in low:
            summe += l + 1

        result = {"file": fileInfo['key'], "summe": summe }
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        basins = findBasins(converted)
        top = findGreatesByCount(basins)
        result1 = 1
        for item in top:
            result1 *= item

        result = {"file": fileInfo['key'], "result1": result1 }
        print(f"Part II: {result}")


process(files)
process2(files)