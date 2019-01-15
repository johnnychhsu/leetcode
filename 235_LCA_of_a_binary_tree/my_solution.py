# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_list = []
        q_list = []
        cur = root
        while True:
            p_list.append(cur)
            if cur.val > p.val:
                cur = cur.left
            elif cur.val < p.val:
                cur = cur.right
            else:
                break

        cur = root
        while True:
            q_list.append(cur)
            if cur.val > q.val:
                cur = cur.left
            elif cur.val < q.val:
                cur = cur.right
            else:
                break

        mark = 0
        for _p, _q in zip(p_list, q_list):
            if _p.val != _q.val:
                break
            else:
                mark += 1
        return p_list[mark - 1]
                
