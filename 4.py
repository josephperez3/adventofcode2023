from sys import stdin

# -------------------- PART 1 --------------------

def parse_scratch_card(line):
    _, number_info = line.split(":")
    winning_numbers, my_numbers = number_info.split("|")
    winning_numbers = winning_numbers.split()
    winning_numbers = dict.fromkeys(winning_numbers, 1)
    my_numbers = my_numbers.split()
    return winning_numbers, my_numbers

def part1():
    total_points = 0
    for line in stdin:
        winning_numbers, my_numbers = parse_scratch_card(line)
        numbers_won = 0
        for number in my_numbers:
            if number in winning_numbers:
                numbers_won += 1
        if numbers_won > 0:
            total_points += 2 ** (numbers_won - 1)
    return total_points

# -------------------- PART 2 --------------------

def getGameNumber(line):
    game_info, _ = line.split(":")
    _, game_number = game_info.split()
    return int(game_number)

def part2():
    scratch_cards_count = 0
    extra_cards = {} # eg. [3] = extra cards for Game 3
    for line in stdin:
        game_number = getGameNumber(line)
        n_extra_cards = extra_cards.get(game_number, 0)
        n_cards = 1 + n_extra_cards
        scratch_cards_count += n_cards

        numbers_won = 0
        winning_numbers, my_numbers = parse_scratch_card(line)
        for number in my_numbers:
            if number in winning_numbers:
                numbers_won += 1
        for win in range(0, numbers_won):
            bonus_game = game_number + win + 1 # +1 since we start at 0
            extra_cards[bonus_game] = extra_cards.get(bonus_game, 0) + n_cards
    return scratch_cards_count




        