# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(s, e):
            if s > e:
                return None
            mid = s + (e-s) // 2
            root = TreeNode(nums[mid])
            root.left = build(s, mid-1)
            root.right = build(mid + 1, e)
            return root

        root = build(0, len(nums)-1)
        return root
