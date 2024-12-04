def get_count(grid):
    NUMBER_OF_ROWS, NUMBER_OF_COLUMNS = len(grid), len(grid[0])

    count = 0

    def is_valid_row_and_column_index(row_index, column_index):
        return 0 <= row_index < NUMBER_OF_ROWS and 0 <= column_index < NUMBER_OF_COLUMNS

    def are_these_three_points_a_mas(row_index_1, column_index_1,
                                     row_index_2, column_index_2,
                                     row_index_3, column_index_3):
        if is_valid_row_and_column_index(row_index_1, column_index_1) and \
           is_valid_row_and_column_index(row_index_2, column_index_2) and \
           is_valid_row_and_column_index(row_index_3, column_index_3):

            return (grid[row_index_1][column_index_1] == 'M' and grid[row_index_2][column_index_2] == 'A' and grid[row_index_3][column_index_3] == 'S') or \
                   (grid[row_index_1][column_index_1] == 'S' and grid[row_index_2][column_index_2] == 'A' and grid[row_index_3][column_index_3] == 'M')

        return False

    for row_index in range(1, NUMBER_OF_ROWS - 1):
        for col_index in range(1, NUMBER_OF_COLUMNS - 1):
            if are_these_three_points_a_mas(row_index - 1, col_index - 1, row_index, col_index, row_index + 1, col_index + 1) and \
               are_these_three_points_a_mas(row_index - 1, col_index + 1, row_index, col_index, row_index + 1, col_index - 1):
                count += 1

    return count


def main():
    grid = []

    with open('input.txt') as f:
        for line in f:
            grid.append(line.strip())

    grid = [list(row) for row in grid]

    count = get_count(grid)
    print(f"Result: {count}")


if __name__ == '__main__':
    main()