# Definition for a binary tree node.
import pdb

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def find(root, value, record, found):
            if root == value:
                return True
            if root.left and not found:
                record.append('l')
                found = find(root.left, value, record, found)
                if not found:
                    record.pop()
            if root.right and not found:
                record.append('r')
                found = find(root.right, value, record, found)
                if not found:
                    record.pop()
            return found
 
        record_p = []
        record_q = []
        find(root, p, record_p, False)
        find(root, q, record_q, False)

        print (record_p)
        print (record_q)

        lcp = []
        index = 0
        for dir_p, dir_q in zip(record_p, record_q):
            if dir_p != dir_q:
                break
            else:
                index += 1
        lcp = record_p[0: index]
        ans = root
        for direction in lcp:
            if direction == 'l':
                ans = ans.left
            else:
                ans = ans.right
        return ans
             
a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(0)
g = TreeNode(8)
h = TreeNode(7)
j = TreeNode(4)
a.left = b
a.right = c
b.left = d
b.right = e
e.left = h
e.right = j
c.left = f
c.right = g
sol = Solution()
sol.lowestCommonAncestor(a, b, j)         
