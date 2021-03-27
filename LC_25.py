# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None or k == 1:
            return head
        
        dummy = ListNode()
        dummy.next = head
        cur = prev = next = dummy
        count = 0
        
        while cur.next != None:
            cur = cur.next
            count += 1
        
        while count >= k:
            cur = prev.next
            next = cur.next
            
            for _ in range(k - 1):
                cur.next = next.next
                next.next = prev.next
                prev.next = next
                next = cur.next
            prev = cur
            count -= k
            
        return dummy.next
        
