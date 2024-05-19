# Island Perimeter

## Overview

The island_perimeter function calculates the perimeter of an island represented within a grid. The grid consists of integers where 0 represents water and 1 represents land (or an island). Each cell in the grid is considered a square with a side length of 1. The grid is rectangular, with its width and height not exceeding 100, and it is completely surrounded by water. There is either one island or none at all, and the island does not contain any lakes.
Function Signature

```
def island_perimeter(grid)

Parameters

    grid (list[list[int]]): A 2D list representing the grid. Each element in the grid is an integer where 0 indicates water and 1 indicates land.

Returns

    int: The total perimeter of the island(s).
```

* Detailed Description

The function iterates through each cell in the grid. If the current cell contains land (1), it checks the neighboring cells (up, down, left, right) to determine if they are water (0). If a neighboring cell is water, it increments the perimeter count because that edge contributes to the island's boundary.
Edge Cases

    If the grid is empty (None or an empty list), the function returns 0, as there is no island to calculate the perimeter for.
    The grid is assumed to be fully surrounded by water, so we do not need to check the edges of the grid explicitly.

* Algorithm

    Initialize a variable perimeter to 0.
    Iterate over each cell in the grid using two nested loops.
    For each land cell (1), increment the perimeter count based on the following conditions:
        If the cell is at the top row (i <= 0) or the cell above it is water (grid[i - 1][j] == 0), increment the perimeter.
        If the cell is at the bottom row (i >= len(grid) - 1) or the cell below it is water (grid[i + 1][j] == 0), increment the perimeter.
        If the cell is at the leftmost column (j <= 0) or the cell to its left is water (grid[i][j - 1] == 0), increment the perimeter.
        If the cell is at the rightmost column (j >= len(grid[i]) - 1) or the cell to its right is water (grid[i][j + 1] == 0), increment the perimeter.
    Return the total perimeter.

* Example

Given the following grid:
```
[[0, 1, 0],
 [0, 1, 0],
 [0, 1, 0]]
```
The function would return 4, as the island has a perimeter of 4 units.
* Limitations

This implementation assumes that the grid dimensions do not exceed 100x100 and that there is only one island or none at all. It also assumes that the grid is fully surrounded by water.