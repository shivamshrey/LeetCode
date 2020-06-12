class MyLinkedList {
    
    class Node {
        int val;
        Node next;
        
        public Node(int val) {
            this.val = val;
        }
        public Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }
    
    private Node head = null, tail = null;
    private int count = 0;
    
    /** Initialize your data structure here. */
    public MyLinkedList() {
        
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        
        if (index < 0 || index >= count)
            return -1;
        
        Node cur = head;
        while (index > 0) {
            cur = cur.next;
            index--;
        }
        
        return cur.val;
        
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {
        Node node = new Node(val);
        
        node.next = head;
        if (head == null)
            tail = node;
        head = node;
        count++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        Node node = new Node(val);
        count++;
        
        if (tail != null)
            tail.next = node;
        else
            head = node;
        tail = node;
        
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        Node node = new Node(val);
        
        if (index <= 0)
            addAtHead(val);
        else if (index == count)
            addAtTail(val);
        else {
            Node cur = head;

            while (index > 1) {
                cur = cur.next;
                index--;
            }

            node.next = cur.next;
            cur.next = node;
            count++;
        }
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= count)
            return;
        
        count--;
        
        if (index == 0) {
            Node node = head.next;
            head = node;
            if (node != null)
                node.next = null;
            if (head == null)
                tail = null;
        } else {
        
            int idx = index;
            Node cur = head;
            while(index > 1) {
                cur = cur.next;
                --index;
            }
            Node node = cur.next;
            cur.next = node.next;
            node.next = null;
            if(idx == count)
                tail = cur;
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */