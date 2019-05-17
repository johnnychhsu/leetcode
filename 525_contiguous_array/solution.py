class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        sum_map = {0:-1}
        _sum = 0
        ans = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum in sum_map:
                ans = max(ans, i - sum_map[_sum])
            else:
                sum_map[_sum] = i
        return ans
