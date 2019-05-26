## 105. Construct binary tree from inorder and preorder traversal
### Description
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
```

### Solution
Recursive. Think about the inorder traversal. We know that the first element of preorder traversal is the root, we can use it to separate the inorder traversal array. The left part from the `root` in inorder traversal array are on the left side to the `root`. The right part are on the right side to the `root`. We can utilize this to construct the binary tree.

Looking for index of `root` on inorder traversal takes time, we can first build a hash map to store the index of each value in the array.
