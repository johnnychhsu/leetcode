# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        def getList(history):
            cur = root
            ans = [root.val]
            for i in history:
                if i == 'l':
                    cur = cur.left
                    ans.append(cur.val)
                else:
                    cur = cur.right
                    ans.append(cur.val)
            return ans
            
        def find(curNode, _sum, history):
            if _sum == sum and not curNode.left and not curNode.right:
                ans.append(getList(history))
            for n in [(curNode.left, 'l'), (curNode.right,'r')]:
                if n[0]:
                    l = len(history)
                    history += n[1]
                    find(n[0], _sum + n[0].val, history)
                    history = history[0:l]
            return

        ans = []
        find(root, root.val, '')
        return ans
