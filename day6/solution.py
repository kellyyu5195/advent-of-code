def file_to_string():
    input_file = open('input.txt', 'r')
    return input_file.read()

def has_duplicates(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return True
    return False

def get_first_marker(input_str, marker_len):
    chars_before = marker_len - 1
    for i in range(len(input_str)):
        if i > chars_before:
            str = input_str[i-chars_before:i+1]
            if not has_duplicates(str):
                return i + 1

def run():
    input_str = file_to_string()
    return get_first_marker(input_str, 4), get_first_marker(input_str, 14)

print(run())