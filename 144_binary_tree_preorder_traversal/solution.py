# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [root]
        ans = []
        while res:
            cur = res.pop()
            ans.append(cur.val)
            if cur.right:
                res.append(cur.right)
            if cur.left:
                res.append(cur.left)
        return ans
        