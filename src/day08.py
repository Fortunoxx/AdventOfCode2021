import sys
sys.path.append('src/puzzle')

day = "08"
file = { "key": "input", "file": f"test/data/day{day}.sample.dat" }

import puzzle
puzzle.FetchForDay(day)


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


def getAllItemsByLength(items, length):
    tempresults = []
    for item in items:
        if(len(item)) == length:
            tempresults.append(item)
    return tempresults


def findPosition(numbers, counter = 1, notIn = ''):
    position = ""
    items = {}
    for n in numbers:
        for item in n:
            if item not in items:
                items[item] = 1
            else:
                items[item] += 1
    for item in items:
        if items[item] == counter:
            if len(notIn) > 0:
                if item not in notIn:
                    position = item
                    break
            else:
                position = item
                break
    return position
    

def applyMapping(dict, mapping):
    mapped = {}
    for d in dict:
        mappingTable = str.maketrans(mapping)
        mapped[d] = dict[d].translate(mappingTable)
    return mapped


def convertSignalToNumber(signals, mapping):
    converted = ''
    numbers = { 
        '0': 'abcefg', 
        '1': 'cf', 
        '2': 'acdeg', 
        '3': 'acdfg', 
        '4': 'bcdf', 
        '5': 'abdfg', 
        '6': 'abdefg', 
        '7': 'acf', 
        '8': 'abcdefg',
        '9': 'abcdfg' 
    }

    mapped = applyMapping(numbers, mapping)

    for signal in signals:
        for n in mapped:
            if len(signal) != len(mapped[n]):
                continue
            counter = 0
            for s in signal:
                if not s in mapped[n]:
                    counter = 0
                    break
                counter += 1
                if counter == len(signal):
                    converted += n
                    counter = 0
                    continue

    return converted    


def deduct2(items, signals):
    positions = { } 
    results = { }

    for item in items:
        if len(item) == 2:
            results["1"] = item
        if len(item) == 3:
            results["7"] = item
        if len(item) == 4:
            results["4"] = item
        if len(item) == 7:
            results["8"] = item

    # A
    positions['a'] = findPosition([results["1"], results["7"]], 1)

    # AE
    temp6 = getAllItemsByLength(items, 6)
    positions['e'] = findPosition(temp6, 2, results['4'])

    # ABE
    temp6.append(results["4"])
    positions['b'] = findPosition(temp6, 4, results['1'])

    # ABDE
    positions['d'] = findPosition([results['4']], 1, results["1"] + positions['b'])

    # ABCDE
    temp6 = getAllItemsByLength(items, 6)
    positions['c'] = findPosition(temp6, 2, positions['d'] + positions['e'])

    # ABCDEG
    positions['g'] = findPosition([results['8']], 1, results['4'] + positions['a'] + positions['e'])

    # ABCDEFG
    positions['f'] = findPosition([results['8']], 1, ''.join(str(positions[x]) for x in positions))

    return convertSignalToNumber(signals, positions)


def deduct(items):
    results = []
    for item in items:
        results.append(int(deduct2(item[0], item[1])))
    return results


def solve_part1(fileInfo):
    converted = convert(fileInfo)
    counter = count(converted, [2,3,4,7])

    # result = {"file": fileInfo['key'], "counter": counter }
    # print(f"Part I: {result}")
    return counter


def solve_part2(fileInfo):
    converted = convert(fileInfo)
    calculated = deduct(converted)
    summe = 0
    for c in calculated:
        summe += c

    # result = {"file": fileInfo['key'], "summe": summe }
    # print(f"Part II: {result}")
    return summe