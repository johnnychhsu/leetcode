class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        table = defaultdict(set)
        for edge in edges:
            s, e = edge
            table[s].add(e)
            table[e].add(s)
        leaves = [key for key in table.keys() if len(table[key]) == 1]
        if not edges:
            return [0]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for l in leaves:
                j = table[l].pop()
                table[j].remove(l)
                if len(table[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
