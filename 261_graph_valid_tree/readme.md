## 261. Graph Valid Tree
Given `n` nodes labeled from `0` to `n-1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
<br />
A valid tree has following properties:
1. No cycle
2. All vertice connect together

### Union Find
A disjoint set data structure keeps track of a set of elements partitioned into number of disjoint subsets. There are two operations : 
1. Find : Determine which subset an element is in
2. Union : Union two subsets into one subset

Thus we can use union find to tell whether there are cycle in a undirected graph. <br />
Every vertex should be in different subset with only one element. Then we loop through all edges. Each time we receive an edge, the two nodes should be in different edge if there is no cycle. <br />
After checking, we put them into the same subset by making one of the node as the parent of another node. We keep tracking the nodes' parent. If we encounter an edge having two nodes that have the same parent, that means they are already in the same subset, which means that there is a cycle.

### BFS or DFS
We can record adjcent nodes of each node. Then we check the graph using DFS or DFS. Using `visited` to mark nodes already checked, using `parent` to record the parent of nodes in each round of seaching.

### Union Find Improvement
The original union find takes O(n) for each edge, this can be improved to O(logn).
1. Union by rank
2. Path Compression

### Reference
[Union Find](https://www.geeksforgeeks.org/union-find/)
