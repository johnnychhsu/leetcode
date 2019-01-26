## Valid BST
1. Solve by inorder traversal
2. Maintain upper and lower bound, then check each node.
```python
def validBST(root):
    def find(node, lower, upper):
        if not node:
            return True
        else:
            return find(node.left, lower, node.val) and find(node.right, node.val, upper)
    return find(root, -float('inf'), float('inf'))
```
