"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20×20 grid?
    - solutuion is symmetric about the diagonal
    # https://www.xarg.org/puzzle/project-euler/problem-15/
"""
import math
# (2n / k) = 2n!/k!(n-k)!

#using pascals triangle and combinatorics:

def pascals_combo_2(grid):
    i = 1
    c = 1
    while i <= grid:
        c = c*(grid + i)/i
        i += 1
    return c
    
print(pascals_combo_2(20))