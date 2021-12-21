import sys
sys.path.append('src/puzzle')

day = "14"

import puzzle
puzzle.FetchForDay(day)


files = [
    { "key": "input", "file": f"test/day{day}.input.dat" },
    { "key": "sample", "file": f"test/day{day}.sample.dat" }
]


def splitIntoParts(polymer, size = 2):
    idx = 0
    parts = []
    while idx < len(polymer) - 1:
        parts.append(polymer[idx:idx + size])
        idx += 1
    return parts


def applyInstructions(parts, instructions):
    result = ''
    First = True
    for part in parts:
        if part in instructions:
            if First:
                result += part[0] + instructions[part] + part[1]
                First = False
            else:
                result += instructions[part] + part[1]
    return result


def grow(polymer, instructions):
    splitted = splitIntoParts(polymer)
    iterated = applyInstructions(splitted, instructions)
    return iterated


def countCharacters(inputString):
    allowedCharacters = ['C', 'H', 'B', 'N']
    result = {}
    for c in allowedCharacters:
        result[c] = inputString.count(c)
    return result


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        polymer = ''
        instructions = {}
        for line in file:
            line = line.replace("\n", "")
            if '' == line:
                continue
            elif '->' in line:
                parts = line.split(" -> ")
                instructions[parts[0]] = parts[1]
            else:
                polymer = line
        return (polymer, instructions)


def process(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        polymer = converted[0]
        for _ in range(10):
            polymer = grow(polymer, converted[1])
        counted = countCharacters(polymer)

        min = sorted(counted.values())[::1][0]
        max = sorted(counted.values())[::-1][0]
        res = max - min

        result = {"file": fileInfo['key'], "result": res }
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)

        result = {"file": fileInfo['key'], "converted": converted }
        print(f"Part II: {result}")


process(files)
# process2(files)
