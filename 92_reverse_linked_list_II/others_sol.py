class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return head
        dummy = ListNode(None)
        prev = dummy
        prev.next = head
        for i in range(m - 1):
            prev = prev.next
        start = prev.next
        then = start.next
        for i in range(n - m):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        return dummy.next
