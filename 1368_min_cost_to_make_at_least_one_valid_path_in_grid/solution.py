class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        cost = 0
        dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        bfs = []
        
        def find(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or dp[x][y] != float('inf'):
                return
            dp[x][y] = cost
            bfs.append((x, y))
            find(x + dirc[grid[x][y] - 1][0], y + dirc[grid[x][y] - 1][1])
        find(0, 0)
        while bfs:
            cost += 1
            bfs, bfs2 = [], bfs
            [find(x+i, y+j) for x, y in bfs2 for i, j in dirc]
            
        return dp[-1][-1]

