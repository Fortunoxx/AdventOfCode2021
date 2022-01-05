from collections import defaultdict

def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        caves = defaultdict(list)
        for line in file:
            for p1, p2 in [line.replace('\n', '').split('-')]:
                if p1 == "start":
                    caves[p1].append(p2)
                elif p2 == "end":
                    caves[p1].append(p2)
                elif p1 == "end":
                    caves[p2].append(p1)
                else:
                    caves[p1].append(p2)
                    caves[p2].append(p1)
        return caves


def find_unique_paths(caves, path, end):
    paths = []
    for cave in caves[path[-1]]:
        if cave == end:
            paths.append(path + [cave])
        elif cave.isupper() or cave not in path:
            paths += find_unique_paths(caves, path + [cave], end)
    return paths


def solve_part1(fileInfo):
    converted = convert(fileInfo)
    unique_paths = find_unique_paths(converted, ['start'], 'end')
    return len(unique_paths)


# def solve_part2(fileInfo):
#     converted = convert(fileInfo)
#     return result


solve_part1({"file": "test/data/day12.sample.dat"})