import challenge
import cProfile
import numpy as np


def run_example(size, N, positive_cells=[]):
    example_array = np.zeros(size, dtype=int)
    for cell in positive_cells:
        example_array[cell[0], cell[1]] = 1
    print(example_array,
          f"\nNumber of neighbors: {challenge.find_neighbors(example_array, N)},"
          f" N = {N}")


print("Example 1:")
run_example((11, 11), 3, [(5, 5)])

print("Example 2:")
run_example((11, 11), 3, [(5, 1)])

print("Example 3:")
run_example((11, 11), 2, [(4, 8), (8, 4)])

print("Example 4:")
run_example((11, 11), 2, [(6, 5), (7, 3)])

print("Example 5:")
run_example((25, 1), 3, [(5, 0), (4, 0), (3, 0), (24, 0)])

print("Example 6:")
run_example((11, 11), 100000, [(5, 5)])

print("Example 7:")
run_example((100, 100), 0, [(25, 25)])

print("Example 8:")
run_example((8, 8), 2, [(0, 0), (7, 7), (7, 0), (0, 7)])

print("Example 9:")
run_example((1000, 1000), 0, [(0, 0)])

print("Example 10:")
run_example((1, 1), 0, [(0, 0)])

print("Example 11:")
run_example((11, 11), 3, [(4, 4), (4, 3), (3, 4), (3, 3)])

# Stopping earlier because N is large:
print("Example 12: ")
run_example((10, 10), 18, [(0, 0)])

# An example of a case where a larger N does not include every cell
print("Example 13: ")
run_example((10, 10), 17, [(0, 0)])

# print("This one may take a while...")
# print("Example 14: timing a large array (10000x10000):")
# example_array = np.zeros((10000, 10000))
# cProfile.run("challenge.find_neighbors(example_array, 0)")

# A very bad case, returning early (once all cells are marked) helps, but...
print("Example 15:")
example_array = np.full((100, 100), 1)
cProfile.run('challenge.find_neighbors(example_array, 197)')

# With an array of only positive values and a "middle" N value,
# the worst case time rears its head
# 100x100 is about 10 seconds, 200x200 with N = 100 is about 2-3 minutes
print("Example 16:")
example_array = np.full((100, 100), 1)
cProfile.run('challenge.find_neighbors(example_array, 50)')
