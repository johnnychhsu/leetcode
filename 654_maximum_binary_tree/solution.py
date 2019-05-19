# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def build(root, left_array, right_array):
            root = TreeNode(root)
            
            if left_array:
                left_max = max(left_array)
                left_index = left_array.index(left_max)
                root.left = build(left_max, left_array[0: left_index], left_array[left_index + 1:])
            
            if right_array:
                right_max = max(right_array)
                right_index = right_array.index(right_max)
                root.right = build(right_max, right_array[0: right_index], right_array[right_index + 1:])
            
            return root
    
        if not nums:
            return None
        _max = max(nums)
        _max_index = nums.index(_max)
        root = build(_max, nums[0: _max_index], nums[_max_index + 1:])
        return root
