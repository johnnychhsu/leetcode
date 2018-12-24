# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        step = 0
        ans = {}
        res = [(root, 0)]

        def find(ans, res):
            if not res:
                return
            else:
                node, step = res[0]
                del res[0]
                if step in ans:
                    ans[step].append(node.val)
                else:
                    ans[step] = [node.val]
                if node.left:
                    res.append((node.left, step - 1))
                if node.right:
                    res.append((node.right, step + 1))
                find(ans, res)
        find(ans, res)
        
        min_key = min(ans.keys())
        max_key = max(ans.keys())
        
        ans_list = []
        for i in range(min_key, max_key + 1, 1):
            ans_list.append(ans[i])
        return ans_list
