def unique_paths_with_obstacles(grid):
    rows, cols = len(grid), len(grid[0])
    memo = {}

    def dfs(r, c):
        if r >= rows or c >= cols or grid[r][c] == 1:
            return 0
        if (r, c) == (rows - 1, cols - 1):
            return 1
        if (r, c) in memo:
            return memo[(r, c)]
        memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        return memo[(r, c)]

    return dfs(0, 0)

grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

print(unique_paths_with_obstacles(grid))

#Coded by Suhail
