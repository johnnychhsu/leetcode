class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from heapq import heappush, heappop
        container = []
        for i in range(len(matrix)):
            heappush(container, (matrix[0][i], 0, i))
        for _ in range(k - 1):
            cur_min = heappop(container)
            if cur_min[1] == len(matrix) - 1:
                continue
            else:
                value = cur_min[0]
                row = cur_min[1]
                col = cur_min[2]
                heappush(container, (matrix[row + 1][col], row + 1, col))
        return heappop(container)[0]

sol = Solution()
a = sol.kthSmallest([[1,2],[1,3]], 3)
print (a)
        
        
