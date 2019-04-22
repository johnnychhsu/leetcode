## 210. Course schedule II
There are a total of n courses you have to take, labeled from 0 to n-1.
<br />
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`
<br />
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
<br />
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

### Example 1:
```
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
```

### Solution
1. [Topological sort](solution.py)
2. [DFS recurssive solution](others_solution.py)
    The key idea here is to use `visited = []` to indicate whether a node has been visited or is currently in our path. If a node is visited before, then we can return True for this node. However, if this node is currently on our path, then this case means that we found a cycle.
