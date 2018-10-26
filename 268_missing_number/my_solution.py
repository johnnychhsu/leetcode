class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        _sum = sum(x for x in range(0, n + 1))
        for n in nums:
            _sum -= n
        return _sum
