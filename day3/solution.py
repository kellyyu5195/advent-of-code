def file_to_string():
    input_file = open('input.txt', 'r')
    return input_file.read()

def string_to_list_of_rucksacks(input_str):
    return input_str.split("\n")

def get_misplaced_item(rucksack):
    midpoint = int(len(rucksack) / 2)
    comp_1 = rucksack[:midpoint]
    comp_2 = rucksack[midpoint:]

    for item in comp_1:
        if item in comp_2:
            return item

def get_item_priority(item):
    if item.islower():
        return ord(item) - ASCII_LOWERCASE_BASE

    return ord(item) - ASCII_UPPERCASE_BASE + 26

ASCII_LOWERCASE_BASE = 96
ASCII_UPPERCASE_BASE = 64

def get_priority_sum(rucksacks):
    sum = 0
    for r in rucksacks:
        misplaced_item = get_misplaced_item(r)
        sum += get_item_priority(misplaced_item)

    return sum

def get_elf_badge(rucksacks):
    r_1 = rucksacks[0]
    r_2 = rucksacks[1]
    r_3 = rucksacks[2]

    for item in r_1:
        if item in r_2 and item in r_3:
            return item

def get_elf_badge_sum(rucksacks):
    sum = 0
    i = 0

    while i < len(rucksacks):
        badge = get_elf_badge(rucksacks[i:i+3])
        sum += get_item_priority(badge)
        print(sum)
        i += 3

    return sum


def run():
    file_str = file_to_string()
    rucksacks = string_to_list_of_rucksacks(file_str)
    return get_priority_sum(rucksacks), get_elf_badge_sum(rucksacks)

print(run())
