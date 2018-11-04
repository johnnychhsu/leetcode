class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_map = {}
        for task in tasks:
            if task in task_map:
                task_map[task] += 1
            else:
                task_map[task] = 1
        _max = 0
        _key = 0
        for key in task_map.keys():
            if task_map[key] > _max:
                _max = task_map[key]
                _key = key
        task_map[_key] = 0
        step = (n + 1) * (_max - 1) + 1
        for key in task_map.keys():
            if task_map[key] - (_max - 1) > 0:
                task_map[key] -= (_max - 1)
            else:
                task_map[key] = 0
        for key in task_map.keys():
            if task_map[key] != 0:
                step += task_map[key]
        return max(step, len(tasks))
        
            
         
