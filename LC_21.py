# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val <= l2.val:
            head = tail = l1
            cur1 = l1.next
            cur2 = l2
        else:
            head = tail = l2
            cur1 = l1
            cur2 = l2.next

        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            tail = tail.next

        if cur1 == None:
            tail.next = cur2
        elif cur2 == None:
            tail.next = cur1

        return head
