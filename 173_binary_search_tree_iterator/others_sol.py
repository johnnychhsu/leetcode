# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        cur = self.stack.pop()
        self.push(cur.right)
        return cur.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False
    
    def push(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
