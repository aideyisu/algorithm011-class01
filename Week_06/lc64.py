class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 
        r, c = len(grid), len(grid[0])
        cur = [0] * c
        cur[0] = grid[0][0] 
        for i in range(1, c):
            cur[i] = cur[i-1] + grid[0][i]
        for i in range(1, r):
            cur[0] += grid[i][0]
            for j in range(1, c):
                cur[j] = min(cur[j-1], cur[j]) + grid[i][j]
        return cur[-1]

