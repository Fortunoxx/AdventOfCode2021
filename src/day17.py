import sys
sys.path.append('src/puzzle')

day = "17"
file = {"key": "input", "file": f"src/data/day{day}.input.dat"}

import puzzle
puzzle.FetchForDay(day)


def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        lines = file.read()
        line = lines.split('\n', 1)[0]
        line = line.replace("target area: ", "")
        parts = line.split(", ")
        xparts = parts[0].split('=')[1].split("..")
        yparts = parts[1].split('=')[1].split("..")
        min = (int(xparts[0]), int(yparts[0]))
        max = (int(xparts[1]), int(yparts[1]))
    return (min, max)


def calcX(velocity, iteration):
    x = 0
    i = velocity[0]
    for _ in range(iteration):
        x += i
        if i > 0:
            i -= 1
    return x


def calcY(velocity, iteration):
    y = 0
    i = velocity[1]
    for _ in range(iteration):
        y += i
        i -= 1
    return y


def calcMaxIteration(velocity, coordinates):
    xmin = coordinates[0][0]
    xmax = coordinates[1][0]
    ymin = coordinates[0][1]
    ymax = coordinates[1][1]
    i = 0
    x = 0
    y = 0

    while not (x >= xmin and x <= xmax and y >= ymin and y <= ymax):
        i += 1
        x = calcX(velocity, i)
        y = calcY(velocity, i)

        if x > xmax or y < ymin: # safety first
            break
    return i


def calcFirstValidTargetX(coordinates):
    xmin = coordinates[0][0]
    xmax = coordinates[1][0]
    i = 0 
    x = 0
    while not (x >= xmin and x <= xmax):
        x = 0
        i += 1
        for j in range(i):
            x += j
    # x is the spot where we will hit the target 
    # i is the first x-velocity when this can happen 
    # -1 because zero-based
    return (x, i-1) 


def calcMaxHeight(y):
    result = 0
    for i in range(y + 1):
        result += i
    return result


def solve_part1(fileInfo):
    converted = convert(fileInfo)
    # we know the y, because this is the lower end of the target area -1
    ys = [converted[0][1], converted[1][1]]
    y = abs(sorted(ys)[0]) - 1
    maxHeight = calcMaxHeight(y)
    return maxHeight


def solve_part2(fileInfo):
    converted = convert(fileInfo)

    # the xs are in a range
    xmin = calcFirstValidTargetX(converted)[1]
    xs = [converted[0][0], converted[1][0]]
    xmax = sorted(xs)[1]

    # the ys are known: all are possible from min(y) of target area up to abs(min(y))-1
    ys = [converted[0][1], converted[1][1]]
    ymin = sorted(ys)[0]
    ymax = abs(sorted(ys)[0]) - 1

    # find max iteration, since minimum will be 1
    # this will be the "shot" that will hit the maximum x 
    # so let's calculate the maximum number of steps to get there
    iteration = calcMaxIteration((xmin, ymax), converted)
    
    minX = converted[0][0]
    maxX = converted[1][0]
    minY = converted[0][1]
    maxY = converted[1][1]
    velocities = []

    # let's try brute force
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            for i in range(1, iteration+1):
                a = calcX((x, y), i)
                b = calcY((x, y), i)
                
                # hit the target area
                if a >= minX and a <= maxX and b >= minY and b <= maxY and (x,y) not in velocities:
                    velocities.append((x, y))
                    break

                # the target area is out of reach now
                if a > maxX or b < minY:
                    break 
    return len(velocities)