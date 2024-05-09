#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    takes grid an an argument: grid is a list of intergers
    0 represents water
    1 represents island
    each cell is a square, with a side length of 1
    cells are connected horizontally/vertically not diagonaly
    grid is rectangular, with its width and height not exceeding 100
    grid is completely surrounded with water
    there is only one island or nothing
    islands have no lakes
    """

    if not grid:
        return 0

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    perimeter += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    perimeter += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    perimeter += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    perimeter += 1

    return perimeter
