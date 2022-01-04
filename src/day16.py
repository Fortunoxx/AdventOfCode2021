def convert(fileInfo):
    with open(fileInfo["file"]) as file:
        line = file.read()
        line = line.replace("\n", "")
        return convertToBinary(line)


def convertToBinary(line):
    binary = ''
    num_of_bits = 4
    for char in line:
        binary += bin(int(char, 16))[2:].zfill(num_of_bits)
    return (binary, line)


def parsePackets(binary, idx, parent, endIdx):
    version_length = 3
    type_id_length = 3
    newIdx = idx

    # parse header
    while newIdx < endIdx:
        version = int(binary[newIdx:newIdx+version_length], 2)
        newIdx += version_length
        type_id = int(binary[newIdx:newIdx+type_id_length], 2)
        newIdx += type_id_length

        if type_id == 4:
            newIdx = parseLiteral(newIdx, binary, version, parent, type_id)
        else:
            newIdx = parseOperator(newIdx, binary, version, parent, type_id)

    return (newIdx, parent)


def parsePacketsByCounter(binary, idx, parent, counter, current = 0):
    version_length = 3
    type_id_length = 3
    newIdx = idx

    # parse header
    while current < counter:
        version = int(binary[newIdx:newIdx+version_length], 2)
        newIdx += version_length
        type_id = int(binary[newIdx:newIdx+type_id_length], 2)
        newIdx += type_id_length

        if type_id == 4:
            newIdx = parseLiteral(newIdx, binary, version, parent, type_id)
        else:
            newIdx = parseOperator(newIdx, binary, version, parent, type_id)

        current += 1

    return (newIdx, parent)


def parseOperator(idx, source, version, parent, type_id):
    newIdx = idx
    length_type_id_length = 1
    type_0_length = 15
    type_1_length = 11

    length_type_id = int(source[newIdx:newIdx+length_type_id_length], 2)
    newIdx += length_type_id_length

    item = { "version": version, "type_id": type_id, "items": [] }
    if not 'items' in parent:
        parent['items'] = [item]
    else:
        parent['items'].append(item)

    if length_type_id == 0:
        total_length_in_bits = int(source[newIdx:newIdx+type_0_length], 2)
        newIdx += type_0_length
        end = newIdx + total_length_in_bits

        while newIdx < end:
            (newIdx, item) = parsePackets(source, newIdx, item, end)
    else:
        number_of_sub_packages = int(source[newIdx:newIdx+type_1_length], 2)
        newIdx += type_1_length
        (newIdx, item) = parsePacketsByCounter(source, newIdx, item, number_of_sub_packages)

    return newIdx


def parseLiteral(idx, source, version, parent, type_id = 4):
    newIdx = idx
    group_identifier_length = 1
    group_length = 4
    isNotLastGroup = '1'
    item = {}
    value = ''

    while isNotLastGroup == '1':
        isNotLastGroup = source[newIdx:newIdx+group_identifier_length]
        newIdx += group_identifier_length
        value += source[newIdx:newIdx+group_length]
        newIdx += group_length

        if isNotLastGroup == '0':
            item = { "version": version, "type_id": type_id, "value": int(value,2) }
            if not 'items' in parent:
                parent['items'] = [item]
            else:
                parent['items'].append(item)

    return newIdx


def calculate_version_sum(packets, result = 0):
    for item in packets['items']:
        result += item['version']
        if 'items' in item:
            result = calculate_version_sum(item, result)
    return result


def calculate_packet_sum(item, result = 0):
    type_id = item['type_id']
    if type_id == 0:
        sub = 0
        for itm in item['items']:
            sub += calculate_packet_sum(itm)
        return sub
    elif type_id == 1:
        sub = 1
        for itm in item['items']:
            sub *= calculate_packet_sum(itm)
        return sub
    elif type_id == 2:
        results = []
        for itm in item['items']:
            results.append(calculate_packet_sum(itm))
        return sorted(results)[0] # minimum
    elif type_id == 4:
        return item['value']
    elif type_id == 3:
        results = []
        for itm in item['items']:
            results.append(calculate_packet_sum(itm))
        return sorted(results)[-1] # maximum
    elif type_id == 5:
        items = item['items']
        result1 = calculate_packet_sum(items[0])
        result2 = calculate_packet_sum(items[1])
        if result1 > result2:
            return 1
        return 0    
    elif type_id == 6:
        items = item['items']
        result1 = calculate_packet_sum(items[0])
        result2 = calculate_packet_sum(items[1])
        if result1 < result2:
            return 1
        return 0
    elif type_id == 7:
        items = item['items']
        result1 = calculate_packet_sum(items[0])
        result2 = calculate_packet_sum(items[1])
        if result1 == result2:
            return 1
        return 0
    else:
        return 0


def solve_part1(data):
    packets = parsePackets(data[0], 0, {}, len(data[0])-7)[1] # this is the definitive end of the line, assuming there can be at most 7 trailing zeros
    version_sum = calculate_version_sum(packets)
    return version_sum


def solve_part2(data):
    packets = parsePackets(data[0], 0, {}, len(data[0])-7)[1]
    calc = calculate_packet_sum(packets['items'][0])
    return calc