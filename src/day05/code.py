import sys
sys.path.append('src/puzzle')
import puzzle

day = "05"
puzzle.FetchForDay(day)

files = [
    {"key": "input", "file": f"src/day{day}/input.dat"},
    {"key": "sample", "file": f"src/day{day}/sample.dat"}
]


def convert(fileInfo, horizontalOrVerticalOnly=True):
    coordinates = []
    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" -> ")
            start = (int(parts[0].split(",")[0]), int(parts[0].split(",")[1]))
            end = (int(parts[1].split(",")[0]), int(parts[1].split(",")[1]))
            if horizontalOrVerticalOnly and (start[0] == end[0] or start[1] == end[1]):
                coordinates.append((start, end))
            else:
                coordinates.append((start, end))
    return coordinates


def calculateWaypoints2(coordinates):
    waypoints = []

    for item in coordinates:
        x1 = item[0][0]
        y1 = item[0][1]
        x2 = item[1][0]
        y2 = item[1][1]

        x = 0
        y = 0

        if(x1 < x2):
            x = 1
        elif (x1 > x2):
            x = -1
        if(y1 < y2):
            y = 1
        elif (y1 > y2):
            y = -1

        step = (x,y)

        current = item[0]
        end = item[1]

        while current != end:
            waypoints.append(current)
            current = (current[0] + step[0], current[1] + step[1])
        waypoints.append(current)

    return (waypoints)


def calculateWaypoints(coordinates):
    waypoints = []

    for item in coordinates:
        x1 = item[0][0]
        y1 = item[0][1]
        x2 = item[1][0]
        y2 = item[1][1]

        tempx1 = x1
        tempx2 = x2
        if x1 > x2:
            tempx1 = x2
            tempx2 = x1

        tempy1 = y1
        tempy2 = y2
        if y1 > y2:
            tempy1 = y2
            tempy2 = y1

        if x1 == x2:
            while tempy1 <= tempy2:
                waypoints.append((x1, tempy1))
                tempy1 += 1
        elif y1 == y2:
            while tempx1 <= tempx2:
                waypoints.append((tempx1, y1))
                tempx1 += 1

    return (waypoints)


def checkForDuplicates(waypoints):
    results = {}
    for p in waypoints:
        if not p in results:
            results[p] = 1
        else:
            results[p] += 1
    return results


def countDuplicates(waypoints):
    result = 0
    for p in waypoints:
        if waypoints[p] >= 2:
            result += 1
    return result


def process(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        calc = calculateWaypoints(converted)
        results = checkForDuplicates(calc)
        counter = countDuplicates(results)
        result = {"file": fileInfo['key'], "counter": counter}
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        converted = convert(fileInfo)
        calc = calculateWaypoints2(converted)
        results = checkForDuplicates(calc)
        counter = countDuplicates(results)
        result = {"file": fileInfo['key'], "counter": counter}
        print(f"Part II: {result}")

process(files)
process2(files)
