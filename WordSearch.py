def find_coordinates(grid, word):
    coordinates = []
    for ind, ch in enumerate(word):
        coordinates.append(locate_in_grid(grid, ch))
    return coordinates


def locate_in_grid(grid, ch):
    coordinates = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ch:
                coordinates.append((i, j))
    return coordinates


def try_coordinates(coordinates, i):
    candidate_coordinates = []
    current_letter_coordinate = coordinates[0][i]
    candidate_coordinates.append(current_letter_coordinate)
    for j in range(i + 1, len(coordinates)):
        next_letter_coordinates = coordinates[j]
        next_letter_coordinate = find_next_horizontal_coordinate(next_letter_coordinates, current_letter_coordinate)
        if next_letter_coordinate is None:
            break
        else:
            candidate_coordinates.append(next_letter_coordinate)
            current_letter_coordinate = next_letter_coordinate
    return candidate_coordinates


def find_next_horizontal_coordinate(next_letter_coordinates, current_letter_coordinate):
    for j in range(len(next_letter_coordinates)):
        if next_letter_coordinates[j][0] == current_letter_coordinate[0] \
                and next_letter_coordinates[j][1] == current_letter_coordinate[1] + 1:
            return next_letter_coordinates[j]


def search(grid, word):
    coordinates = find_coordinates(grid, word)

    result = word + ": "

    for i in range(len(coordinates[0])):
        candidate_coordinates = try_coordinates(coordinates, i)
        if len(candidate_coordinates) == len(word):
            for coordinate in candidate_coordinates:
                result += "(" + str(coordinate[0]) + "," + str(coordinate[1]) + ")"
    return result
