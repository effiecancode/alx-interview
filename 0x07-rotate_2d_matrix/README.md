# Rotate_2d_matrix
## Solution:
* Transpose the Matrix: The first step is to transpose the matrix.
* Transposing a matrix involves swapping its rows with columns.
* This can be done by iterating over the rows and columns and swapping the elements at position [i][j] with [j][i].
* Reverse Each Row: After transposing, each row of the matrix is now in the correct position for a 90-degree clockwise rotation. However, the rows themselves are in the wrong order.
* To correct this, we reverse each row.
* This approach is more straightforward and avoids the complexities of manually swapping elements in a nested loop.

* Example Usage:
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

rotated_matrix = rotate_2d_matrix(matrix)
print(rotated_matrix)
* This will output:
```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```
* This demonstrates that the matrix has been rotated 90 degrees clockwise as intended.