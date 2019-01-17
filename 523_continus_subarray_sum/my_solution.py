class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        acu = 0
        if k == 0:
            for i in range(len(nums)):
                acu = nums[i]
                for j in range(i+1, len(nums)):
                    acu += nums[j]
                    if acu == 0:
                        return True
        else:
            for i in range(len(nums)):
                acu = nums[i]
                for j in range(i+1, len(nums)):
                    acu += nums[j]
                    if acu % k == 0:
                        return True
        return False
            
