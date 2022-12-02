def file_to_string():
    input_file = open('input.txt', 'r')
    return input_file.read()

def string_to_cal_per_elf(input_str):
    cal_per_elf_input = input_str.split("\n\n")

    elf_cal_strs = [elf_list.split("\n") for elf_list in cal_per_elf_input]

    return [map(lambda x: int(x), elf_cal_str) for elf_cal_str in elf_cal_strs]

def get_most_elf_calories(list_of_calories_per_elf):
    largest_elf_cal = 0
    for i in range(len(list_of_calories_per_elf)):
        elf_sum = sum(list_of_calories_per_elf[i])
        if elf_sum > largest_elf_cal:
            largest_elf_cal = elf_sum

    return largest_elf_cal

def get_top_3_elves(list_of_calories_per_elf):
    top_3_sums = [0, 0, 0]
    for i in range(len(list_of_calories_per_elf)):
        current_max = top_3_sums[2]
        current_min = top_3_sums[0]
        elf_sum = sum(list_of_calories_per_elf[i])
        if elf_sum < current_min:
            continue
        top_3_sums = top_3_sums[1:]
        if elf_sum > current_max:
            top_3_sums.append(elf_sum)
        elif elf_sum > top_3_sums[1]:
            top_3_sums.insert(1, elf_sum)
        else:
            top_3_sums.insert(0, elf_sum)

    return sum(top_3_sums)


def run():
    file_contents = file_to_string()
    elf_info = string_to_cal_per_elf(file_contents)
    solution = get_most_elf_calories(elf_info)
    print('top one elf: ' + str(solution))
    elf_info_again = string_to_cal_per_elf(file_contents)
    print('top 3 elves: ' + str(get_top_3_elves(elf_info_again)))

run()