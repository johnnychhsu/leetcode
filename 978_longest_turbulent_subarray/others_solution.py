class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        increase = 1
        decrease = 1
        ans = 1
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                decrease = increase + 1
                increase = 1
            elif A[i] > A[i-1]:
                increase = decrease + 1
                decrease = 1
            else:
                increase = 1
                decrease = 1
            ans = max(ans, max(increase, decrease))
        return ans
            
