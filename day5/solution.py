import re

def file_to_string():
    input_file = open('input.txt', 'r')
    return input_file.read()

def parse_stacks_and_moves(input_str):
    first_move_index = input_str.index('move')
    stacks_str = input_str[:first_move_index]
    stacks_rows = stacks_str.split('\n')
    stacks = {}
    stacks_rows = stacks_rows[:-3]
    for row in stacks_rows:
        i = 0
        stack_num = 1
        while i < len(row):
            if row[i+1] != ' ':
                if stack_num in stacks:
                    stacks[stack_num] = [row[i+1]] + stacks[stack_num]
                else:
                    stacks[stack_num] = [row[i+1]]
            i += 4
            stack_num += 1

    moves_str = input_str[first_move_index:]

    moves = re.split('move | from | to |\n', moves_str)
    moves = [i for i in moves if i != '']
    return stacks, moves

def make_move(stacks, moves):
    num_to_move = int(moves[0])
    from_stack = stacks[int(moves[1])]
    to_stack = stacks[int(moves[2])]

    for i in range(num_to_move):
        item = from_stack.pop()
        to_stack.append(item)

    return stacks

def make_bulk_move(stacks, moves):
    num_to_move = int(moves[0])
    from_stack = stacks[int(moves[1])]
    to_stack = stacks[int(moves[2])]

    items_to_move = from_stack[-num_to_move:]
    to_stack += items_to_move
    stacks[int(moves[1])] = from_stack[:len(from_stack)-num_to_move]

    return stacks

def get_tops_of_stacks(stacks, moves):
    i = 0
    while i < len(moves):
        stacks = make_move(stacks, moves[i:i+3])
        i += 3

    solution = ''
    for i in range(1, max(stacks.keys())+1):
        solution += stacks[i][-1]

    return solution

def get_tops_of_stacks_new(stacks, moves):
    i = 0
    while i < len(moves):
        stacks = make_bulk_move(stacks, moves[i:i+3])
        i += 3

    solution = ''
    for i in range(1, max(stacks.keys())+1):
        solution += stacks[i][-1]

    return solution

# helper for debugging
def print_stacks(stacks):
    for i in range(1, max(stacks.keys())+1):
        print(i, stacks[i])

def run():
    file_str = file_to_string()
    stacks, moves = parse_stacks_and_moves(file_str)
    part_1 = get_tops_of_stacks(stacks, moves)
    stacks, moves = parse_stacks_and_moves(file_str)
    part_2 = get_tops_of_stacks_new(stacks, moves)
    return part_1, part_2

print(run())
