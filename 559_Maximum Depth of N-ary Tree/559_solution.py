"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        _max = -1
        res = [(root, 1)]
        while res:
            cur, d = res.pop()
            _max = max(d, _max)
            for n in cur.children:
                res.append((n, d + 1))
        return _max
