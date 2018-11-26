# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        prev = None
        run = head
        cur = head
        while run.next != None:
            prev = run
            run = run.next
            if run.next != None:
                prev = run
                run = run.next
                prev.next = run.next
                temp = cur.next
                cur.next = run
                run.next = temp
                cur = cur.next
                run = prev

        return head
        
        
