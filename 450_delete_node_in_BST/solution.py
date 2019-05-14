# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        def findRightSmallest(node):
            if node.left:
                return findRightSmallest(node.left)
            else:
                return node.val
        
        def delete(node, key):
            if not node:
                return
            if node.val < key:
                node.right = delete(node.right, key)
            elif node.val > key:
                node.left = delete(node.left, key)
            elif node.val == key:
                if not node.right and not node.left:
                    return None
                if not node.right:
                    return node.left
                temp = findRightSmallest(node.right)
                delete(node, temp)
                node.val = temp
            return node
        return delete(root, key)

                
                
                    
                
                

        
        

        