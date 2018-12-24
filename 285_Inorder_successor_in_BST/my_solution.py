# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur = root
        res = []
        def find(cur, res):
            if cur.right:
                find(cur.right, res)
            res.append(cur)
            if cur.left:
                find(cur.left, res)
        find(root, res)
        while res:
            node = res.pop()
            if node.val == p.val:
                break
        if res:
            return res.pop()
        else:
            return None
        
