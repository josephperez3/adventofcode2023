from sys import stdin

# -------------------- PART 1 --------------------

FIVE_K = 6
FOUR_K = 5
FULL = 4
THREE_K = 3
TWO_P = 2
ONE_P = 1
HIGH = 0

NUM_TYPES = 7

hand_types = [[] for x in range(0, NUM_TYPES)]
def parse_input():
    for line in stdin:
        hand, bid = line.split()
        process_hand((hand, bid))
        

def process_hand(hand):
    card_count = {}
    cards, _ = hand
    for card in cards:
        card_count[card] = card_count.get(card, 0) + 1
    max_count = 0
    pair_count = 0
    for card, count in card_count.items():
        max_count = max(max_count, count)
        if count == 2: pair_count += 1
    hand_type = None
    if max_count == 5:
        hand_type = FIVE_K
    elif max_count == 4:
        hand_type = FOUR_K
    elif max_count == 3 and pair_count:
        hand_type = FULL
    elif max_count == 3:
        hand_type = THREE_K
    elif max_count == 2 and pair_count > 1:
        hand_type = TWO_P
    elif max_count == 2:
        hand_type = ONE_P
    else:
        hand_type = HIGH
    hand_types[hand_type].append(hand)

def get_card_value(card):
    value = 0
    try:
        value = int(card)
    except:
        match card:
            case "T":
                value = 10
            case "J":
                value = 11
            case "Q":
                value = 12
            case "K":
                value = 13
            case "A":
                value = 14
    return value

def sort_hands(hands):
    hands.sort(key=lambda hand: [get_card_value(card) for card in hand[0]])

def part1():
    parse_input()
    rank = 1
    total_winnings = 0
    for hands in hand_types:
        sort_hands(hands)
        for hand in hands:
            _, bet = hand
            total_winnings += rank * int(bet)
            rank += 1
    return total_winnings

# -------------------- PART 2 --------------------

hand_types = [[] for x in range(0, NUM_TYPES)]
    
def parse_input2():
    for line in stdin:
        hand, bid = line.split()
        process_hand2((hand, bid))
        
def process_hand2(hand):
    card_count = {}
    cards, _ = hand
    for card in cards:
        card_count[card] = card_count.get(card, 0) + 1
    max_count = 0
    pair_count = 0
    for card, count in card_count.items():
        if card != "J":
            max_count = max(max_count, count)
            if count == 2: pair_count += 1
    joker_count = card_count.get("J", 0)
    if max_count == 2 and joker_count:
        pair_count -= 1
    max_count += joker_count
    hand_type = None
    if max_count == 5:
        hand_type = FIVE_K
    elif max_count == 4:
        hand_type = FOUR_K
    elif max_count == 3 and pair_count:
        hand_type = FULL
    elif max_count == 3:
        hand_type = THREE_K
    elif max_count == 2 and pair_count > 1:
        hand_type = TWO_P
    elif max_count == 2:
        hand_type = ONE_P
    else:
        hand_type = HIGH
    hand_types[hand_type].append(hand)

def get_card_value2(card):
    value = 0
    try:
        value = int(card)
    except:
        match card:
            case "T":
                value = 10
            case "J":
                value = 1
            case "Q":
                value = 12
            case "K":
                value = 13
            case "A":
                value = 14
    return value 

def sort_hands2(hands):
    hands.sort(key=lambda hand: [get_card_value2(card) for card in hand[0]])

def part2():
    parse_input2()
    rank = 1
    total_winnings = 0
    for hands in hand_types:
        sort_hands2(hands)
        for hand in hands:
            _, bet = hand
            total_winnings += rank * int(bet)
            rank += 1
    return total_winnings

