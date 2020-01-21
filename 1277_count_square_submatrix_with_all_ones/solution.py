class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for x in range(1, len(matrix)):
            for y in range(1, len(matrix[0])):
                if matrix[x][y] > 0:
                    matrix[x][y] *= min(matrix[x-1][y-1], matrix[x][y-1], matrix[x-1][y]) + 1
        return sum(map(sum, matrix))
