from sys import stdin
import math
import cmath

# -------------------- PART 1 --------------------

def calc_record_range(time, dist_record):
    # let x = time spent pressing button
    # distance = speed * time
    # distance = x * (race_time - x)
    # distance = x * (race_time - x) - dist_record 
    # distance = -x^2 + x(race_time) - dist_record
    
    # for quadratic formula...
    a = -1
    b = time
    c = -1 * dist_record

    discriminant = (b**2) - (4*a*c)
    sol1 = (-b+math.sqrt(discriminant))/(2*a)
    sol2 = (-b-math.sqrt(discriminant))/(2*a)

    # always have to round up, so do floor(x + 1)
    sol1 = math.floor(sol1 + 1)
    sol2 = math.ceil(sol2 - 1)

    record_range = int(sol2 - sol1 + 1)
    return record_range

test_input = """
Time:      7  15   30
Distance:  9  40  200
"""

test_input = test_input.splitlines()

def parse_input():
    time_line = input()
    distance_line = input()
    _, time_numbers = time_line.split(":")
    _, distance_numbers = distance_line.split(":")
    time_numbers = [int(x) for x in time_numbers.split()]
    distance_numbers = [int(x) for x in distance_numbers.split()]
    return time_numbers, distance_numbers

def part1():
    sol = 1
    time_numbers, distance_numbers = parse_input()
    race_infos = zip(time_numbers, distance_numbers)
    for time, dist_record in race_infos:
        sol *= (calc_record_range(time, dist_record))
    return sol


# -------------------- PART 1 --------------------

def parse_input_2():
    time_line = input()
    distance_line = input()
    _, time_numbers = time_line.split(":")
    _, distance_numbers = distance_line.split(":")
    time_number = int("".join(time_numbers.split()))
    distance_number = int("".join(distance_numbers.split()))
    return time_number, distance_number

def part2():
    sol = 1
    time_number, distance_number = parse_input_2()
    sol *= (calc_record_range(time_number, distance_number))
    return sol