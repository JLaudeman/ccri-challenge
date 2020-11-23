# Cell Neighborhoods Challenge
import numpy as np


def mark_neighbors(marked_array, N, cell):
    count = 0
    height, width = marked_array.shape[1:]
    for row in range(cell[1] - N, cell[1] + N + 1):
        for col in range(cell[0] - N + abs(row - cell[1]),
                         cell[0] + N - abs(row - cell[1]) + 1):
            if row >= height:
                row = height - 1
            elif row < 0:
                row = 0
            # To wrap around, allow y-vals to be negative and mod by height
            # if row >= height:
            #    row = row % height
            # elif row < 0:
            #    row = -1 * (abs(row) % height)

            if col >= width:
                col = width - 1
            elif col < 0:
                col = 0
            # wrapping works the same as above
            # if col >= width:
            #    col = col % width
            # elif col < 0:
            #    col = -1 * (abs(col) % width)

            if not marked_array[1][row, col]:
                marked_array[1][row, col] = 1
                count += 1

    return marked_array, count


def find_neighbors(input_array, N):
    height, width = input_array.shape

    # Convert to 3-D array for convenient marking
    marked_array = np.array(
        [input_array, np.zeros(input_array.shape)], ndmin=3, dtype=int)

    # Find positive values, mark and count their neighbors
    # Note, for a rectangular grid, the maximum distance between any two
    # neighbors is the distance between two opposite diagonal squares.
    # If N is equal to that distance or greater, and there is at least
    # one positive value in the grid, then every square will be a neighbor.
    neighbors = 0
    for col in range(width):
        for row in range(height):
            if input_array[row][col] > 0:
                if N < height + width - 2:
                    marked_array, count = mark_neighbors(
                        marked_array, N, (col, row))
                    neighbors += count
                    if neighbors >= height * width:
                        return neighbors
                else:
                    return height * width

    return neighbors
