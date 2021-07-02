# 143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle node
        fptr = head
        sptr = head
        while fptr and fptr.next:
            sptr = sptr.next
            fptr = fptr.next.next
        
        # reverse the second half of the list
        prev = None
        cur = sptr
        
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        # Merge the two lists in alternating fashion
        second = prev # second points to head of reversed list
        first = head # first points to head of original list

        while second.next:
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp
