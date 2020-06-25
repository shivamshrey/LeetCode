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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null)
            return head;
        
        ListNode tail = head;
        int count = 1;
        
        while (tail.next != null) {
            count++;
            tail = tail.next;
        }
        
        k %= count;
        
        if (k == 0)
            return head;
        
        tail.next = head;
        int stepsToNewTail = count - k;
        
        while (stepsToNewTail-- > 0)
            tail = tail.next;
        
        head = tail.next;
        tail.next = null;
        
        return head;
    }
}
