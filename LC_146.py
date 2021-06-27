# 146. LRU Cache

class DListNode:
    '''Doubly Linked List Node'''
    def __init__(self, key=None, value=None):
        self.prev = self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head = DListNode()
        self.tail = DListNode()
        # assumption: LRU key is next to head
        # and MRU key is before tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: DListNode) -> None:
        '''Always add new node right before tail'''
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        node.next.prev = node
    
    def _remove_from_head(self) -> int:
        '''Remove an existing node from linked list'''
        key = self.head.next.key
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return key

    def _move_to_tail(self, node: DListNode) -> None:
        '''Move node to tail of linked list'''
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self._add_node(node)
        
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        
        # move the accessed node to the tail
        self._move_to_tail(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        
        if not node:
            # add new key before tail
            node = DListNode(key, value)
            self.cache[key] = node
            self._add_node(node)
            self.size += 1
            
            # if capacity is reached, then remove the LRU key
            if self.size > self.capacity:
                key = self._remove_from_head()
                del self.cache[key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_tail(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
