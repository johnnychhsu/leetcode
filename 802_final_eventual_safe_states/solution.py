class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        from collections import defaultdict
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)
        
        def find(cur):
            if color[cur] != WHITE:
                return color[cur] == BLACK
            color[cur] = GRAY
            for nei in graph[cur]:
                if color[nei] == GRAY or not find(nei):
                    return False
            color[cur] = BLACK
            return True
        return list(filter(find, range(len(graph))))
                    
