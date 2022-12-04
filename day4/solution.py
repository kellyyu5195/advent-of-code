def file_to_string():
    input_file = open('input.txt', 'r')
    return input_file.read()

def get_assignment_pairs(input_str):
    assigments_unparsed = input_str.split("\n")

    return [[r.split("-") for r in a.split(",")] for a in assigments_unparsed]

def do_assignments_fully_overlap(a1, a2):
    a1_min, a1_max, a2_min, a2_max = int(a1[0]), int(a1[1]), int(a2[0]), int(a2[1])

    return (a1_min <= a2_min and a2_max <= a1_max) or (a2_min <= a1_min and a1_max <= a2_max)


def get_num_fully_overlapping_pairs(pairs):
    sum = 0

    for pair in pairs:
        if do_assignments_fully_overlap(pair[0], pair[1]):
            sum += 1

    return sum

def do_assignments_overlap(a1, a2):
    a1_min, a1_max, a2_min, a2_max = int(a1[0]), int(a1[1]), int(a2[0]), int(a2[1])

    return (a1_max in range(a2_min, a2_max+1)) or (a2_max in range(a1_min, a1_max+1))

def get_num_overlapping_pairs(pairs):
    sum = 0

    for pair in pairs:
        if do_assignments_overlap(pair[0], pair[1]):
            sum += 1

    return sum


def run():
    pairs = get_assignment_pairs(file_to_string())
    return get_num_fully_overlapping_pairs(pairs), get_num_overlapping_pairs(pairs)

print(run())
