class Solution:
    def regionsBySlashes(self, grid):
        N = len(grid)
        extend_N = N * 3
        num_map = [[0 for _ in range(extend_N)] for _ in range(extend_N)]
        for row in range(N):
            for col in range(N):
                if grid[row][col] == '/':
                    for i in range(3):
                        num_map[row*3+i][col*3+2-i] = 1
                elif grid[row][col] == '\\':
                    for i in range(3):
                        num_map[row*3+i][col*3+i] = 1
        
        def isValid(row, col):
            if 0 <= row < extend_N and 0 <= col < extend_N:
                return True
            else:
                return False
        
        def find(row, col):
            if isValid(row, col) and num_map[row][col] == 0:
                num_map[row][col] = 1
                find(row+1, col)
                find(row-1, col)
                find(row, col+1)
                find(row, col-1)
        total = 0
        for row in range(extend_N):
            for col in range(extend_N):
                if num_map[row][col] == 0:
                    find(row, col)
                    total += 1
        return total
sol = Solution()
print(sol.regionsBySlashes([" /","/ "]))

