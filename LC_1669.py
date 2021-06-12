# 1669. Merge In Between Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        cur = list1
        while cur:
            if count == a - 1:
                start = cur
            if count == b + 1:
                end = cur
                break
            cur = cur.next
            count += 1
        
        cur = list2
        while cur.next:
            cur = cur.next
        
        start.next = list2
        cur.next = end
        
        return list1
        