import sys
sys.path.append('src/puzzle')

day = "06"

import puzzle
puzzle.FetchForDay(day)


files = [
    { "key": "input", "file": f"test/day{day}.input.dat" },
    { "key": "sample", "file": f"test/day{day}.sample.dat" }
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


def reproduceByNumber(input, iterations=80, resetTimer=6, creationTimer=8):
    if(iterations > 0):
        resettedElements = 0
        stateAfterCycle = {}
        for i in input:
            if i == 0:
                stateAfterCycle[creationTimer] = input[i]
                resettedElements = input[i]
            else:
                stateAfterCycle[i-1] = input[i]
        if not resetTimer in stateAfterCycle:
            stateAfterCycle[resetTimer] = resettedElements
        else:
            stateAfterCycle[resetTimer] += resettedElements
        result = reproduceByNumber(stateAfterCycle, iterations - 1)
    else:
        result = input
    return result


def aggregate(input):
    results = {}
    for i in input:
        if not i in results:
            results[i] = 1
        else:
            results[i] += 1
    return results


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
        converted = convert(fileInfo)
        aggregated = aggregate(converted)
        results = reproduceByNumber(aggregated, 256)
        result = 0
        for i in results:
            result += results[i]

        result = {"file": fileInfo['key'], "result": result }
        print(f"Part II: {result}")


process(files)
process2(files)
