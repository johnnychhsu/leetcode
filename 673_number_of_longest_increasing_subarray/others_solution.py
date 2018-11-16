class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [0] * len(nums)
        number = [0] * len(nums)

        ans = 0
        max_l = 0

        for i in range(len(nums)):
            dp[i] = 1
            number[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1:
                        number[i] += number[j]
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        number[i] = number[j]

            if max_l == dp[i]:
                ans += number[i]
            if max_l < dp[i]:
                max_l = dp[i]
                ans = number[i]
        return ans
    

        
