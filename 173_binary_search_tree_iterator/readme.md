## 173. Binary Search Tree Iterator
`next()` and `hasNext()` should be average O(1). So we can maintain a stack, then check whether there is next smallest is O(1). <br />
As for `next()`, in the init, we push all node's that are left, and their left child and root into the stack. Then the space is O(h). Each we call `next()`, we just pop it, and check its right child, then do the same thing as init to the right child. 
<br />
The worst case for this `next()` is O(n), because we push all left child into stack. But the average case is O(1). Since the worst case is that all node are connect directly, and all are left child of their parent. <br />
So, if we do this to n node, the average time is `n/n = 1`.
