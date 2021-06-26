# 92. Reverse Linked List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        prev_rev = None # prev_rev = node previous to the reversed linked list
        
        for _ in range(left):
            prev_rev = cur
            cur = cur.next
        
        # set the pointers
        rev_tail = cur  # rev_tail = tail of reversed linked list
        prev = None
        
        # reverse
        for _ in range(right - left + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # make appropriate connections
        rev_tail.next = cur
        prev_rev.next = prev
        
        return dummy.next
        