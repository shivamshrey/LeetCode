# 445. Add Two Numbers II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        head = None
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            cur_sum = l1_val + l2_val + carry
            carry = cur_sum // 10
            last_digit = cur_sum % 10
            
            cur = ListNode(last_digit)
            cur.next = head
            head = cur
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carry > 0:
            cur = ListNode(carry)
            cur.next = head
            head = cur
        
        return head
    
    def reverse(self, head):
        prev = None
        cur = head
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev
