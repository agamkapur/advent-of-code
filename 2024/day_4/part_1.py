WORD_TO_FIND = "XMAS"
LENGTH_OF_WORD_TO_FIND = len(WORD_TO_FIND)


def is_word_present_at_location_direction(number_of_rows, number_of_columns, row_index, column_index,
    row_direction, column_direction, grid):
    for i in range(LENGTH_OF_WORD_TO_FIND):
        new_row_index, new_column_index = row_index + i * row_direction, column_index + i * column_direction
        if new_row_index < 0 or new_row_index >= number_of_rows or new_column_index < 0 or \
                new_column_index >= number_of_columns or grid[new_row_index][new_column_index] != WORD_TO_FIND[i]:
            return False
    return True


def get_count(grid):
    locations = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]

    number_of_rows, number_of_columns = len(grid), len(grid[0])

    count = 0

    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            for row_direction, column_direction in locations:
                if is_word_present_at_location_direction(number_of_rows, number_of_columns, row_index, column_index,
                    row_direction, column_direction, grid):
                    count += 1

    return count


def main():
    grid = []

    with open('input.txt') as f:
        for line in f:
            grid.append(line.strip())

    grid = [list(row) for row in grid]
    count = get_count(grid)
    print(f"Result : {count}")


if __name__ == '__main__':
    main()