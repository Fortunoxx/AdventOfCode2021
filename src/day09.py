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

        result = {"file": fileInfo['key'], "summe": summe } # 1775 too high
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)

        result = {"file": fileInfo['key'], "converted": converted }
        print(f"Part II: {result}")


process(files)
# process2(files)