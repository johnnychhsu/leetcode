class Solution:
    def findLengthOfLCIS(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        left = 0
        right = 1
        ans = 1
        while right < len(nums):
            if nums[right] > nums[right - 1]:
                right += 1
            else:
                ans = max(ans, right - left)
                left = right
                right += 1
        if left != right - 1:
            ans = max(ans, right - left)
        return ans
                
                
