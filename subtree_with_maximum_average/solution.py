"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.ans = None
        self._max = -float('inf')
        def find(node):
            if not node:
                return (0, 0)
            right_avg, right_num = find(node.right)
            left_avg, left_num = find(node.left)
            cur_value = node.val + right_avg * right_num + left_num * left_avg
            cur_num = 1 + right_num + left_num
            cur_avg = cur_value / cur_num
            if cur_avg > self._max:
                self.ans = node
                self._max = cur_avg
            return (cur_avg, cur_num)
        find(root)
        return self.ans
