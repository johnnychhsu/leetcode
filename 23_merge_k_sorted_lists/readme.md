## 23. Merge K Sorted Lists
1. Using priority queue (min heap) : I use heapq. What's worth noting is that, if we use `heapq.heappush([], (1,'a'))`, `1` will be the priority criteria. IF there are two element that has the same priority, then it will check the next element, which in this case is `a`. <br />
Thus, to avoid this problem, we can add one more item in the tuple, for example, add the added order like `(1, 0, 'a')`, the order is unique.
2. Divide and conquer. Merge two list within different pairs, so each iteration will reduce the number of lists into `n/2`.

