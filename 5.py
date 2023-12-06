from sys import stdin

# -------------------- PART 1 --------------------

def parse_input():
    resource_maps = {}
    source_type = ""
    dest_type = ""
    seeds_to_be_planted = []
    for line in stdin:
        line_arr = line.split()
        if len(line_arr) == 0:
            # input is just an empty line, pass to get the new line
            pass
        elif line_arr[0] == "seeds:":
            seeds_to_be_planted = line_arr[1:]
        elif line_arr[-1] == "map:":
            source_type, _, dest_type = line_arr[0].split("-")
            resource_maps[source_type] = []
        else:
            dest_start, source_start, range_len = line_arr
            resource_maps[source_type].append((dest_start, source_start, range_len, dest_type))
    return resource_maps, source_type, dest_type, seeds_to_be_planted

def part1():
    resource_maps, source_type, dest_type, seeds_to_be_planted = parse_input()
    lowest_final = float('inf')
    for seed in seeds_to_be_planted:
        current_resource = "seed"
        current_number = int(seed)
        while current_resource != "location":
            resource_map = resource_maps[current_resource]
            dest_number = None
            dest_type = None
            for mapping in resource_map:
                dest_start, source_start, range_len, dest_type = mapping
                dest_start, source_start, range_len = int(dest_start), int(source_start), int(range_len)
                # print(f'{current_resource} range: {range(source_start, source_start + range_len)}')
                if current_number in range(source_start, source_start + range_len):
                    offset = current_number - source_start
                    dest_number = dest_start + offset
                    break
            if not dest_number:
                dest_number = current_number
                # print(f'2 {current_resource}: {current_number} to {dest_type}: {dest_number}')
            current_number = dest_number 
            current_resource = dest_type
        lowest_final = min(lowest_final, current_number)
    return lowest_final


# -------------------- PART 2 --------------------

def part2():
    seed_ranges = []
    resource_maps, source_type, dest_type, seeds_to_be_planted = parse_input()
    for i in range(0, len(seeds_to_be_planted), 2):
        seed_start, range_len = int(seeds_to_be_planted[i]), int(seeds_to_be_planted[i + 1])
        seed_ranges.append((seed_start, seed_start + range_len))
        # print(f'{seed_start} to {seed_}')

    paths_to_end = {}
    for resource in resource_maps.keys():
        paths_to_end[resource] = {}


    """
    For some range (6...15)
    6 and 15 will all resolve to the same pattern (eg 6...15 -> 106...115) WHEN 
    - you are in a pattern already. For example, 0 to 30 goes to 100. 
        -> New range starts at your source (6 + offset) and goes to either max of your range (15) OR max of resource range (30) - choose min of these
        -> all elements in your range get the same offset (100 in this case)
    - OR NONE of your elements are in the pattern
        -> Then, 6...15 stays as 6...15
        -> UNLESS there's some resource pattern that starts at 10 for example.. then we'd have to make a new range from there

    Store all these calculated ranges in a new array, and do it recursively 

    Recursively: We have a range 1-50. We determine 1-25 are all the same. 
    Now we have a range 26-50. Do the function again.

    """ 


    rangs = seed_ranges
    current_resource = "seed"
    while current_resource != "location":
        new_rangs = []
        for range_start, range_end in rangs:
            current_index = range_start
            resource_map = resource_maps[current_resource]
            i = 0
            while current_index < range_end:
                dest_number = None
                end_number = None
                dest_type = None
                closest_range = float('inf')
                current_number = current_index
                for mapping in resource_map:
                    dest_start, source_start, range_len, dest_type = mapping
                    dest_start, source_start, range_len = int(dest_start), int(source_start), int(range_len) 
                    source_range_end = source_start + range_len
                    if source_start > current_number:
                        # find the closest range up (can skip to there)
                        closest_range = min(closest_range, source_start)
                        
                    if current_number >= source_start and current_number < source_range_end:
                        # in the range of this mapping
                        up_until = min(range_end, source_range_end)
                        offset = dest_start - source_start
                        dest_number = current_number + offset
                        end_number = up_until + offset
                        rng = (dest_number, end_number)
                        new_rangs.append(rng)
                        break
                if not dest_number:
                    dest_number = current_number
                    end_number = min(range_end, closest_range)
                    # what if there is no closest range? Empty until the end
                    rng = (dest_number, end_number)
                    new_rangs.append(rng)
                current_index += (end_number - dest_number)
        current_resource = resource_map[0][3]
        rangs = new_rangs

    min_loc = min(rangs, key = lambda x : x[0])[0]
    return min_loc