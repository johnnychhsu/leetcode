def minimumAverage(customers):
    import heapq
    length = len(customers)
    tasks = []
    customers.sort()
    customers.reverse()
    pq = []
    cur = 0
    total = 0
    while customers or pq:
        while customers and customers[-1][0] <= cur:
            c = customers.pop()
            c.reverse()
            heapq.heappush(pq, c)
        if pq:
            operation, come = heapq.heappop(pq)
            wait = cur - come
            total += wait + operation
            cur += operation
        else:
            c = customers.pop()
            total += c[1]
            cur = sum(c)
    return total // length
