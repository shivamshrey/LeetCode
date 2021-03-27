# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        prev = head
        cur = head.next.next
        head = head.next
        head.next = prev
        
        while cur != None and cur.next != None:
            prev.next = cur.next
            prev = cur
            next = cur.next.next
            cur.next.next = cur
            cur = next        
        prev.next = cur
            
        return head
    