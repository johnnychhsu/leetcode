class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(height) - 1
        left_max = 0
        right_max = 0
        ans = 0
        
        while left_pointer < right_pointer:
            left_max = max(left_max, height[left_pointer])
            right_max = max(right_max, height[right_pointer])
            if right_max > left_max:
                ans += left_max - height[left_pointer]
                left_pointer += 1
            else:
                ans += right_max - height[right_pointer]
                right_pointer -= 1
            
        return ans
        
        
