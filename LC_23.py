# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC: O(n log k)
# SC: O(n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda x, y: True if x.val < y.val else False
        
        dummy = ListNode()
        cur = dummy
        heap = []
        
        for head in lists:
            if head:
                heap.append(head)
        
        heapq.heapify(heap)
        
        while heap:
            node = heapq.heappop(heap)
            cur.next = node
            if node.next:
                heapq.heappush(heap, node.next)
            cur = cur.next
            
        return dummy.next
