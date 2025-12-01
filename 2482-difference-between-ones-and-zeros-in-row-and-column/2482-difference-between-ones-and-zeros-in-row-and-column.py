class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (row[i] + col[j]) -m -n
        return grid