day = "01"
files = [ 
    { "key": "input", "file": open(f"src/day{day}/input.dat") },
    { "key": "sample", "file": open(f"src/day{day}/sample.dat") }
]

cnt = 3

for fileInfo in files:
    counter = 0
    last = None
    arrays = []
    results = []

    for line in fileInfo["file"]:
        number = int(line)
        arrays.append([])

        for array in arrays:
            if (len(array) < cnt):
                array.append(number)

    l = len(arrays) - 1
    
    # remove last 2 arrays - incomplete
    arrays.pop(l)
    arrays.pop(l - 1)

    for a in arrays: 
        s = 0
        for i in a:
            s += i
        results.append(s)

    for number in results:
        if last is not None and last < number:
            counter += 1
        last = number

    print(f"{fileInfo['key']}: {counter}")
    fileInfo["file"].close()