import sys
sys.path.append('src/puzzle')

day = "11"

import numpy as np
import puzzle
puzzle.FetchForDay(day)


files = [
    { "key": "input", "file": f"test/day{day}.input.dat" },
    { "key": "sample", "file": f"test/day{day}.sample.dat" }
]


def increaseAdjacent(coordinates, array, maxX, maxY):
    for d in directions:
        x = coordinates[0] + d[0]
        y = coordinates[1] + d[1]
        if x >= 0 and x < maxX and y >= 0 and y < maxY and array[y][x] != 0:
            array[y][x] += 1


def increaseAndFlash(array, totalFlashCounter, energyGain = 1, minFlashLevel = 10):
    converted = np.array(array)
    modified = converted + energyGain

    # increase adjacent objects by number of neighbours with 9 or more
    hasFlashed = True
    localFlashCounter = 0
    while hasFlashed:
        hasFlashed = False
        y = 0
        for row in modified:
            x = 0
            for val in modified[y]:
                if val >= 10:
                    hasFlashed = True
                    totalFlashCounter += 1
                    localFlashCounter += 1
                    increaseAdjacent((x, y), modified, len(row), len(modified))
                    modified[y][x] = 0
                x += 1
            y += 1

    z = np.where(modified >= minFlashLevel, 0, modified)
    return (z, totalFlashCounter, localFlashCounter)


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        stacks = []
        for line in file:
            array = []
            line = line.replace("\n", "")
            for char in line:
                array.append(int(char))
            stacks.append(array)
        return stacks


def process(fileInfos, counter = 10):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        totalFlashCounter = 0
        for _ in range(counter):
            (converted, totalFlashCounter, _) = increaseAndFlash(converted, totalFlashCounter)

        result = {"file": fileInfo['key'], "score": totalFlashCounter, "array": converted }
        print(f"Part I: {result}")


def process2(fileInfos, maxIterations):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        numberOfFlashesWhenAllAreActiveSimultaneously = len(converted) * len(converted[0]) # not so nice I know
        allAreFlashing = False
        iteration = 0
        totalFlashCounter = 0
        while not allAreFlashing and iteration < maxIterations: # fallback to prevent infinite loop
            iteration += 1
            (converted, totalFlashCounter, numberFlashingCurrently) = increaseAndFlash(converted, totalFlashCounter)
            if numberFlashingCurrently == numberOfFlashesWhenAllAreActiveSimultaneously:
                allAreFlashing = True
                break

        result = {"file": fileInfo['key'], "iteration": iteration, "array": converted }
        print(f"Part II: {result}")

# declare a static array of coordinates pointing to neighbours
directions = []
for a in range(3):
    for b in range(3):
        x = a-1
        y = b-1
        if (x,y) != (0,0):
            directions.append((x, y))

process(files, 100)
process2(files, 500)