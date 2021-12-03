day = "01"
files = [ 
    { "key": "input", "file": open(f"src/day{day}/input.dat") },
    { "key": "sample", "file": open(f"src/day{day}/sample.dat") }
]

for fileInfo in files:
    counter = 0
    last = None

    for line in fileInfo["file"]:
        number = int(line)
        if last is not None and last < number:
            counter += 1
        last = number

    print(f"{fileInfo['key']}: {counter}")
    fileInfo["file"].close()