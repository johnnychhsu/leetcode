def check_binary_search_tree_(root):
    if not root:
        return True
    from collections import deque
    res = deque()
    def find(node):
        if not node:
            return
        else:
            if node.left:
                find(node.left)
            res.extend([node])
            if node.right:
                find(node.right)
    find(root)
    prev = res.popleft()
    while res:
        cur = res.popleft()
        if cur.data <= prev.data:
            return False
        else:
            prev = cur
    return True
