from sys import stdin

trie = {
    "t": {
        "w": "o",
        "h": "ree"
    },
    "f": {
        "o": "ur",
        "i": "ve"
    },
    "o": "ne",
    "s": {
        "i": "x",
        "e": "ven"
    },
    "e": "ight",
    "n": "ine",
}

numberStrToIntMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def numberStrToInt(number):
    ret_int = 0
    try:
        ret_int = int(number)
    except:
        ret_int = numberStrToIntMap.get(number)
    return ret_int

def checkForNumber(string, index):
    current_char = str(string[index])
    if current_char in "0123456789":
        return current_char
    current_string = ""
    trie_node = trie.get(current_char)
    while trie_node != None:
        current_string += current_char
        if isinstance(trie_node, str):
            len_remaining = len(trie_node)
            if (index + len_remaining < len(string)) and string[index + 1: index + len_remaining + 1] == trie_node:
                return current_string + trie_node
            return ""
        elif isinstance(trie_node, dict):
            index += 1
            current_char = string[index]
            trie_node = trie_node.get(current_char)
        else:
            return ""
    return ""
            


sum = 0
for line in stdin:
    n1 = 0
    n2 = 0
    i = 0
    while i < len(line):
        x = checkForNumber(line, i)
        x = numberStrToInt(x)
        i += 1
        if not x:
            continue
        n2 = x
        if not n1:
            n1 = x
    line_number = str(n1) + str(n2)
    sum += int(line_number)
print(sum)
