class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        dp = [[-1 for _ in range(w)] for _ in range(h)]
        
        if obstacleGrid[h-1][w-1] != 1:
            dp[h-1][w-1] = 1
        else:
            return 0

        def isValid(x, y):
            if 0 <= x < h and 0 <= y < w and obstacleGrid[x][y] != 1:
                return True
            else:
                return False
        
        def find(x, y):
            if not isValid(x, y):
                return 0
            if dp[x][y] != -1:
                return dp[x][y]
            
            right = 0
            down = 0
            if isValid(x+1, y):
                right = find(x+1, y)
            if isValid(x, y+1):
                down = find(x, y+1)
            dp[x][y] = right + down
            return dp[x][y]
    
        return find(0, 0)
            
        
        
