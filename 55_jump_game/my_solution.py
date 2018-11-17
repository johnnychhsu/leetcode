class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        des = len(nums) - 1
        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= des:
                des = index
        if des == 0:
            return True
        else:
            return False
            
