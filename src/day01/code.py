sample = open("src/day01/sample.dat")
input = open("src/day01/input.dat")
files = [ 
    { "key": "sample", "file": sample },
    { "key": "input", "file": input }
]

for fileInfo in files:
    counter = 0
    last = None

    for line in fileInfo["file"]:
        intLine = int(line)
        if last is not None and last < intLine:
            counter += 1
        last = intLine

    print(f"{fileInfo['key']}: {counter}")
    fileInfo["file"].close()