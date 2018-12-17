class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        left = right = current = 0
        limit = 2
        l = len(tree)
        visited_type = []
        _max = 0
        
        while right < l:
            if tree[right] in visited_type:
                right += 1
            elif len(visited_type) < limit:
                visited_type.append(tree[right])
                right += 1
            else:
                _max = max(_max, right - current)
                target = tree[right - 1]
                visited_type = [target]
                while left < right:
                    if tree[left] != target:
                        left += 1
                        current = left
                    else:
                        left += 1
                left = current
        _max = max(_max, right - current)
        return _max
        
