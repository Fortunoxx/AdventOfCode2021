# import turtle
# from turtle import *


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


def solve_part1(fileInfo):
    converted = convert(fileInfo)
    folded = converted[0]
    for instruction in converted[1]:
        folded = fold(folded, instruction)
        break # stop after first iteration
    return len(folded)


def solve_part2(fileInfo):
    offset = 80
    # alternate = True
    converted = convert(fileInfo)
    folded = converted[0]
    for instruction in converted[1]:
        folded = fold(folded, instruction)

    # for coord in folded:
    #     printDot(coord, alternate, 6, offset)

    # offset -= 20
    # alternate = False
    return len(folded)


# def printDot(coordinates, UseAlternateColor = False, factor = 6, offsetBase = 80):
#     color = 'aquamarine'
#     if UseAlternateColor == True:
#         color = 'orange'

#     pen.penup()
#     offset = offsetBase * factor
#     pen.goto(coordinates[0] * factor - offset, coordinates[1] * factor * -1 - offset)
#     pen.color(color)
#     pen.dot()


# window_ = turtle.Screen()
# window_.bgcolor("darkslategray")
# window_.title("Turtle")
# pen = turtle.Turtle()
# pen.speed(0)
# turtle.tracer(20,0)
# turtle.exitonclick()