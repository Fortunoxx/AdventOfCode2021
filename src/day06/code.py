import sys
sys.path.append('src/puzzle')

day = "06"

import puzzle
puzzle.FetchForDay(day)


files = [
    { "key": "input", "file": f"src/day{day}/input.dat" },
    {"key": "sample", "file": f"src/day{day}/sample.dat"}
]


def reproduce(input, iterations=80, resetTimer=6, creationTimer=8):
    if(iterations > 0):
        newElements = 0
        stateAfterCycle = []
        for i in input:
            if i == 0: 
                i = resetTimer
                newElements += 1
            else: 
                i -= 1
            stateAfterCycle.append(i)
        for i in range(newElements):
            stateAfterCycle.append(creationTimer)
        result = reproduce(stateAfterCycle, iterations - 1)
    else:
        result = input
    return result


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        lines = file.read()
        first = lines.split('\n', 1)[0]
        parts = list(map(int, first.split(",")))
        return parts


def process(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        results = reproduce(converted)

        result = {"file": fileInfo['key'], "result": len(results) }
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        counter = 0

        file = open(fileInfo["file"])
        for line in file:
            counter += 1

        file.close()

        result = {"file": fileInfo['key']}
        print(f"Part II: {result}")


process(files)
# process2(files)
