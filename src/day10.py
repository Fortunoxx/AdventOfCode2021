import math
chars = { '(': ')', '<': '>', '[': ']', '{': '}' }


def isOpeningChar(openingChar, charTable):
    if openingChar in charTable.keys():
        return True
    return False


def isCorrectClosingChar(openingChar, closingChar, charTable):
    if openingChar not in charTable.keys() or closingChar not in charTable.values():
        return False
    if charTable[openingChar] != closingChar:
        return False
    return True


def isUnclosedBracket(inputArray, charTable):
    idx = 0
    workArray = inputArray[:]
    while idx >= 0:
        if idx >= len(workArray):
            return None
        if isOpeningChar(workArray[idx], charTable):
            idx += 1
            continue
        elif idx > 0 and isCorrectClosingChar(workArray[idx-1], workArray[idx], charTable):
            workArray.pop(idx)
            workArray.pop(idx-1)
            idx -= 1
        elif idx > 0 and not isCorrectClosingChar(workArray[idx-1], workArray[idx], charTable):
            return workArray[idx]
    return None


def autoCompleteChunks(inputArray, charTable):
    workArray = inputArray[:]
    autoCompletedCollection = []

    for array in workArray:
        idx = 0
        autoCompletedCharacters = []

        while idx >= 0:
            if idx >= len(array):
                break
            if isOpeningChar(array[idx], charTable):
                idx += 1
                continue
            elif idx > 0 and isCorrectClosingChar(array[idx-1], array[idx], charTable):
                array.pop(idx)
                array.pop(idx-1)
                idx -= 1
        # we now have a sanitized array
        for c in array[::-1]:
            autoCompletedCharacters.append(charTable[c])
        autoCompletedCollection.append(autoCompletedCharacters)
    return autoCompletedCollection


def separateChunks(stacks, charTable):
    unclosed = []
    incomplete = []
    for s in stacks:
        char = isUnclosedBracket(s, charTable)
        if char is not None:
            unclosed.append(char)
        else:
            incomplete.append(s)
    return (unclosed, incomplete)


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        stacks = []
        for line in file:
            array = []
            line = line.replace("\n", "")
            for char in line:
                array.append(char)
            stacks.append(array)
        return stacks


def calculateIllegalCharacterScore(characters, scoreTable = { ')': 3, ']': 57, '}': 1197, '>': 25137 }):
    mySum = 0
    for c in characters:
        mySum += scoreTable[c]
    return mySum


def calculateAutoCompletedCharacterScore(characters, scoreTable = { ')': 1, ']': 2, '}': 3, '>': 4 }):
    mySum = 0
    for u in characters:
        mySum = mySum * 5 + scoreTable[u]
    return mySum


def calculateAndSortResults(arrays):
    scores = []
    for a in arrays:
        scores.append(calculateAutoCompletedCharacterScore(a))
    idx = math.floor(len(scores) / 2)
    res = sorted(scores)[idx]
    return res


def solve_part1(fileInfo, charTable=chars):
    converted = convert(fileInfo)
    separated = separateChunks(converted, charTable)
    score = calculateIllegalCharacterScore(separated[0])
    return score

def solve_part2(fileInfo, charTable=chars):
    converted = convert(fileInfo)
    separated = separateChunks(converted, charTable)
    completed = autoCompleteChunks(separated[1], charTable)
    calculated = calculateAndSortResults(completed)
    return calculated