class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        fast = 1
        cur = nums[0]
        l = float('inf')
        while fast < len(nums):
            if cur < s:
                cur += nums[fast]
                fast += 1
            while cur >= s:
                l = min(l, fast - slow)
                cur -= nums[slow]
                slow += 1
        return 0 if l == float('inf') else l
