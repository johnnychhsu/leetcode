class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def find(graph, cur, index, ans):
            cur_node = graph[index]
            cur.append(index)
            if cur[-1] == len(graph) - 1:
                ans.append(cur)
                return
            last_step = len(cur)
            for i in cur_node:
                find(graph, cur, i, ans)
                cur = cur[0: last_step]

        ans = []
        find(graph, [], 0, ans)
        return ans
                
