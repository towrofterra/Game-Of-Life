# Jake Levi's Game of Life 8/27/18
import copy

print("Welcome to the Game of Life. This is a one player game")


example_board0 = [[0, 1, 0, 0],
                  [1, 0, 1, 0],
                  [0, 1, 0, 0],
                  [1, 0, 1, 0]]

example_board1 = [[0, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]


# Board -> Board
# Transforms a board of numbers into a board with each number representing the number of live neighbours the cell had
def num_neighbours(b):
    new_b = copy.deepcopy(b)
    for r in range(0, len(b)):
        for c in range(0, len(b[r])):
            if r == 0 and c == 0:
                new_b[r][c] = b[r][c + 1] + b[r + 1][c]

            elif r == 0 and c == len(b[r])-1:
                new_b[r][c] = b[r][c - 1] + b[r + 1][c]

            elif r == 0:
                new_b[r][c] = b[r][c - 1] + b[r][c + 1] + b[r + 1][c]

            elif c == 0 and r == len(b)-1:
                new_b[r][c] = b[r][c + 1] + b[r - 1][c]

            elif c == 0:
                new_b[r][c] = b[r][c + 1] + b[r - 1][c] + b[r + 1][c]

            elif r == len(b)-1 and c == len(b[r])-1:
                new_b[r][c] = b[r][c - 1] + b[r - 1][c]

            elif c == len(b[r])-1:
                new_b[r][c] = b[r][c - 1] + b[r - 1][c] + b[r + 1][c]

            elif r == len(b)-1:
                new_b[r][c] = b[r][c - 1] + b[r][c + 1] + b[r - 1][c]

            else:
                new_b[r][c] = b[r][c-1] + b[r][c+1] + b[r-1][c] + b[r+1][c]
    return new_b


assert num_neighbours(example_board0) == [[2, 0, 2, 0],
                                          [0, 4, 0, 1],
                                          [3, 0, 3, 0],
                                          [0, 3, 0, 1]]

assert num_neighbours(example_board1) == [[0, 0, 1, 0],
                                          [0, 1, 0, 1],
                                          [0, 0, 1, 0],
                                          [0, 0, 0, 0]]


# Board -> Print
# Prints the board nicely
def print_board(b):
    for r in b:
        print(r)


# Board -> Board
# Moves the given board on one tick
def next_gen(b_neighbours, b):

    new_b = copy.deepcopy(b)
    for r in range(0, len(b)):
        for c in range(0, len(b[r])):
            if b[r][c] == 1:
                if b_neighbours[r][c] < 2 or b_neighbours[b][c] == 4:
                    new_b[r][c] = 0
                else:
                    new_b[r][c] = 1
            elif b_neighbours[r][c] == 3:
                new_b[r][c] = 1
    return new_b


assert next_gen(num_neighbours(example_board0), example_board0) == [[0, 0, 0, 0],
                                                                    [0, 0, 0, 0],
                                                                    [1, 0, 1, 0],
                                                                    [0, 1, 0, 0]]

assert next_gen(num_neighbours(example_board1), example_board1) == [[0, 0, 0, 0],
                                                                    [0, 0, 0, 0],
                                                                    [0, 0, 0, 0],
                                                                    [0, 0, 0, 0]]


def main(b=[[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]], gen=0):
    print("\nGeneration ", gen)
    print_board(b)
    b = next_gen(num_neighbours(b), b)
    input("Press enter to continue")
    main(b, gen + 1)


main(example_board0)
