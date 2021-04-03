def find_next_empty(sudoku):
    # finds the next row and column where the value is 0
    # returns row, column if there is an empty box or None, None if not
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col

    return None, None


def guess_is_valid(sudoku, guess, row, col):
    # figures out if the guess is valid for the rules of sudoku
    # starting with checking the row
    row_values = sudoku[row]
    if guess in row_values:
        return False

    # checking the column (for each row check col-position)
    column_values = [sudoku[r][col] for r in range(9)]
    if guess in column_values:
        return False

    # checking if guess is in 3x3 matrix, so check if in 0, 1 or 2 row
    row_start = (row // 3) * 3
    # check if in 0, 1 or 2 column
    column_start = (col // 3) * 3
    # check if if guess is in 3x3 matrix
    for r in range(row_start, row_start + 3):
        for c in range(column_start, column_start + 3):
            if guess == sudoku[r][c]:
                return False

    # at this point, the guess is valid
    return True


def solve_sudoku(sudoku):
    # searching for empty (0) boxes
    row, col = find_next_empty(sudoku)

    # check, if there are empty boxes left
    if row is None:
        return True

    # there is an empty box, so make a guess between 1 and 10
    for guess in range(1, 10):
        # check if guess is valid
        if guess_is_valid(sudoku, guess, row, col):
            # set the guess in place
            sudoku[row][col] = guess
            # recursively call the function
            if solve_sudoku(sudoku):
                return True

        # not valid or guess was wrong: backtracking!
        sudoku[row][col] = 0

    # sudoku is unsolvable?
    return False


def print_result(sudoku):
    for i in range(9):
        if i % 3 == 0:
            print("-" * 27)
        row = ""
        for j in range(9):
            if j % 3 == 0:
                row = row + " | "
            row = row + str(sudoku[i][j]) + " "
        print(row)


if __name__ == "__main__":
    sudoku = [
        [5, 0, 1, 0, 7, 0, 3, 9, 0],
        [3, 0, 0, 1, 0, 0, 2, 0, 0],
        [0, 0, 2, 6, 5, 0, 0, 7, 1],
        [1, 6, 4, 9, 3, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 6, 1, 0, 3, 0],
        [0, 3, 0, 0, 0, 4, 9, 0, 8],
        [0, 0, 5, 0, 0, 8, 1, 4, 3],
        [0, 1, 8, 0, 0, 0, 5, 2, 0],
    ]

    print(solve_sudoku(sudoku))
    print_result(sudoku)
