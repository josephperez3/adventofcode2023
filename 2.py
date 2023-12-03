from sys import stdin


# ----------- PART 1 ------------


real_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_game_possible(cube_sets):
    # cube_sets= " 3 blue, 4 red; 4 blue, 3 green ..."
    for cube_set in cube_sets.split(";"):
        # cube_set = "3 blue, 4 red, 2 green"
        cube_tuples = cube_set.split(",")
        for cube_tuple in cube_tuples:
            cube_number, cube_color = cube_tuple.split()
            if int(cube_number) > real_cubes.get(cube_color, 0):
                return False
    return True

def part1():
    sum = 0
    for line in stdin:
        game_info, cube_sets = line.split(":")
        _, game_number = game_info.split(" ")
        if is_game_possible(cube_sets):
            sum += int(game_number)
    print(sum)

# ----------- PART 2 ------------
import math

def get_min_set(cube_sets):
    # cube_sets= " 3 blue, 4 red; 4 blue, 3 green ..."
    min_set = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for cube_set in cube_sets.split(";"):
        # cube_set = "3 blue, 4 red, 2 green"
        cube_tuples = cube_set.split(",")
        for cube_tuple in cube_tuples:
            cube_number, cube_color = cube_tuple.split()
            min_set[cube_color] = max(min_set[cube_color], int(cube_number))
    return min_set

def part2():
    sum = 0
    for line in stdin:
        game_info, cube_sets = line.split(":")
        _, game_number = game_info.split(" ")
        min_set = get_min_set(cube_sets)
        min_set_power = math.prod(min_set.values())
        sum += min_set_power
    print(sum)