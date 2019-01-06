## 346. Moving Average from Data Stream
### Queue
My idea is use collections.deque.

### More Efficient
We don't need to sum the queue every time. Using `queue[index % size]`, we can renew the element every time without `deque`.
<br />
Besides, we can maintain `sum` using the `queue[index % size]` to minus the oldest element.
