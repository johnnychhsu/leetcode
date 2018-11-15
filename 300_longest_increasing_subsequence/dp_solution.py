def lengthOfLIS(nums):
    dp = [0] * len(nums)
    for i in range(len(nums)):
        max_l = 0
        for j in range(i):
            if nums[j] > nums[i]:
                max_l = max(max_l + 1, dp[j])
        dp[i] = max_l + 1
    return max(dp)


