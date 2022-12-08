def file_to_string():
    input_file = open('input.txt', 'r')
    return input_file.read()

def get_tree_grid(input_str):
    # [[0, 2, 3],
    #  [1, 3, 4],
    #  [9, 1, 6]]
    return input_str.split('\n')

def is_tree_visible(grid, row, column):
    num_columns = len(grid[0]) # column
    num_rows = len(grid)   # row
    tree_height = grid[row][column]

    vis_left = True
    for i in range(column):
        if grid[row][i] >= tree_height:
            vis_left = False

    vis_right = True
    for i in range(column+1, num_columns):
        if grid[row][i] >= tree_height:
            vis_right = False

    vis_top = True
    for i in range(row):
        if grid[i][column] >= tree_height:
            vis_top = False

    vis_bottom = True
    for i in range(row+1, num_rows):
        if grid[i][column] >= tree_height:
            vis_bottom = False

    return vis_left or vis_right or vis_top or vis_bottom

def get_visible_trees(grid):
    num_columns = len(grid[0]) # column
    num_rows = len(grid)   # row

    visible_trees_count = 0

    for i in range(num_rows):
        for j in range(num_columns):
            if i in {0, num_rows-1} or j in {0, num_columns-1}:
                visible_trees_count += 1
            elif is_tree_visible(grid, i, j):
                visible_trees_count += 1

    return visible_trees_count

def get_scenic_score(grid, row, column):
    num_columns = len(grid[0]) # column
    num_rows = len(grid)   # row
    tree_height = grid[row][column]

    vis_left = column
    for i in reversed(range(column)):
        if grid[row][i] >= tree_height:
            vis_left = column - i
            break

    vis_right = num_columns - 1 - column
    for i in range(column+1, num_columns):
        if grid[row][i] >= tree_height:
            vis_right = i - column
            break

    vis_top = row
    for i in reversed(range(row)):
        if grid[i][column] >= tree_height:
            vis_top = row - i
            break

    vis_bottom = num_rows - 1 - row
    for i in range(row+1, num_rows):
        if grid[i][column] >= tree_height:
            vis_bottom = i - row
            break
    # print(vis_left, vis_right, vis_top, vis_bottom)
    return vis_left * vis_right * vis_top * vis_bottom

def get_scenic_tree(grid):
    num_columns = len(grid[0]) # column
    num_rows = len(grid)   # row

    most_scenic = 0

    for i in range(num_rows):
        for j in range(num_columns):
            if i in {0, num_rows-1} or j in {0, num_columns-1}:
                continue
            score = get_scenic_score(grid, i, j)
            if score > most_scenic:
                most_scenic = score

    return most_scenic

def run():
    input_str = file_to_string()
    trees = get_tree_grid(input_str)
    return get_visible_trees(trees), get_scenic_tree(trees)

print(run())
