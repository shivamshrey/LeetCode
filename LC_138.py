# 138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        # Create and interweave cloned list with original list
        old = head
        while old:
            new = Node(old.val)
            new.next = old.next
            old.next = new
            old = new.next
        
        # Link random pointers of new nodes created.
        old = head
        while old:
            old.next.random = old.random.next if old.random else None
            old = old.next.next
        
        # Unweave the linked list to separate original and cloned list
        old = head
        new = head.next
        copy_head = head.next
        
        while old:
            old.next = old.next.next
            new.next = new.next.next if new.next else None
            
            old = old.next
            new = new.next
        
        return copy_head
        