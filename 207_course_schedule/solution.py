class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        come = defaultdict(list)
        out = [0 for _ in range(numCourses)]
        
        for e in prerequisites:
            des, src = e
            come[src].append(des)
            out[des] += 1
        
        res = []
        for n in range(numCourses):
            if out[n] == 0:
                res.append(n)
        taken = 0
        while res:
            src = res.pop()
            taken += 1
            for des in come[src]:
                out[des] -= 1
                if out[des] == 0:
                    res.append(des)
        return taken == numCourses
