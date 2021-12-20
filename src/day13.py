import sys
sys.path.append('src/puzzle')

day = "13"

import puzzle
puzzle.FetchForDay(day)


files = [
    { "key": "input", "file": f"test/day{day}.input.dat" },
    { "key": "sample", "file": f"test/day{day}.sample.dat" }
]


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        coordinates = []
        foldingInstructions = []
        for line in file:
            line = line.replace("\n", "")
            if ',' in line:
                parts = line.split(",")
                coordinates.append((int(parts[0]), int(parts[1])))
            elif 'fold along' in line:
                parts = line.split(' ')
                interestingParts = parts[2].split('=')
                foldingInstructions.append((interestingParts[0], int(interestingParts[1])))
        return (coordinates, foldingInstructions)


def fold(data, foldingInstructions):
    folded = []
    axis = foldingInstructions[0]
    number = foldingInstructions[1]

    for d in data:
        if axis == 'y':
            value = d[1]
            if value < number and d not in folded:
                folded.append(d)
            elif value > number:
                newCoordinates = (d[0], number + number - value )
                if newCoordinates not in folded:
                    folded.append(newCoordinates)
        elif axis == 'x':
            value = d[0]
            if value < number and d not in folded:
                folded.append(d)
            elif value > number:
                newCoordinates = (number + number - value, d[1])
                if newCoordinates not in folded:
                    folded.append(newCoordinates)
    return folded


def process(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        folded = converted[0]
        for instruction in converted[1]:
            folded = fold(folded, instruction)
            break # stop after first iteration

        result = {"file": fileInfo['key'], "folded": len(folded) } # 837 too high
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)

        result = {"file": fileInfo['key'], "converted": converted }
        print(f"Part II: {result}")


process(files)
# process2(files)