### 142. Linked List Cycle II
First use two pointers to detect whether there is a cycle or not. 
Pointer `slow` take one step each time, while pointer `fast` take two steps each time. If there is no cycle, then the fast will reach `None` first. 
If there is a cycle, suppose `slow` and `fast` meet when `slow` go through `s` steps. 
Then `fast` take `2s` steps. So, `steps by fast` - `step by slow` = `2s - s = s`. 
`fast` walks `s` more steps than `slow`. So now, we set another pointer called `run`, start from head.
That is, `run = head`. Let `run` and `slow` walk one step each time simoutaneously. 
They will meet each other at the node where cycle begins. 
The reason is that because at the node `fast` and `slow` meet, `fast` walks `s` steps more. 
Thus from the same node, the slow walks `s` more steps will reach the node they meet again. 
So now the `run` is like the `slow` in the begining. `run` and `slow` will reach the node that is the start of cycle at the same time.
