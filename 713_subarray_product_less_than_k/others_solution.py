class Solution:
    def numSubarrayProductLessThanK(self, nums: 'List[int]', k: 'int') -> 'int':
        ans = 0
        left = 0
        prev = 1
        for right in range(0, len(nums)):
            prev *= nums[right]
            while left <= right and prev >= k:
                prev /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
