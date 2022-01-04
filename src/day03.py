def convert(fileInfo):
    arrays = []
    with open(fileInfo["file"]) as file:
        linecounter = 0

        for line in file:
            arraywidth = 0
            linecounter += 1
            arr = []
            for bit in line:
                if (bit != "\n"):
                    arr.append(int(bit))
                    arraywidth += 1
            arrays.append(arr)


    return {"arrays": arrays, "lines": linecounter, "width": arraywidth}


def solve_part1(fileInfo):
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
    return gamma * epsilon

def filter(arrays, mostCommon=True):
    currentArray = arrays["arrays"]
    idx = 0

    while idx < int(arrays["width"]) and len(currentArray) > 1:
        numbers = []
        for a in currentArray:
            num = a[idx]
            numbers.append(num)

        bitToFind = 0
        if mostCommon and sum(numbers) >= len(currentArray) / 2:
            bitToFind = 1
        elif not mostCommon and sum(numbers) < len(currentArray) / 2:
            bitToFind = 1

        tempArray = []
        for a in currentArray:
            if a[idx] == bitToFind:
                tempArray.append(a)

        currentArray = tempArray
        idx += 1

    binary = ''.join(list(map(lambda x: str(x), currentArray[0])))
    return int(binary, 2)


def solve_part2(fileInfo):
    arrays = convert(fileInfo)
    intOxy = filter(arrays)
    intCo2 = filter(arrays, False)

    return intOxy * intCo2