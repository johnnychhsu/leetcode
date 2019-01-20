# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def addElement(ans, level, node):
            if level < len(ans):
                ans[level].append(node.val)
            else:
                ans.insert(level, [node.val])
        
        if not root:
            return []
        
        from collections import deque
        res = deque()
        res.extend([(root, 0)])
        ans = []
        while res:
            cur, level = res.popleft()
            addElement(ans, level, cur)
            if cur.left:
                res.extend([(cur.left, level + 1)])
            if cur.right:
                res.extend([(cur.right, level + 1)])
        return ans
