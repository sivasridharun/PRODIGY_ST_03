def print_grid(grid):
    for row in grid:
        print(" ".join(str(n) if n else "." for n in row))

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    box_row, box_col = row//3*3, col//3*3
    return all(grid[r][c] != num for r in range(box_row, box_row+3) for c in range(box_col, box_col+3))

def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if is_valid(grid, r, c, n):
                        grid[r][c] = n
                        if solve(grid): return True
                        grid[r][c] = 0
                return False
    return True

grid = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print("Original:")
print_grid(grid)
if solve(grid):
    print("\nSolved:")
    print_grid(grid)
else:
    print("No solution.")
