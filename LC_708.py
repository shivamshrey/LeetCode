# 708. Insert into a Sorted Circular Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head == None:
            node = Node(insertVal)
            node.next = node
            return node
        
        prev, cur = head, head.next
        to_insert = False
        
        while True:
            if prev.val <= insertVal <= cur.val:
                # Case 1: minimumVal of list <= insertVal <= maximumVal of list
                to_insert = True
            elif prev.val > cur.val:
                # Case 2: insertVal lies beyond minimumVal and maximumVal of list
                # Tail element is the largest element in the list
                # and prev is now pointing to it
                if insertVal >= prev.val or insertVal <= cur.val:
                    to_insert = True
            
            if to_insert:
                prev.next = Node(insertVal, cur)
                return head
            
            prev, cur = cur, cur.next
            # if entire list is traversed
            if prev == head:
                break
        
        # Case 3: all values of the list are same
        prev.next = Node(insertVal, cur)
        return head
        