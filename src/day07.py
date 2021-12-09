import sys
sys.path.append('src/puzzle')

day = "07"

import puzzle
puzzle.FetchForDay(day)


files = [
    { "key": "input", "file": f"test/day{day}.input.dat" },
    { "key": "sample", "file": f"test/day{day}.sample.dat" }
]


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
    current = None
    for i in range(max):
        totalDifference = 0
        for pos in sort:
            totalDifference += abs(pos-i)
        if diff is None or totalDifference < diff: 
            diff = totalDifference
            current = i
    return (diff, current)

def process(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        result = align(converted)

        result = {"file": fileInfo['key'], "result": result }
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        result = {"file": fileInfo['key'], "result": "todo" }
        print(f"Part II: {result}")


process(files)
# process2(files)
