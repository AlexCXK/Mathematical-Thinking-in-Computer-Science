# 1 represents /, 2 represents \, 0 empty cell
from timeit import default_timer as timer

# board size n x n
n = 5

# number of diagonals to place
d = 16

# number of solutions found so far
num_sol = 0

# initialise board of size (n+2) x (n+2), to create a frame of empty cells
# to make checks of adjacent cells easier
board = []
for i in range(0, n + 2):
    row = [0] * (n + 2)
    board.append(row)


# print board
def print_board():
    print("\u250C", end="")  # ┌
    for i in range(n - 1):
        print("\u2500\u2500\u2500\u252C", end="")  # ───┬
    print("\u2500\u2500\u2500\u2510")  # ─┐
    for row in range(1, n + 1):
        print("\u2502", end="")  # │
        for col in range(1, n + 1):
            if board[row][col] == 1:
                print(" / ", end="")
            elif board[row][col] == 2:
                print(" \\ ", end="")
            else:
                print("   ", end="")
            print("\u2502", end="")  # │
        print()
        if row == n:
            print("\u2514", end="")  # └
            for i in range(n - 1):
                print("\u2500\u2500\u2500\u2534", end="")  # ──┴
            print("\u2500\u2500\u2500\u2518")  # ──┘
        else:
            print("\u251C", end="")  # ├
            for i in range(n - 1):
                print("\u2500\u2500\u2500\u253C", end="")  # ──┼
            print("\u2500\u2500\u2500\u2524")  # ──┤


# check if given value can be placed in given cell
def is_valid(y, x, val):
    if val == 0:
        return True

    # check upper, lower, left, right:
    # cannot have two diagonals with different incline, regadless of the value being placed
    # i.e. new value_new + value_adjacent cannot be equal to 3
    if board[y][x - 1] + val == 3 or board[y][x + 1] + val == 3 or board[y - 1][x] + val == 3 or board[y + 1][
        x] + val == 3:
        return False
    # if upper-left or lower-right is 2, cannot place 2
    if board[y - 1][x - 1] + val == 4 or board[y - 1][x - 1] + val == 4:
        return False
    # if upper-right or lower-left is 1, cannot place 1
    if val == 1 and (board[y + 1][x - 1] + val == 2 or board[y - 1][x + 1] + val == 2):
        return False

    # otherwise, can place value
    return True


# place diagonal in a given cell
# curr_diag: number of diagonals already placed
def place_diag(y, x, curr_diag, cells_left):
    # is the number of empty cells left less than the number of unplaced diagonals?
    # it's faster to pass the number of cells as a parameter than to calculate it each time
    if cells_left < d - curr_diag:
        return

    # have all required diagonals already been placed?
    if curr_diag == d + 1:
        global num_sol
        num_sol += 1
        print(f"Found solution #{num_sol}")
        print_board()
        print()
        return

    # have we covered all board?
    if y == n + 1:
        return

        # calculate next position
    next_x = x + 1
    next_y = y
    if next_x > n:
        next_x = 1
        next_y += 1

    for val in (2, 1, 0):
        if is_valid(y, x, val):
            # place diagonal
            board[y][x] = val
            # go to the next cell
            next_diag = curr_diag
            if val != 0:
                next_diag += 1
            place_diag(next_y, next_x, next_diag, cells_left - 1)
            board[y][x] = val
    return


start_time = timer()
place_diag(1, 1, 1, 25)
end_time = timer()
print(f"Time elapsed: {end_time - start_time} s")