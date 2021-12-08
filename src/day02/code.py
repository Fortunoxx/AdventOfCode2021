import sys
sys.path.append('src/puzzle')
import puzzle

day = "02"
puzzle.FetchForDay(day)


files = [
    {"key": "input", "file": f"src/day{day}/input.dat"},
    {"key": "sample", "file": f"src/day{day}/sample.dat"}
]


def process(fileInfos):
    for fileInfo in fileInfos:
        horiz = 0
        depth = 0

        file = open(fileInfo["file"])
        for line in file:
            parts = line.split(' ')
            cmd = parts[0]
            num = int(parts[1])
            if cmd == "forward":
                horiz += num
            elif cmd == "down":
                depth += num
            elif cmd == "up":
                depth -= num

        file.close()

        result = {"file": fileInfo['key'], "horiz": horiz,
                  "depth": depth, "prod": horiz*depth}
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        horiz = 0
        depth = 0
        aim = 0

        file = open(fileInfo["file"])
        for line in file:
            parts = line.split(' ')
            cmd = parts[0]
            num = int(parts[1])
            if cmd == "forward":
                horiz += num
                depth += (aim * num)
            elif cmd == "down":
                aim += num
            elif cmd == "up":
                aim -= num

        file.close()
        
        result = {"file": fileInfo['key'], "horiz": horiz,
                  "depth": depth, "prod": horiz*depth}
        print(f"Part II: {result}")


process(files)
process2(files)
