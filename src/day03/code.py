day = "03"
files = [
    {"key": "input", "file": f"src/day{day}/input.dat"},
    {"key": "sample", "file": f"src/day{day}/sample.dat"}
]


def convert(fileInfo):
    arrays = []
    file = open(fileInfo["file"])
    linecounter = 0

    for line in file:
        arraywidth = 0
        linecounter += 1
        arr = []
        for bit in line:
            arraywidth += 1
            if (bit != "\n"):
                arr.append(int(bit))
        arrays.append(arr)

    file.close()
    
    return {"arrays": arrays, "lines": linecounter, "width": arraywidth}


def process(fileInfos):
    for fileInfo in fileInfos:
        arrays = convert(fileInfo)
        length = int(arrays["lines"])
        idx = 0
        sum1 = ""
        sum2 = ""

        while idx < int(arrays["width"]):
            numbers = []
            for a in arrays["arrays"]:
                num = a[idx]
                numbers.append(num)

            sum = 0
            for n in numbers:
                sum += n

            if sum > length / 2:
                sum1 += "1"
                sum2 += "0"
            else:
                sum1 += "0"
                sum2 += "1"
            idx += 1

        gamma = int(sum1, 2)
        epsilon = int(sum2, 2)
        result = {"file": fileInfo['key'], "gamma": gamma,
                  "epsilon": epsilon, "result": gamma * epsilon}
        print(f"Part I: {result}")


def process2(fileInfos):
    for fileInfo in fileInfos:
        counter = 0

        file = open(fileInfo["file"])
        for line in file:
            counter += 1

        file.close()
        result = {"file": fileInfo['key']}
        print(f"Part II: {result}")


process(files)
process2(files)
