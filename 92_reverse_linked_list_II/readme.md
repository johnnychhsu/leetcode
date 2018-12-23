### 92. Reverse Linked List II
The idea is that, once the partial nodes reversed, then we only need to consider the left nodes, which means that we only need to move the left nodes one by one to the front, then it is done.

Thus, we have to record the previous node of the reverse segment, make its next points to the next node of the two nodes that are currently swap.

Once two nodes are swap, we only need to connect the previous one to the swap one, then it's done.
