# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def find(node, _min, _max):
            if not _min < node.val < _max:
                return False
            else:
                left = right = True
                if node.left:
                    n_max = min(_max, node.val)
                    left = find(node.left, _min, n_max)
                if node.right:
                    n_min = max(_min, node.val)
                    right = find(node.right, n_min, _max)
                return left and right
        if not root:
            return True
        return find(root, -float('inf'), float('inf'))
