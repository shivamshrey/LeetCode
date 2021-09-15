// 146. LRU Cache

class DListNode {
    DListNode next;
    DListNode prev;
    int key;
    int value;
    
    DListNode(int key, int value) {
        this.next = null;
        this.prev = null;
        this.key = key;
        this.value = value;
    }
}

class LRUCache {
    private int capacity;
    private int size;
    private DListNode head;
    private DListNode tail;
    private Map<Integer, DListNode> cache = new HashMap<>();
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        size = 0;
        head = new DListNode(0, 0);
        tail = new DListNode(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        DListNode node = cache.get(key);
        if (node == null)
            return -1;
        moveToTail(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        DListNode node = this.cache.get(key);
        if (node == null) {
            node = new DListNode(key, value);
            addNode(node);
            cache.put(key, node);
            size += 1;
            
            if (size > capacity) {
                key = removeFromHead();
                cache.remove(key);
                size -= 1;
            }
        } else {
            node.value = value;
            moveToTail(node);
        }
    }
    
    private void addNode(DListNode node) {
        // add node to before the tail
        node.next = tail;
        node.prev = tail.prev;
        node.next.prev = node;
        node.prev.next = node;
    }
    
    private void moveToTail(DListNode node) {
        // move node to before the tail
        node.prev.next = node.next;
        node.next.prev = node.prev;
        addNode(node);
    }
    
    private int removeFromHead() {
        // remove node next to head
        int key = head.next.key;
        head.next = head.next.next;
        head.next.prev = head;
        return key;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
