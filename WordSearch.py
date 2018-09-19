def locate_in_grid(grid, ch):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ch:
                return i, j


def search(grid, word):
    positions = []
    for ind, ch in enumerate(word):
        positions.append(locate_in_grid(grid, ch))

    result = word + ": "

    for position in positions:
        result += "(" + str(position[0]) + "," + str(position[1]) + ")"

    return result
