import sys
sys.path.append('src/puzzle')

day = "08"

import puzzle
puzzle.FetchForDay(day)


files = [
    { "key": "input", "file": f"test/day{day}.input.dat" },
    { "key": "sample", "file": f"test/day{day}.sample.dat" }
]


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        array = []
        for line in file:
            line = line.replace("\n", "")
            parts = line.split("|")
            array.append((parts[0].strip().split(" "), parts[1].strip().split(" ")))
        return array


def count(items, lengths):
    counter = 0
    for item in items:
        for i in item[1]:
            if len(i) in lengths:
                counter += 1
    return counter


def process(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        counter = count(converted, [2,3,4,7])

        result = {"file": fileInfo['key'], "counter": counter }
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        result = align2(converted)

        result = {"file": fileInfo['key'], "result": result } # 99266250
        print(f"Part II: {result}")


process(files)
# process2(files)
