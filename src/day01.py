import sys
sys.path.append('src/puzzle')
import puzzle

day = "01"
puzzle.FetchForDay(day)


files = [
    {"key": "input", "file": f"test/day{day}.input.dat"},
    {"key": "sample", "file": f"test/day{day}.sample.dat"}
]


def process(fileInfos):
    for fileInfo in fileInfos:
        counter = 0
        last = None

        file = open(fileInfo["file"])
        for line in file:
            number = int(line)
            if last is not None and last < number:
                counter += 1
            last = number

        file.close()

        print(f"Part I: {fileInfo['key']}: {counter}")


def process2(fileInfos):
    cnt = 3
    for fileInfo in fileInfos:
        counter = 0
        last = None
        arrays = []
        results = []

        file = open(fileInfo["file"])
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

        print(f"Part II: {fileInfo['key']}: {counter}")


process(files)
process2(files)
