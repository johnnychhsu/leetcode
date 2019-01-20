class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(s, e):
            left = s
            right = e
            while left <= right:
                mid = (right+left) // 2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
            
        def findIndex():
            if nums[0] < nums[-1]:
                return  -1

            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        if not nums:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        rotate_index = findIndex()
        if rotate_index == -1:
            return binarySearch(0, len(nums) - 1)
        if target > nums[rotate_index]:
            return -1
        else:
            if target == nums[rotate_index]:
                return rotate_index
            elif target >= nums[0]:
                return binarySearch(0, rotate_index)
            else:
                return binarySearch(rotate_index + 1, len(nums) - 1)
        
        
        
