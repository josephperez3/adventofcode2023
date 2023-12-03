from sys import stdin

# -------------------- PART 1 --------------------

def getNumber(index, line, schematics):
    number = ""
    while index < len(line):
        current_char = line[index]
        if current_char not in "0123456789":
            break
        number += current_char
        index += 1
    return number

def isSymbol(char):
    return (char >= '!' and char <= "/") or (char >= ":" and char <= "@")

def checkForSymbol(index_tuple, schematics):
    line_number, line_index = index_tuple
    if (line_number < 0) or (line_number >= len(schematics)):
        return False
    line = schematics[line_number]
    if (line_index < 0) or (line_index >= len(line)):
        return False
    char = line[line_index]
    return char != '.' and isSymbol(char)

def isEnginePart(number, line_number, starting_index, schematics):
    # need to check diagonals for first and last, up and down for middle chars
    i = 0
    while i < len(number):
        indices_to_check = []
        current_index = starting_index + i
        if i == 0:
            # check left edges
            indices_to_check.append((line_number - 1, current_index - 1))
            indices_to_check.append((line_number, current_index - 1))
            indices_to_check.append((line_number + 1, current_index - 1))
        if i == len(number) - 1:
            # check right edges
            indices_to_check.append((line_number - 1, current_index + 1))
            indices_to_check.append((line_number, current_index + 1))
            indices_to_check.append((line_number + 1, current_index + 1))
        # check up and down
        indices_to_check.append((line_number - 1, current_index))
        indices_to_check.append((line_number + 1, current_index))

        for index_tuple in indices_to_check:
            if checkForSymbol(index_tuple, schematics):
                return True

        i += 1

    return False
            

def part1():
    schematics = []
    for line in stdin:
        schematics.append(line)

    sum = 0
    for line_number, line in enumerate(schematics):
        index = 0
        while index < len(line):
            number = getNumber(index, line, schematics)
            if number:
                if isEnginePart(number, line_number, index, schematics):
                    sum += int(number)
                index += len(number)
            else:
                index += 1
    return sum

# -------------------- PART 2 --------------------

def isGear(index_tuple, schematics):
    line_number, line_index = index_tuple
    if (line_number < 0) or (line_number >= len(schematics)):
        return False
    line = schematics[line_number]
    if (line_index < 0) or (line_index >= len(line)):
        return False
    char = line[line_index]
    return char == '*'

def getAdjacentGears(number, line_number, starting_index, schematics):
    # need to check diagonals for first and last, up and down for middle chars
    i = 0
    adjacentGears = []
    while i < len(number):
        indices_to_check = []
        current_index = starting_index + i
        if i == 0:
            # check left edges
            indices_to_check.append((line_number - 1, current_index - 1))
            indices_to_check.append((line_number, current_index - 1))
            indices_to_check.append((line_number + 1, current_index - 1))
        if i == len(number) - 1:
            # check right edges
            indices_to_check.append((line_number - 1, current_index + 1))
            indices_to_check.append((line_number, current_index + 1))
            indices_to_check.append((line_number + 1, current_index + 1))
        # check up and down
        indices_to_check.append((line_number - 1, current_index))
        indices_to_check.append((line_number + 1, current_index))

        for index_tuple in indices_to_check:
            if isGear(index_tuple, schematics):
                # return location of gear
                adjacentGears.append(index_tuple)

        i += 1

    return adjacentGears

def part2():
    schematics = []
    for line in stdin:
        schematics.append(line)

    gear_parts = {}
    sum = 0
    for line_number, line in enumerate(schematics):
        index = 0
        while index < len(line):
            number = getNumber(index, line, schematics)
            if number:
                adjacentGears = getAdjacentGears(number, line_number, index, schematics)
                for gearLocation in adjacentGears:
                    gear_parts.setdefault(gearLocation, []).append(number)
                index += len(number)
            else:
                index += 1
    for part_list in gear_parts.values():
        if len(part_list) == 2:
            sum += (int(part_list[0]) * int(part_list[1]))
    print(sum)