"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# TC: O(n)
# SC: O(1)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        
        cur = head
        while cur != None:
            copy_node = Node(cur.val)
            copy_node.next = cur.next
            cur.next = copy_node
            cur = cur.next.next
        
        cur = head
        while cur != None:
            cur.next.random = cur.random.next if cur.random != None else None
            cur = cur.next.next
        
        copy_head = head.next
        cur1 = head
        cur2 = copy_head
        
        while cur1 != None and cur2.next != None:
            cur1.next = cur1.next.next
            cur1 = cur1.next
            cur2.next = cur2.next.next
            cur2 = cur2.next
        cur1.next = None
        
        return copy_head
    
