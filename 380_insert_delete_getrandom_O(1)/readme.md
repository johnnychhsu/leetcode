## 380. Insert delete getrandom O(1)
### Description
Design a data structure that supports all following operations in average O(1) time.

1. insert(val): Inserts an item val to the set if not already present.
2. remove(val): Removes an item val from the set if present.
3. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

### Solution
We can use a list to store the `val`, a dict to record the `val` index in the list. Then if we want to remove, we can simply move the `val` to the tail, then pop it.