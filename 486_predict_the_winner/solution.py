class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) <= 2:
            return True
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]

        def find(i, j):
            if i == j:
                return nums[i]
            if j == i + 1:
                return max(nums[i], nums[j])
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = max(nums[i] + min(find(i + 1, j - 1), find(i + 2, j)),
                           nums[j] + min(find(i + 1, j - 1), find(i, j - 2)))
            return dp[i][j]

        target = sum(nums) // 2 + 1 if sum(nums) % 2 == 1 else sum(nums) // 2
        return find(0, len(nums) - 1) >= target



