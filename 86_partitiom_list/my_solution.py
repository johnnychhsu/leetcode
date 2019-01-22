# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(-1)
        large = ListNode(-1)
        small_dummy = small
        large_dummy = large
        cur = head
        while cur:
            if cur.val < x:
                small.next = cur
                small = cur
            else:
                large.next = cur
                large = cur
            cur = cur.next
        large.next = None
        small.next = large_dummy.next
        return small_dummy.next
        
            
