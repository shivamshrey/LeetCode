# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fptr = sptr = None
        cur = head
        
        for i in range(k - 1):
            cur = cur.next
        
        fptr = cur
        sptr = head
        cur = cur.next
        
        while cur != None:
            cur = cur.next
            sptr = sptr.next
            
        fptr.val, sptr.val = sptr.val, fptr.val
        
        return head
