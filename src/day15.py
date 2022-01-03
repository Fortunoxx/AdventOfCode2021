import sys
sys.path.append('src/puzzle')

day = "15"
# file = {"key": "input", "file": f"src/data/day{day}.input.dat"}
file = {"key": "input", "file": f"test/data/day{day}.sample.dat"}

import numpy as np
import puzzle
puzzle.FetchForDay(day)


def dijkstra(nodes, distances):
    # These are all the nodes which have not been visited yet
    unvisited = {node: None for node in nodes}
    # It will store the shortest distance from one node to another
    visited = {}
    current = 0
    # It will store the predecessors of the nodes
    currentDistance = 0
    unvisited[current] = currentDistance
    # Running the loop while all the nodes have been visited
    while True:
        # iterating through all the unvisited node
        for neighbour, distance in distances[current].items():
            # Iterating through the connected nodes of current_node (for 
            # example, a is connected with b and c having values 10 and 3
            # respectively) and the weight of the edges
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        # up until now the shortest distance between the source node and target node 
        # has been found. Set the current node as the target node
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: 
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited


def convert(fileInfo, multiply = 0):
    arrays = []
    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            arr = []
            for pos in line:
                arr.append(int(pos))
            arrays.append(arr)

    if multiply > 0:
        final = np.array(arrays)

        # append horizontally
        m = final[:]
        for _ in range(multiply):
            m = m + 1
            n = np.where(m >= 10, 1, m) # reset to 1 when >= 10
            final = np.concatenate((final, n), axis=1) 
            m = n

        # append vertically
        m = final[:]
        for _ in range(multiply):
            m = m + 1
            n = np.where(m >= 10, 1, m) # reset to 1 when >= 10
            final = np.concatenate((final, n), axis=0) # append vertically
            m = n

        # overwrite working array
        arrays = final 

    nodes = []
    distances = {}

    y = 0
    for a in arrays:
        x = 0
        for _ in a:
            id = calcId(x, y, len(arrays))
            nodes.append(id)
            distances[id] = getNeighbours((x, y), arrays)
            x += 1
        y += 1

    return (nodes, distances, len(arrays))


def getNeighbours(pos, source):
    theMax = len(source) # we assume, there is an equal number of rows and columns
    x = pos[0]
    y = pos[1]

    result = {}
    if x > 0:
        result[calcId(x-1, y, theMax)] = source[y][x-1]
    if x < theMax - 1:
        result[calcId(x+1, y, theMax)] = source[y][x+1]
    if y > 0:
        result[calcId(x, y-1, theMax)] = source[y-1][x]
    if y < theMax - 1:
        result[calcId(x, y+1, theMax)] = source[y+1][x]
    return result


def calcId(x, y, size):
    return y * size + x


def solve_part1(fileInfo):
    converted = convert(fileInfo)
    d = dijkstra(converted[0], converted[1])
    endPosition = converted[2] * converted[2] - 1
    calculatedMinimalRisk = d[endPosition]
    return calculatedMinimalRisk


def solve_part2(fileInfo):
    converted = convert(fileInfo, 4)
    d = dijkstra(converted[0], converted[1])
    endPosition = converted[2] * converted[2] - 1
    calculatedMinimalRisk = d[endPosition]
    return calculatedMinimalRisk


print(f"Part 1: {solve_part1(file)}")
print(f"Part 2: {solve_part2(file)}")