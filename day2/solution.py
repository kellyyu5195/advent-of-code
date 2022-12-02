def file_to_string():
    input_file = open('input.txt', 'r')
    return input_file.read()

def string_to_round_list(input_str):
    list_of_rounds = input_str.split("\n")
    return [round.split(" ") for round in list_of_rounds]

# A, X = Rock 1
# B, Y = Paper 2
# C, Z = Scissor 3

XYZ_TO_POINTS = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

TIE = 3
WIN = 6
LOSE = 0

OUTCOME_MATRIX = {
    ('A', 'X'): TIE,
    ('A', 'Y'): WIN,
    ('A', 'Z'): LOSE,
    ('B', 'X'): LOSE,
    ('B', 'Y'): TIE,
    ('B', 'Z'): WIN,
    ('C', 'X'): WIN,
    ('C', 'Y'): LOSE,
    ('C', 'Z'): TIE,
}


def calculate_score(list_of_rounds):
    total_score = 0

    for round in list_of_rounds:
        total_score += XYZ_TO_POINTS[round[1]]
        total_score += OUTCOME_MATRIX[(round[0], round[1])]

    return total_score


ABC_TO_POINTS = {
    'A': 1,
    'B': 2,
    'C': 3,
}
XYZ_TO_OUTCOME = {
    'X': LOSE,
    'Y': TIE,
    'Z': WIN,
}
ABC_TO_XYZ = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}
ABC_TO_WINNING_OUTCOME = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}
ABC_TO_LOSING_OUTCOME = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

def calculate_score_part_2(list_of_rounds):
    total_score = 0

    for round in list_of_rounds:
        opponent, me = round[0], round[1]
        if XYZ_TO_OUTCOME[me] == TIE:
            total_score += TIE
            total_score += ABC_TO_POINTS[opponent]
        elif XYZ_TO_OUTCOME[me] == WIN:
            total_score += WIN
            total_score += ABC_TO_POINTS[ABC_TO_WINNING_OUTCOME[opponent]]
        elif XYZ_TO_OUTCOME[me] == LOSE:
            total_score += LOSE
            total_score += ABC_TO_POINTS[ABC_TO_LOSING_OUTCOME[opponent]]
    return total_score

def run():
    file_str = file_to_string()
    rounds = string_to_round_list(file_str)
    outcome = calculate_score(rounds)
    outcome_pt2 = calculate_score_part_2(rounds)

    return outcome, outcome_pt2

print(run())
