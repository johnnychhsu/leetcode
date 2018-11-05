# Definition for singly-linked list.
import pdb
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        step_meet_first = 0
        while fast != None:
            pdb.set_trace()
            fast = fast.next
            if fast != None:
                fast = fast.next
                slow = slow.next
                step_meet_first += 1
                if slow == fast:
                    break
        if fast == None:
            return None
        else:
            # run = ListNode(-1)
            run = head
            while run != slow:
                run = run.next
                slow = slow.next
            return run
            
a = ListNode(1)
b = ListNode(2)
a.next = b
b.next = a
sol = Solution()
sol.detectCycle(a)            
                                
            
            
