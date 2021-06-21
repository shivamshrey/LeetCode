# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        cur = dummy
        heap = []
        ListNode.__lt__ = lambda x, y: True if x.val < y.val else False # key statement
        for node in lists:
            if node != None:
                heap.append((node.val, node))
        heapq.heapify(heap)
        
        while heap:
            val, node = heapq.heappop(heap)
            cur.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            cur = cur.next
        return dummy.next
    