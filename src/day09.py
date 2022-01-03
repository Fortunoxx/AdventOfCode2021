import sys
# import turtle
# from turtle import *

sys.path.append('src/puzzle')

day = "09"
file = {"key": "input", "file": f"src/data/day{day}.input.dat"}

import puzzle
puzzle.FetchForDay(day)


def findNeighbours(arrays, x, y, maxX = 9, maxY = 4):
    neighbours = []
    if x > 0:
        neighbours.append(arrays[y][x-1])
    if x < maxX:
        neighbours.append(arrays[y][x+1])
    if y > 0:
        neighbours.append(arrays[y-1][x])
    if y < maxY:
        neighbours.append(arrays[y+1][x])
    return neighbours


def findLowPoints(arrays):
    results = []
    y = 0
    for array in arrays:
        x = 0
        for a in array:
            neighbours = findNeighbours(arrays, x, y, len(array)-1, len(arrays)-1)
            x += 1
            isLowest = True
            for n in neighbours:
                if n <= a:
                    isLowest = False
                    break
            if isLowest == True:
                results.append(a)
        y += 1
    return results


def printDot(coordinates, UseAlternateColor = False, factor = 6, offsetBase = 80):
    color = 'aquamarine'
    if UseAlternateColor == True:
        color = 'sienna'

    pen.penup()
    offset = offsetBase * factor
    pen.goto(coordinates[0] * factor - offset, coordinates[1] * factor - offset)
    pen.color(color)
    pen.dot()


def addNeighbours(coordinates, values, processed, results, maxX = 9, maxY = 4):
    x = coordinates[0]
    y = coordinates[1]

    if coordinates not in processed:
        processed.append(coordinates)
        tempValue = values[coordinates]
        if tempValue != 9:
            # printDot(coordinates)
            results.append(coordinates)
            addNeighbours(coordinates, values, processed, results, maxX, maxY)
        # else:
        #     printDot(coordinates, True)

    tempCoordinates = (x - 1, y)
    if x > 0 and tempCoordinates not in processed:
        processed.append(tempCoordinates)
        tempValue = values[tempCoordinates]
        if tempValue != 9:
            # printDot(tempCoordinates)
            results.append(tempCoordinates)
            addNeighbours(tempCoordinates, values, processed, results, maxX, maxY)
        # else:
        #     printDot(tempCoordinates, True)
    tempCoordinates = (x + 1, y)
    if x < maxX and tempCoordinates not in processed:
        processed.append(tempCoordinates)
        tempValue = values[tempCoordinates]
        if tempValue != 9:
            # printDot(tempCoordinates)
            results.append(tempCoordinates)
            addNeighbours(tempCoordinates, values, processed, results, maxX, maxY)
        # else:
        #     printDot(tempCoordinates, True)
    tempCoordinates = (x, y - 1)
    if y > 0 and tempCoordinates not in processed:
        processed.append(tempCoordinates)
        tempValue = values[tempCoordinates]
        if tempValue != 9:
            # printDot(tempCoordinates)
            results.append(tempCoordinates)
            addNeighbours(tempCoordinates, values, processed, results, maxX, maxY)
        # else:
        #     printDot(tempCoordinates, True)
    tempCoordinates = (x, y + 1)
    if y < maxY and tempCoordinates not in processed:
        processed.append(tempCoordinates)
        tempValue = values[tempCoordinates]
        if tempValue != 9:
            # printDot(tempCoordinates)
            results.append(tempCoordinates)
            addNeighbours(tempCoordinates, values, processed, results, maxX, maxY)
        # else:
        #     printDot(tempCoordinates, True)
    return results

def findBasins(arrays):
    # store all processed coordinates (x,y)
    values = {}
    y = 0
    maxX = 0
    maxY = 0
    for array in arrays:
        x = 0
        for a in array:
            coordinates = (x,y)
            values[coordinates] = a
            x += 1
            if maxX < x:
                maxX = x
        y += 1
        if maxY < y:
            maxY = y

    processed = []
    results = []
    for c in values:
        if c not in processed:
            results.append(addNeighbours(c, values, processed, [], maxX - 1, maxY - 1))
    return results


def findGreatesByCount(arrays, counter = 3):
    counters = []
    for a in arrays:
        counters.append(len(a))
    return sorted(counters)[-1*counter:]


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        arrays = []
        for line in file:
            array = []
            line = line.replace("\n", "")
            for char in line:
                array.append(int(char))
            arrays.append(array)
        return arrays


def solve_part1(fileInfo):
    converted = convert(fileInfo)
    low = findLowPoints(converted)
    summe = 0
    for l in low:
        summe += l + 1
    return summe


def solve_part2(fileInfo):
    converted = convert(fileInfo)
    basins = findBasins(converted)
    top = findGreatesByCount(basins)
    result1 = 1
    for item in top:
        result1 *= item
    return result1


# window_ = turtle.Screen()
# window_.bgcolor("darkslategray")
# window_.title("Turtle")
# pen = turtle.Turtle()
# pen.speed(0)
# turtle.tracer(20,0)

print(f"Part 1: {solve_part1(file)}")
print(f"Part 2: {solve_part2(file)}")
# turtle.exitonclick()
