// 23. Merge k Sorted Lists

// TC: O(n log k)
// SC: O(n)

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> priorityQueue = 
            new PriorityQueue<>(new Comparator<ListNode>() {
                public int compare(ListNode l1, ListNode l2) {
                    return l1.val - l2.val;
                }
            });
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        for (ListNode head : lists) {
            if (head != null) {
                priorityQueue.add(head);
            }
        }
        
        while (!priorityQueue.isEmpty()) {
            ListNode node = priorityQueue.poll();
            cur.next = node;
            cur = cur.next;
            if (node.next != null) {
                priorityQueue.add(node.next);
            }
        }
        
        return dummy.next;
    }    
}
