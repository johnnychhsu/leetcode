class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def _reverse(i):
            left = len(nums) - 1
            right = i
            while left > right:
                nums[left], nums[right] = nums[right], nums[left]
                left -= 1
                right += 1

        swap_index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                swap_index = i
                break
        if swap_index == -1:
            nums.sort()
        else:
            for i in range(len(nums) - 1, swap_index, -1):
                if nums[i] > nums[swap_index]:
                    nums[swap_index], nums[i] = nums[i], nums[swap_index]
                    break
            _reverse(swap_index + 1)
