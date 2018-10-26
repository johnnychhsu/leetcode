# Definition for singly-linked list.
import pdb
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def findPart(head):
        slow = head
        fast = head.next
        while fast != None:
            fast = fast.next
            if fast != None:
                fast = fast.next
                slow = slow.next
        left_head = head
        right_head = slow.next
        slow.next = None
        return left_head, right_head
    
    def merge(left, right):
        if not left:
            return right
        if not right:
            return left

        if left and right:
            if left.val <= right.val:
                result = left
                result.next = merge(left.next, right)
            else:
                result = right
                result.next = merge(left, right.next)
        return result   
 
    def mergeSort(head):
        if head == None or head.next == None:
            return head
        else:
            left_head, right_head = findPart(head)
            # pdb.set_trace()            
            l = mergeSort(left_head)
            r = mergeSort(right_head)
            return merge(l, r)
        
    return mergeSort(head)
            
head = ListNode(4)
a = ListNode(2)
b = ListNode(1)
c = ListNode(3)
d = ListNode(0)
head.next = a
a.next = b
b.next = c
# c.next = d
h = sortList(head)
ans = []
while h:
    ans.append(h.val)
    h = h.next
print (ans)
