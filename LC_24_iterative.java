// 24. Swap Nodes in Pairs

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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode();
        ListNode prev = dummy;
        prev.next = head;
        
        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;
            prev.next = second;
            first.next = second.next;
            second.next = first;
            prev = first;
        }
        
        return dummy.next;
    }
}
