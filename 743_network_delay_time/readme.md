## 743. Network Delay Time
### Description
There are N network nodes, labelled 1 to N.
<br .>
Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
<br />
Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
<br />
Note:
1. `N` will be in the range [1, 100].
2. `K` will be in the range [1, N].
3. The length of times will be in the range [1, 6000].
4. All edges `times[i] = (u, v, w)` will have `1 <= u, v <= N` and `0 <= w <= 100`.

### Solution
1. We need to find the shortest path from init node to all nodes, then return the maximum time. We can use a priority queue.

### Reference
1. [Dijkstra’s Algorithm](https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/)
