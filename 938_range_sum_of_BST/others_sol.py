# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if not node:
                return 
            else:
                if L <= node.val <= R:
                    self.ans += node.val
                if node.val > L:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        dfs(root)
        return self.ans
