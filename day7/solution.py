def file_to_string():
    input_file = open('input.txt', 'r')
    return input_file.read()

def get_all_terminal_lines(input_str):
    return input_str.split('\n')

class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.sub_dirs = []
        self.files = []
        self.size = 0  # represents the size of only files in this directory, not subdirectories

    def _print(self):
        print(self.name,
              self.parent.name if self.parent else None,
              [d.name for d in self.sub_dirs],
              self.files,
              self.size)

def generate_file_structure(terminal_lines):
    folders = []
    current_folder, previous_folder = None, None

    for line in terminal_lines:
        components = line.split(' ')
        if components[0] == '$' and components[1] == 'cd':
            if components[2] == '..':
                current_folder = previous_folder
                if previous_folder:
                    previous_folder = previous_folder.parent
                else:
                    previous_folder = None
            else:
                folder_name = components[2]
                if folder_name not in folders:
                    new_f = Folder(folder_name, current_folder)
                    folders.append(new_f)
                    if current_folder:
                        current_folder.sub_dirs.append(new_f)
                previous_folder = current_folder
                current_folder = new_f
        elif components[0] == '$' and components[1] == 'ls':
            continue
        elif components[0] == 'dir':
            folder_name = components[1]
            new_f = Folder(folder_name, current_folder)
            if new_f not in folders:
                folders.append(new_f)
                if current_folder:
                    current_folder.sub_dirs.append(new_f)
        else:
            current_folder_files = current_folder.files
            if (components[0], components[1]) not in current_folder_files:
                current_folder.files.append((components[0], components[1]))
                current_folder.size += int(components[0])


    return folders

def get_folder_size_total(folder):
    total = 0
    for sub in folder.sub_dirs:
        total += get_folder_size_total(sub)
    return total + folder.size

def get_file_sum(folders):
    sum = 0
    for f in folders:
        total_f_size = get_folder_size_total(f)
        if total_f_size <= 100000:
            sum += total_f_size

    return sum


def get_directory_to_delete(folders):
    folder_sizes = []
    total_storage = get_folder_size_total(folders[0])
    free_storage = 70000000 - total_storage
    space_needed = 30000000 - free_storage
    for f in folders[1:]:
        folder_sum = get_folder_size_total(f)
        if folder_sum >= space_needed:
            folder_sizes.append(folder_sum)

    return min(folder_sizes)

def run():
    input_str = file_to_string()
    term_lines = get_all_terminal_lines(input_str)
    folders = generate_file_structure(term_lines)
    return get_file_sum(folders), get_directory_to_delete(folders)

print(run())
