## 207. Course Schedule
There are a total of n courses you have to take, labeled from 0 to n-1.
<br />
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
<br />
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

```command
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible
```

### Solution 
1. DFS
2. Topological sort [Accepted]
    This is better solution. It takes O(V+E) time and space. The idea is simple, we always take those classes with no prerequisities until no such classes. If courses taken equals to total courses, then we are done, else it is impossible to take all.
