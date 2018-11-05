"""
Watch the nums index
"""
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-1)
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == i:
                i += 1
            elif nums[i] > 0 and nums[i] < l and nums[nums[i]] == nums[i]:
                nums[i] = 0
            elif nums[i] > 0 and nums[i] < l:
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
            else:
                i += 1

        for i in range(1, l):
            if nums[i] != i:
                return i
        return l
import pdb
sol = Solution()
print (sol.firstMissingPositive([2,1,0]))
