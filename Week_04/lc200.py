class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc, nums_islands = len(grid[0]), 0

        def dfs(r, c):
            grid[r][c] = 0
            nr, nc = len(grid), len(grid[0])
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                    dfs(x, y)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    nums_islands += 1
                    dfs(r, c)

        return nums_islands
