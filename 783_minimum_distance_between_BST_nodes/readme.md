## 783. Minimum distance between BST nodes
### Description
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

### Solution
Inorder traversal. We need to calculate the largest node in left subtree and smallest node in right subtree, thus we can calculate both in inorder traversal. This takes O(n) time.
