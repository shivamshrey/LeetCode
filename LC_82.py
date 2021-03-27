# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur != None and cur.next != None:
            if cur.val == cur.next.val:
                while cur.next != None and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        
        return dummy.next
    
