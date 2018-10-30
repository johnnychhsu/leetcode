# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
This take O(n) time.
"""

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def find(root, cur_sum, target, cache, ans):
            if not root:
                return
            cur_sum += root.val
            previous_path_sum = cur_sum - target
            ans[0] += cache.get(previous_path_sum, 0)
            cache[cur_sum] = cache.get(cur_sum, 0) + 1
            
            find(root.left, cur_sum, target, cache, ans)
            find(root.right, cur_sum, target, cache, ans)
            cache[cur_sum] -= 1
            
        cache = {0:1}
        ans = [0]
        find(root, 0, sum, cache, ans)
        return ans[0]
