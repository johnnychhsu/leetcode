class Solution:
    def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
        i = 0
        ans = []
        while i < len(nums):
            n = nums[i]
            if nums[i] == i + 1 or n == -1:
                i += 1
            elif nums[i] == nums[n - 1]:
                ans.append(n)
                nums[n - 1] = -1
                i += 1
            else:
                nums[i], nums[n-1] = nums[n-1], nums[i]
        return ans
