# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        head = ListNode(0)
        mark = head
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        while heap:
            cur = heapq.heappop(heap)
            head.next = cur[2]
            head = head.next
            if cur[2].next:
                i += 1
                heapq.heappush(heap, (cur[2].next.val, i, cur[2].next))
        return mark.next
        
