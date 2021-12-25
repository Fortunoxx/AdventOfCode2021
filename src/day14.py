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


def applyInstructions2(parts, instructions):
    result = {}
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


def grow2(splittedPolymer, instructions, elementCounters):
    newPolymerComponents = {}
    for item in splittedPolymer:
        if item in instructions:
            _middle = instructions[item]
            _first = item[:1] + _middle
            _second = _middle + item[1:]

            # add new elements
            for fs in [_first, _second]:
                if fs not in newPolymerComponents:
                    newPolymerComponents[fs] = splittedPolymer[item]
                else:
                    newPolymerComponents[fs] += splittedPolymer[item]

            # count new elements
            if not _middle in elementCounters:
                elementCounters[_middle] = splittedPolymer[item]
            else:
                elementCounters[_middle] += splittedPolymer[item]

    return (newPolymerComponents, elementCounters)


def countCharacters(inputString):
    allowedCharacters = []
    for one in range(65, 90):
        allowedCharacters.append(chr(one))
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

        polymer = converted[0]
        elementCounters = {}
        for p in polymer:
            if not p in elementCounters:
                elementCounters[p] = 1
            else:
                elementCounters[p] += 1

        parts = splitIntoParts(polymer)
        components = {}

        for part in parts:
            if part not in components:
                components[part] = 1
            else:
                components[part] += 1

        for _ in range(40):
            (components, elementCounters) = grow2(components, converted[1], elementCounters)
        
        min = sorted(elementCounters.values())[::1][0]
        max = sorted(elementCounters.values())[::-1][0]
        res = max - min

        result = {"file": fileInfo['key'], "result": res }
        print(f"Part II: {result}")

process(files)
process2(files)
