import sys
sys.path.append('src/puzzle')
import puzzle

day = "xx"
puzzle.FetchForDay(day)


files = [ 
    { "key": "input", "file": f"src/day{day}/input.dat" },
    { "key": "sample", "file": f"src/day{day}/sample.dat" }
]

def process(fileInfos):
    for fileInfo in fileInfos:
        counter = 0

        file = open(fileInfo["file"])
        for line in file:
            counter+=1

        file.close()

        result = { "file": fileInfo['key'] }
        print(f"Part I: {result}")

def process2(fileInfos):
    for fileInfo in fileInfos:
        counter = 0

        file = open(fileInfo["file"])
        for line in file:
            counter+=1

        file.close()
        
        result = { "file": fileInfo['key'] }
        print(f"Part II: {result}")

process(files)
process2(files)