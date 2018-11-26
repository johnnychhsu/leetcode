### 378. K Smallest Element In Sorted Matrix
#### Min Heap Solution
Ref : Python heapq
We can use heapq for priority queue, or modify the __lt__ for a class for priority.

#### Binary Search
We count how many elements are less or equal to the mid value.
First get the mid by calculating `(matrix[0][0] + matrix[n - 1][n - 1]) / 2`
