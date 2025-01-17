def search(grid, word):
    coordinates = find_all_coordinates_for_all_letters(grid, word)

    result = word + ": "

    search_strategies = [
        find_horizontal_forward_coordinate,
        find_horizontal_backward_coordinate,
        find_vertical_downward_coordinate,
        find_vertical_upward_coordinate
    ]

    for i in range(len(coordinates[0])):
        starting_letter_coordinate = coordinates[0][i]
        for st in search_strategies:
            candidate_coordinates = try_coordinates(coordinates, starting_letter_coordinate, st)
            if len(candidate_coordinates) == len(word):
                result += report_coordinates(candidate_coordinates)
                break
    return result


def find_all_coordinates_for_all_letters(grid, word):
    coordinates = []
    for ch in word:
        coordinates.append(locate_in_grid(grid, ch))
    return coordinates


def locate_in_grid(grid, ch):
    coordinates = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ch:
                coordinates.append((i, j))
    return coordinates


def find_horizontal_forward_coordinate(next_letter_coordinates, current_letter_coordinate):
    for j in range(len(next_letter_coordinates)):
        if next_letter_coordinates[j][0] == current_letter_coordinate[0] \
                and next_letter_coordinates[j][1] == current_letter_coordinate[1] + 1:
            return next_letter_coordinates[j]


def find_horizontal_backward_coordinate(next_letter_coordinates, current_letter_coordinate):
    for j in range(len(next_letter_coordinates)):
        if next_letter_coordinates[j][0] == current_letter_coordinate[0] \
                and next_letter_coordinates[j][1] == current_letter_coordinate[1] - 1:
            return next_letter_coordinates[j]


def find_vertical_downward_coordinate(next_letter_coordinates, current_letter_coordinate):
    for j in range(len(next_letter_coordinates)):
        if next_letter_coordinates[j][0] == current_letter_coordinate[0] + 1 \
                and next_letter_coordinates[j][1] == current_letter_coordinate[1]:
            return next_letter_coordinates[j]


def find_vertical_upward_coordinate(next_letter_coordinates, current_letter_coordinate):
    for j in range(len(next_letter_coordinates)):
        if next_letter_coordinates[j][0] == current_letter_coordinate[0] - 1 \
                and next_letter_coordinates[j][1] == current_letter_coordinate[1]:
            return next_letter_coordinates[j]


def try_coordinates(coordinates, current_letter_coordinate, find_next_letter_coordinate):
    candidate_coordinates = [current_letter_coordinate]
    for j in range(1, len(coordinates)):
        next_letter_coordinates = coordinates[j]
        next_letter_coordinate = find_next_letter_coordinate(next_letter_coordinates, current_letter_coordinate)
        if next_letter_coordinate is None:
            break
        else:
            candidate_coordinates.append(next_letter_coordinate)
            current_letter_coordinate = next_letter_coordinate
    return candidate_coordinates


def report_coordinates(coordinates):
    result = ""
    for coordinate in coordinates:
        result += "(" + str(coordinate[0]) + "," + str(coordinate[1]) + ")"
    return result
