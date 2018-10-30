# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def find(root, history, target, ans):
            history = [x + root.val for x in history] + [root.val]
            for num in history:
                if num == target:
                    ans[0] += 1
            if root.left:
                find(root.left, history, target, ans)
            if root.right:
                find(root.right, history, target, ans)
                
        ans = [0]
        if not root:
            return 0
        find(root, [], sum, ans)
        return ans[0]
            
            
