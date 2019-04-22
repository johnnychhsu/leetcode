class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        condition = defaultdict(list)
        nums = [0 for _ in range(numCourses)]
        for pre in prerequisites:
            des, src = pre
            condition[src].append(des)
            nums[des] += 1

        res = []
        for i in range(numCourses):
            if nums[i] == 0:
                res.append(i)
        order = []
        while res:
            src = res.pop()
            nums[src] -= 1
            order.append(src)
            for des in condition[src]:
                nums[des] -= 1
                if nums[des] == 0:
                    res.append(des)
        
        return order if len(order) == numCourses else []
